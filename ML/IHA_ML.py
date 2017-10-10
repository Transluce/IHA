# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 15:25:06 2017

@author: jm
"""
import speech_recognition as sr
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
import string
import re
import pyttsx3
import spacy
from IHA_Command import predict
from spacy.en import English
STOPLIST = set(stopwords.words('english') + ["n't", "'s", "'m", "ca"] + list(ENGLISH_STOP_WORDS))
# List of symbols we don't care about
SYMBOLS = " ".join(string.punctuation).split(" ") + ["-----", "---", "...", "“", "”", "'ve"]
parser=English()
class CleanTextTransformer(TransformerMixin):
    """
    Convert text to cleaned text
    """


    def transform(self, X, **transform_params):
        return [cleanText(text) for text in X]

    def fit(self, X, y=None, **fit_params):
        return self

    def get_params(self, deep=True):
        return {}
def cleanText(text):
    # get rid of newlines
        text = text.strip().replace("\n", " ").replace("\r", " ")
    
    # replace twitter @mentions
        mentionFinder = re.compile(r"@[a-z0-9_]{1,15}", re.IGNORECASE)
        text = mentionFinder.sub("@MENTION", text)
    
    # replace HTML symbols
        text = text.replace("&amp;", "and").replace("&gt;", ">").replace("&lt;", "<")
    
    # lowercase
        text = text.lower()

        return text
    
# A custom function to tokenize the text using spaCy
# and convert to lemmas
def tokenizeText(sample):
    # get the tokens using spaCy
    tokens = parser(sample)

    # lemmatize
    lemmas = []
    for tok in tokens:
        lemmas.append(tok.lemma_.lower().strip() if tok.lemma_ != "-PRON-" else tok.lower_)
    tokens = lemmas

    # stoplist the tokens
    tokens = [tok for tok in tokens if tok not in STOPLIST]

    # stoplist symbols
    tokens = [tok for tok in tokens if tok not in SYMBOLS]

    # remove large strings of whitespace
    while "" in tokens:
        tokens.remove("")
    while " " in tokens:
        tokens.remove(" ")
    while "\n" in tokens:
        tokens.remove("\n")
    while "\n\n" in tokens:
        tokens.remove("\n\n")

    return tokens

#text to speech
engine = pyttsx3.init()
#rate = engine.getProperty('rate')
#engine.setProperty('rate', rate+10)
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice',voices[1].id)

           
nlp=spacy.load('en')
vectorizer = CountVectorizer(tokenizer=tokenizeText, ngram_range=(1,1))
clf = LinearSVC()
pipeline=Pipeline([("cleanText",CleanTextTransformer()),("vectorizer",vectorizer),("clf",clf)])
commands_file=open("commands.ibf","r+")
commandsLabel_file=open("commands_label.ibf","r+")
commands_file.seek(0)
commandsLabel_file.seek(0)
#commandsDataSet
#commands = ["turn off the lights","turn off the lights in the living room","turn off the lights in the kitchen","turn off the television","turn on the lights","turn on all the lights", "turn on the lights in the kitchen","turn the lights on","turn off all the lights","turn the lights off"]
#commandLabel = ["lights-all=off", "lights-livingRoom=off", "lights-kitchen=off", "television-livingRoom=off", "lights-all=on", "lights-all=on", "lights-kitchen=on","lights-all=on","lights-all=off","lights-all=off"]
commands=commands_file.read().split(",")
commandLabel=commandsLabel_file.read().split(",")

#train
pipeline.fit(commands, commandLabel)

#speech to text

condition =False
response=False
while condition ==False:
    
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Speak:")                                                                   
        audio = r.listen(source)  
        try:
            speech = [r.recognize_google(audio)]
            print (speech)
            condition =True
     
        except sr.UnknownValueError:
            print("Could not understand audio")
            condition =False

#def mainfunction(source):
    
    if condition ==True:
#Predict
        preds=pipeline.predict(speech)
        predString=str(preds[0])
        print(predString)
        #predString=predString[2:len(predString)-2]
        if speech[0] not in commands:
            aiPrediction=predString.split('=')[1]
            print("Do you want me to turn it "+aiPrediction)
            engine.say("Do you want me to turn it "+aiPrediction)
            engine.runAndWait()
            while response==False:
                 with sr.Microphone() as source:                                                                       
                     print("Speak:")
                     audio = r.listen(source)
                     try:
                         responseSpeech = [r.recognize_google(audio)]
                         print(responseSpeech[0])
                         if responseSpeech[0]=="yes":
                             commands_file.write(str(","+speech[0]))
                             commandsLabel_file.write(str(","+predString))
                             commands.extend(speech)
                             commandLabel.append(predString)
                             print(commands)
                             response=True
                         elif responseSpeech[0]=="no":
                             commands.extend(speech)
                             commands_file.write(str(","+speech[0]))
                             
                             if predString[len(predString)-2:len(predString)]=="on":
                                 predStringNew=predString[0:len(predString)-2]
                                 predStringNew+="off"
                             else:
                                 predStringNew=predString[0:len(predString)-3]
                                 predStringNew+="on"
                             commandLabel.append(predStringNew)
                             commandsLabel_file.write(str(","+predStringNew))
                             predString=predStringNew
                             response=True
                     except sr.UnknownValueError:
                        print("Could not understand audio")
            predict(predString)
        else:
            predict(predString)
            condition=False
commands_file.close()
commandsLabel_file.close()
"""
for(sample,pred) in zip(test,preds):
   print(sample, ":", pred) 
"""

   
       

