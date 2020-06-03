import urllib.request
import random
import json
#from bs4 import BeautifulSoup
random.seed()

def queryThesaurus(word):
    queryObj = {
        "key": "JrQIYHZrkov1vQ1UEgQA",
        "word": word,
        "language": "en_US",
        "output": "json"
    }
    url = "https://thesaurus.altervista.org/thesaurus/v1?"
    for item in queryObj.items():
        url += item[0] + "=" + item[1] + "&"
    
    url = url[:-1]
    htmlfile = urllib.request.urlopen(url).read()
    response = json.loads(htmlfile)['response']
    ret = []
    for matches in response:
        for syn in matches['list']['synonyms'].split('|'):
            if syn[-1] is ')':
                ret.append(syn[:syn.index(' ')])
            else:
                ret.append(syn)
    return ret


sad = queryThesaurus("sad")
true = queryThesaurus("true")

print(random.choice(sad) + ", but " + random.choice(true))



#true = [None] * 46
#soup = BeautifulSoup(htmlfile, 'html.parser')
#print(soup.prettify())
#soup.find_all('a',class_='css-')[0].get_text()
#soup.find_all(["iv a"]).get_text()
#soup.find_all(["iv a"]).get_text()
#58 TO 104
#i=58
#k = 0
#while i < 105:
#    true.insert(k,soup.select('a')[i].get_text())
#    i = i+1
#    k=k+1
#del true[47:] 
#print(soup.select('a').get_text())


#Sad (46), begins at 59
#url = "https://www.thesaurus.com/browse/sad?s=t"
#htmlfile1 = urllib.request.urlopen(url)
#sad = [None] * 49
#soup1 = BeautifulSoup(htmlfile1, 'html.parser')
#u=59
#j = 0
#while u < 105:
#    sad.insert(j,soup1.select('a')[u].get_text())
#    u = u+1
#    j=j+1
#del sad[46:]


#t = random.randrange(47)

#s = random.randrange(46)


#print(sad[s] + ' but '+true[t])
