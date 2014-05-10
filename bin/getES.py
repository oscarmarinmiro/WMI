__author__ = 'Oscar'

import random
from elasticsearch import Elasticsearch
import time

def getTweetsFromWords(words,lang="en",maxDocs=100,index="twitter_river"):
    es = Elasticsearch([{'host':'tesla','port':9200}])
    res = es.search(index="twitter_river",q="text:"+words+" AND lang:"+lang,fields="text")
    results = list()
    for hit in res['hits']['hits']:
        results.append(hit['fields']['text'])

    return results


def getCountFromWords(words, lang="en"):

    es = Elasticsearch([{'host':'tesla','port':9200}])
    res = es.search(index="twitter_river",q="text:"+" AND ".join(words)+" AND lang:"+lang,fields="text")

    return res['hits']['total']
