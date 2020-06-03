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

