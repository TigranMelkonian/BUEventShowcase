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
from Event import Event


#TODO: create spreadsheet that has access codes that inputs to host/auth
host = 'search-eventapplication-ldgoqbtlexdxxkndppin4fmifm.us-east-1.es.amazonaws.com'
awsauth = AWS4Auth( 'AKIAITWX6QS2WAYB3NPQ', 'yacyjM/f02hTEhRcHdtXEYFdPEuiShutvOWqze2H', 'us-east-1', 'es')

data = {}



# add test-index to elastic search cluster and link mapping
def makeMapping(self, es):
    es.indices.create(index='test-index', ignore=400)
    es.indices.put_mapping(index='test-index', body=mapping, doc_type='csv')


#create mapping
mapping=  {
            "properties": {

                "eventName": {
                    "type":"string",
                    "index":"analyzed"
                },"organizer": {
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
                }
            }
        }

event1 =  Event("event1", "IOrganizer", "Participants", "descript", False, "boston", "cost", "date", "endDate")
event1.getJSON()#this just updates dictionary
data = event1.getDictionary()
print(data)
uniqueID = data['eventName'] + data['startTime']

#connect to aws elasticsearch cluster instance : cluster name is "eventapplication"
es = Elasticsearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection)    
print(es.info())

es.indices.create(index=uniqueID, ignore=400)
es.indices.put_mapping(index=uniqueID, body=data, doc_type='JSON')#does not accep data's mapping but accepts mapping. 





