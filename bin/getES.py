__author__ = 'Oscar'

import random
from elasticsearch import Elasticsearch
import time
import requests
import json
import pprint
import sys

PAGE_SIZE = 100000

def getTotalDocs(lang="en"):

    url = "http://assets.outliers.es/es/twitter_river/_search"

    params = {'q': "lang="+lang}

    res = requests.get(url, params = params)

    return res.json()['hits']['total']




def getTweetsFromWords(words,lang="en",maxDocs=100,index="twitter_river"):
    
    results = list()

    url = "http://assets.outliers.es/es/twitter_river/_search"

    params = {'q': "text:"+ words + " AND lang="+lang, 'fields':"text", "size": PAGE_SIZE}

    res = requests.get(url, params = params)

    data = json.loads(res.text)['hits']['hits']

    myCount = json.loads(res.text)['hits']['total']

    print data

    for entry in data:
        print entry
        results.append(entry['fields'])

    print "LONGITUD: %d" %  len(results)

    #es = Elasticsearch([{'host':'assets.outliers.es/es','port':80}])
  
    #res = es.search(index=index,q="text:"+words+" AND lang:"+lang,fields="text")

    #print res['hits']['hits']

    #for hit in res['hits']['hits']:
    #    results.append(hit['fields'])

    
    return results,myCount


def getCountFromWords(words, lang="en", index="twitter_river"):

    query = " AND ".join(words)
    url = "http://assets.outliers.es/es/twitter_river/_search"

    print "Mandando"
    pprint.pprint(url)
    pprint.pprint(words)

    params = {'q': query+" AND lang="+lang, 'fields':"text"}

    pprint.pprint(params)

    try:
        res = requests.get(url, params = params)
        print res
        data = json.loads(res.text)
        print data
        #es = Elasticsearch([{'host':'tesla','port':9200}])

        #res = es.search(index=index,q="text:"+" AND ".join(words)+" AND lang:"+lang,fields="")

        return data['hits']['total']
    except:
        return 0
