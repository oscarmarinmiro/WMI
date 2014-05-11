__author__ = 'Oscar'

import pprint
import re
import math

from getES import getCountFromWords, getTweetsFromWords, getTotalDocs

TOP_WORDS = 50

def getPMI (total, combined, first, second):

    print "DATOSPMI"
    print "%d %d %d %d" % (total, combined, first, second)
    #
    myNum = float(combined+1)
    #
    myDen = float((first*second)+1)

    myResult = math.log(total * myNum / myDen,2)

    #math.log
    #
    # myResult = math.log(myNum+0.01/myDen+0.01)
    #
    # print "%f" % myResult


    return myResult

def getStopWords():

    FILE_IN = "../data/stopwords.txt"

    fileIn = open(FILE_IN,"rb")

    for line in fileIn:
        myWords = line.decode("utf8").split(", ")

    return myWords

def normalizeTokens(myDict):

    myList = []

    topKeys = sorted(myDict.keys(), key = lambda key: myDict[key], reverse=True)[:TOP_WORDS]

    for key in topKeys:
        myList.append({'word': key, 'count': myDict[key]})

    return myList

def getWMIData(wordOne, wordTwo, lang, totalDocs):

    myWords = getStopWords()

    print "1"

    (wordOneTweets, oneCount) = getTweetsFromWords(wordOne, lang)

    print "2"

    oneTexts = [tweet['text'] for tweet in wordOneTweets]

    (wordTwoTweets, twoCount) = getTweetsFromWords(wordTwo, lang)

    twoTexts = [tweet['text'] for tweet in wordTwoTweets]

    myTokensOne = normalizeTokens(getTokensFromTexts(oneTexts, myWords,wordOne,wordTwo))

    #pprint.pprint(myTokensOne)

    myTokensTwo = normalizeTokens(getTokensFromTexts(twoTexts, myWords,wordTwo,wordTwo))

    #pprint.pprint(myTokensTwo)


    finalDict = myTokensOne + myTokensTwo

    finalTokens = {}

    for entry in finalDict:
        finalTokens[entry['word']] = {}

    for key in finalTokens:
        finalTokens[key]['first'] = getCountFromWords([key,wordOne], "en")
        finalTokens[key]['second'] = getCountFromWords([key,wordTwo], "en")
        finalTokens[key]['all'] = getCountFromWords([key], "en")
        finalTokens[key]['firstPMI'] = getPMI(totalDocs,finalTokens[key]['first'], finalTokens[key]['all'],oneCount)
        finalTokens[key]['secondPMI'] = getPMI(totalDocs,finalTokens[key]['second'], finalTokens[key]['all'], twoCount)

    # pprint.pprint(finalTokens)

    finalStruct = []

    for key in finalTokens:
        finalStruct.append({'word': key, 'xPMI': finalTokens[key]['firstPMI'], 'yPMI': finalTokens[key]['secondPMI']})

    #pprint.pprint(finalStruct)

    sortedFirst = sorted(finalStruct, key = lambda entry: entry['xPMI'], reverse = True)

    print "Para %s" % wordOne

    pprint.pprint(sortedFirst)

    sortedSecond = sorted(finalStruct, key = lambda entry: entry['yPMI'], reverse = True)

    print "Para %s" % wordTwo

    pprint.pprint(sortedSecond)


    return

def getTokensFromTexts(texts,myWords,origWord, origWordTwo):

    tokenCounts = {}

    for text in texts:
        tokens = re.split('[\s\.\,\;\']+',text)
        for token in tokens:
            token = token.lower()
            if token not in myWords and len(token)> 2 and token != origWord.lower() and token != origWord.lower() and (token.isalnum() or re.match(r'[#]',token)):
                if token not in tokenCounts:
                    tokenCounts[token] = 0
                tokenCounts[token] +=1
    return tokenCounts


totalDocs = getTotalDocs()

#print "El total de docs es %d" % totalDocs
getWMIData("boy","girl","en", totalDocs)


