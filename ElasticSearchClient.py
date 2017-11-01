'''
created on November 1st, 2017

@author Tigran Melkonian
'''
## I probably dont need all of these. just have them here for future functions / methods
from elasticsearch import Elasticsearch, RequestsHttpConnection
from elasticsearch import client
from elasticsearch import helpers
from requests_aws4auth import AWS4Auth
import argparse
import json
import copy
import csv
import requests


host = 'search-eventapplication-ldgoqbtlexdxxkndppin4fmifm.us-east-1.es.amazonaws.com'
awsauth = AWS4Auth('AKIAJYOM6S2EK4QZOUYQ', 'BcMrUsTgVrsoHbIVHR4eToiqP0hs2z9msUQajh3F', 'us-east-1', 'es')

#connect to aws elasticsearch cluster instance : cluster name is "eventapplication"
es = Elasticsearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection)

print(es.info())

#create mapping
mapping=  {
            "properties": {

                "title": {
                    "type":"string",
                    "index":"analyzed"
                },"categories": {
                    "type":"string",
                    "index":"analyzed"
                },"language": {
                    "type":"string",
                    "index":"analyzed"
                },"last_build_date": {
                    "type":"string",
                    "index":"analyzed"
                },"description": {
                    "type":"string",
                    "index":"analyzed"
                },"keywords": {
                    "type":"string",
                    "index":"analyzed"
                },"itunes_id": {
                    "type":"string",
                    "index":"not_analyzed"
                },"first_episode": {
                    "type":"string",
                    "index":"not_analyzed"
                },"first_episode_title": {
                    "type":"string",
                    "index":"analyzed"
                },"last_episode": {
                    "type":"string",
                    "index":"not_analyzed"
                },"last_episode_title": {
                    "type":"string",
                    "index":"not_analyzed"
                },"rank": {
                    "type":"float",
                    "index":"analyzed"
                },"link": {
                    "type":"string",
                    "index":"not_analyzed"
                }
            }
        }

# add test-index to elastic search cluster and link mapping
es.indices.create(index='test-index', ignore=400)
es.indices.put_mapping(index='test-index', body=mapping, doc_type='csv')



