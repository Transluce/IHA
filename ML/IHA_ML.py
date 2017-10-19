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
#light intent
def lights():
    global response,condition,predString
    print(commands)
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
def searcher():
    from IHA_GoogleSearch import search
    print("'"+speech[0]+"'")
    doc=nlp(speech[0])
    #print(doc[0].text, doc[0].ent_iob, doc[0].ent_type_)
    entityCount=0
    nouns=[]
    for word in doc:
        if word.pos_=="NOUN":
            entityCount+=1
            nouns.append(word.text)
        print(word.pos_)
    if entityCount==2:
        searchString=nouns[1]
    else:
        searchString=speech[0]
    #searchString=speech[0].split()[2]
    search(searchString)
#Start of Program
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice',voices[1].id)
#Loading English model of spacy
nlp=spacy.load('en')
vectorizer = CountVectorizer(tokenizer=tokenizeText, ngram_range=(1,1))
clf = LinearSVC()
pipeline=Pipeline([("cleanText",CleanTextTransformer()),("vectorizer",vectorizer),("clf",clf)])
#Get commands
commands_file=open("commands.ibf","r+")
commandsLabel_file=open("commands_label.ibf","r+")
commands_file.seek(0)
commandsLabel_file.seek(0)
commands=commands_file.read().split(",")
commandLabel=commandsLabel_file.read().split(",")

#train
pipeline.fit(commands, commandLabel)
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
        string=predString.split('-')[0]
        #predString=predString[2:len(predString)-2]
        case={"lights":lights,
              "search":searcher
              }
        case[string]()
commands_file.close()
commandsLabel_file.close()  

   
       

