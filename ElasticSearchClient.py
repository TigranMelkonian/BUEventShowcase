'''
created on November 5th, 2017

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


class ES_Client:
    def __init__(self,args):
        self.args = args
        self.es = None
        self.client = None
        host = 'search-eventapplication-ldgoqbtlexdxxkndppin4fmifm.us-east-1.es.amazonaws.com'
        awsauth = AWS4Auth( 'AKIAITWX6QS2WAYB3NPQ', 'yacyjM/f02hTEhRcHdtXEYFdPEuiShutvOWqze2H', 'us-east-1', 'es')
        try:
                self.es = Elasticsearch(
                      hosts=[{'host': host, 'port': 443}],
                      http_auth=awsauth,
                      use_ssl=True,
                      verify_certs=True,
                      connection_class=RequestsHttpConnection)    
        except:
                print ("Connection to Elasticsearch host %s failed.",args.es_host)
        else:
            try:
                    self.client = client.IndicesClient(self.es) 
            except:
                print ("Elasticsearch client interface create failed on host:%s.",args.es_host)
            else:
                self.indexLabel = args.index

    def index_create( self ):
        event=  {
            "properties": {

                "eventName": {
                    "type":"string",
                    "index":"analyzed"
                },"organizer": {
                    "type":"string",
                    "index":"analyzed"
                },"participants": {
                    "type":"string",
                    "index":"analyzed"
                },"description": {
                    "type":"string",
                    "index":"analyzed"
                },"tags": {
                    "type":"string",
                    "index":"analyzed"
                },"registrationRequired": {
                    "type":"string",
                    "index":"analyzed"
                },"location": {
                    "type":"string",
                    "index":"not_analyzed"
                },"address": {
                    "type":"string",
                    "index":"not_analyzed"
                },"city": {
                    "type":"string",
                    "index":"analyzed"
                },"zipCode": {
                    "type":"string",
                    "index":"not_analyzed"
                },"startTime": {
                    "type":"string",
                    "index":"not_analyzed"
                },"endTime": {
                    "type":"float",
                    "index":"analyzed"
                },"duration": {
                    "type":"float",
                    "index":"analyzed"
                },"cost": {
                    "type":"float",
                    "index":"analyzed"
                },"minCost": {
                    "type":"float",
                    "index":"analyzed"
                },"maxCsot": {
                    "type":"float",
                    "index":"analyzed"
                },"refundPolicy": {
                    "type":"float",
                    "index":"analyzed"
                },"subOrganizers": {
                    "type":"float",
                    "index":"analyzed"
                },"sponsors": {
                    "type":"float",
                    "index":"analyzed"
                },"ID": {
                    "type":"float",
                    "index":"analyzed"
                }
            }
        }
        cfg = {
                "settings": {
                     "index": {
                        "number_of_shards":   1,
                        "number_of_replicas": 0
                      }
                },
                    
                "mappings": {
                     "event": event,
                 }
                    
               }
        if self.client != None:
            self.client.create(index=self.indexLabel,body=cfg)
            
    def index_delete( self ):
        if self.client != None and self.client.exists(index=self.indexLabel):
            r = self.client.delete(index=self.indexLabel)

    def send_events_to_ES(self, eventList):
        '''
        Sends list of podcasts to ES
        '''
        r0   = { '_op_type': "",
                 '_index':self.es,
                 '_type':"",
                 '_id':int,
                 'eventName':"", 'organizer': "",'participants':"",'description':"",'tags':[],'registrationRequired':bool,'location':"",'address':'','city':'','zipCode':"",'startTime':"",'endTime':"",'duration':int,'cost':int,'minCost':int,'maxCsot':int,'refundPolicy':bool,'subOrganizers':"",'sponsors':""}        
        docL = []
        #in future would call andy's event.py
        eventList = [{ '_op_type':'index',
                       '_index':'math',
                       '_type':"event",
                       '_id':1,
                       'eventName':"testEvent1", 'organizer': "Tigran",'participants':"andy",'description':"first event input",'tags':[],'registrationRequired':True,'location':"GSU",'address':'near mugar','city':'Boston','zipCode':"02215",'startTime':"now",'endTime':"end",'duration':120,'cost':3,'minCost':0,'maxCsot':3,'refundPolicy':False,'subOrganizers':"andy",'sponsors':"none"
                    },
                     { '_op_type':'index',
                       '_index':'science',
                       '_type':"event",
                       '_id':1,
                       'eventName':"testEvent1", 'organizer': "Tigran",'participants':"andy",'description':"first event input",'tags':[],'registrationRequired':True,'location':"GSU",'address':'near mugar','city':'Boston','zipCode':"02215",'startTime':"now",'endTime':"end",'duration':120,'cost':3,'minCost':0,'maxCsot':3,'refundPolicy':False,'subOrganizers':"andy",'sponsors':"none"
                    }]

        
        print ('sending event to ES')
        for event in eventList:
            try:
                entry=copy.deepcopy(r0)
                for key in r0:
                    if key in event:
                        entry[key]=event.get(key)
                docL.append(entry)
            except:
                print ('error that prevents sending event to stic')
        self._bulk_insert( docL )
                                   
    def _bulk_insert( self, docL ):
        try:
            helpers.bulk(client=self.es,actions=docL,stats_only=True) 
        except Exception as e:
            print ('elastic bulk send error: '+str(type(e)))
            
    def apply_query_settings( self ):
        settings = {
            "settings": {
                "index": {
                    "number_of_replicas": 7
                }
            }            
        }
        if self.client!=None:
            r = self.client.put_settings(body=settings, index=self.indexLabel )
                                   
def parse_pgm_args():

    descStr = """ Perform an operation (create,delete,report)"""
    ap = argparse.ArgumentParser(description=descStr)
    ap.add_argument("-a","--action",          choices=['delete','create','report', 'bulkInsert'])
    ap.add_argument("-x","--index",           default="math")
    return ap.parse_args()

if __name__ == '__main__':
    args = parse_pgm_args()
    EsTest = ES_Client(args)
    
    #delete, report, or create
    
    print (args)
    if  args.action=='create':
        EsTest.index_create()
        EsTest.apply_query_settings()
    elif args.action=='delete':
        EsTest.index_delete()
    elif args.action=='bulkInsert':
        EsTest.send_events_to_ES('eventList')
    else:
        print("Unknown action:%s",args.action)
        
    pass

                                   

