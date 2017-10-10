"""
For documentation of the webbrowser module,
see http://docs.python.org/library/webbrowser.html
"""
import webbrowser
new = 2 # open in a new tab, if possible
search = input("What do you want to search?: ")
x=len(search)
search2=list(search)
y2=0
while y2 < x:
    if(search2[y2] == ' '):
        search2[y2] = '+'    
    y2+=1
search = "".join(search2)
print(search)
print(x)
# open a public URL, in this case, the webbrowser docs
url = "https://www.google.com.ph/search?q="
url2 = url + search
webbrowser.open(url2,new=new)
