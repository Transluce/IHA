import webbrowser
def search(searchSubject):
    new = 2
    subjectLength=len(searchSubject)
    searchSubjectWords=list(searchSubject)
    charCount=0
    while charCount < subjectLength:
        if searchSubjectWords[charCount] == ' ':
            searchSubjectWords[charCount] = '+'    
        charCount+=1
    search = "".join(searchSubjectWords)
    # open a public URL, in this case, the webbrowser docs
    url = "https://www.google.com.ph/search?q="
    finalUrl = url + search
    webbrowser.open(finalUrl,new=new)
