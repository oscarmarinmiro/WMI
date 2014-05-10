__author__ = 'Oscar'

import random
from elasticsearch import Elasticsearch
import time

def getTweetsFromWords(words,lang="en",maxDocs=100,index="twitter_river"):
    
    results = list()

    es = Elasticsearch([{'host':'tesla','port':9200}])
  
    res = es.search(index=index,q="text:"+words+" AND lang:"+lang,fields="text")

    for hit in res['hits']['hits']:
        results.append(hit['fields'])

    
    return results


def getCountFromWords(words, lang="en"):

    es = Elasticsearch([{'host':'tesla','port':9200}])
    res = es.search(index="twitter_river",q="text:"+" AND ".join(words)+" AND lang:"+lang,fields="text")

    return res['hits']['total']
