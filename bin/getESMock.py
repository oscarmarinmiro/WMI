__author__ = 'Oscar'

import random
import pprint

geekText = "I'm a geek. I love iphone, star wars, comic and computers"

hipsterText = "I'm a hipster. I love iphone, fixies and beards"

def getTweetsFromWords(words,lang):

    myData = []

    if words=="geek":
        myText = geekText
    else:
        myText = hipsterText

    for i in range(0,random.randint(100,1000)):
        myData.append({'text':myText})

    return myData


def getCountFromWords(words, lang):

    return random.randint(10,100)