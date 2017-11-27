'''
11/18/17
New Version of Elastic Search
'''
## I probably dont need all of these. just have them here for future functions / methods
from elasticsearch import Elasticsearch, RequestsHttpConnection
from elasticsearch import client
from elasticsearch import helpers
from requests_aws4auth import AWS4Auth
import argparse
import json
import requests
import sys
import copy

class ES_Client:
    def __init__(self,aws_access_code, aws_secret_code):
        self.es = None
        self.client = None

        host = 'search-bueventshowcase-2vvvoxbm5u73pdzuqois4u2aru.us-east-2.es.amazonaws.com'
        awsauth = AWS4Auth( aws_access_code, aws_secret_code, 'us-east-2', 'es')
        try:
                #this is hard coded
                self.indexName = 'Events'
                self.es = Elasticsearch(
                      hosts=[{'host': host, 'port': 443}],
                      http_auth=awsauth,
                      use_ssl=True,
                      verify_certs=True,
                      connection_class=RequestsHttpConnection) 
                self.client = client.IndicesClient(self.es)    
        except:
                print ("Connection to Elasticsearch host %s failed.",es)
        
    #deletes all the nodes inside a given index  and the index itself fro the cluster
    def index_delete( self, indexLabel):
        print('indexLabel is ' + indexLabel)
        if self.client != None and self.client.exists(index=indexLabel):
            print('deleting...')
            self.client.delete(index=indexLabel)

    #deletes individual Nodes
    def delete_node(self, nodeLabel):
        print('nodeLabel is ' + nodeLabel)
        if self.client != None and self.client.exists(index=self.indexName):
            print('deleting...')
            self.es.delete(index=self.indexName, doc_type="event",id=int(nodeLabel))

    def send_events_to_ES(self, eventList):
        #docL=self.checkFormatting(eventList)
        #print(docL)
        r0   = { '_op_type': "",
                 '_index':self.es,
                 '_type':"",
                 '_id':int,
                 'eventName':"", 'organizer': "",'participants':"",'description':"",'tags':[],'registrationRequired':bool,'location':"",'address':'','city':'','zipCode':"",'startTime':"",'endTime':"",'duration':int,'cost':int,'minCost':int,'maxCsot':int,'refundPolicy':bool,'subOrganizers':"",'sponsors':""}        
        docL = []
        for event in eventList:
            print("Sending Event: ",event)
            try:
                entry=copy.deepcopy(r0)
                for key in r0:

                    if key in event:
                        entry[key]=event.get(key)
                docL.append(entry)
            except:
                print ('error that prevents sending event to stic')
        print(docL)
        self._bulk_insert( docL )

    #adds multiple nodes to the default index
    def _bulk_insert(self, eventList):
        try:
            helpers.bulk(client=self.es,actions=eventList,stats_only=True) 
            #for event in docL:
             #   print(event)
                #helpers.bulk(client=self.es, actions=event, index=event['_index'], stats_only=True)
        except Exception as e:
            print ('elastic bulk send error: '+str(type(e)))

    #gets nodes based on index ID
    def get_info(self, nodeIndex):
        if self.client !=None and self.client.exists(index=self.indexName):
          return self.es.get(index=self.indexName, id=int(nodeIndex))

    #returns the number of nodes in our cluster
    def _count(self):
    	return self.es.count(index=self.indexName)

    #returns a list of nodes that match the query
    def description_search(self, criteria):
        if self.client !=None and self.client.exists(index=self.indexName):
            return self.es.search(index=self.indexName, doc_type='event', q=criteria)
        else:
            return "no matches!"



if __name__ == '__main__':

    #aws_access_code = input('Pass access')
    #aws_secret_code = input("secret please:")

    passwords = json.load(open("auth.json"))
    aws_access_code = passwords["AWSAccessKeyId"]
    aws_secret_code = passwords["AWSSecretKey"]

    #EsTest = ES_Client(aws_access_code, aws_secret_code)	
    EsTest = ES_Client(aws_access_code, aws_secret_code)



    eventList = [{ '_op_type':'index',
                       '_index':'Events',
                       '_type':"event",
                       '_id':1,
                       'eventName':"testEvent1", 'organizer': "Tigran",'participants':"andy",'description':"first tiger input",'tags':[],'registrationRequired':True,'location':"GSU",'address':'near mugar','city':'Boston','zipCode':"02215",'startTime':"now",'endTime':"end",'duration':120,'cost':3,'minCost':0,'maxCost':3,'refundPolicy':False,'subOrganizers':"andy",'sponsors':"none"
                    },
                    { '_op_type':'index',
                       '_index':'Events',
                       '_type':"event",
                       '_id':5,
                       'eventName':"testEvent1", 'organizer': "Tigran",'participants':"andy",'description':"first tigre input",'tags':[],'registrationRequired':True,'location':"GSU",'address':'near mugar','city':'Boston','zipCode':"02215",'startTime':"now",'endTime':"end",'duration':120,'cost':3,'minCost':0,'maxCost':3,'refundPolicy':False,'subOrganizers':"andy",'sponsors':"none"
                    },
                    { '_op_type':'index',
                       '_index':'Events',
                       '_type':"event",
                       '_id':8,
                       'eventName':"testEvent1", 'organizer': "Tigran",'participants':"andy",'description':"tiger",'tags':[],'registrationRequired':True,'location':"GSU",'address':'near mugar','city':'Boston','zipCode':"02215",'startTime':"now",'endTime':"end",'duration':120,'cost':3,'minCost':0,'maxCost':3,'refundPolicy':False,'subOrganizers':"andy",'sponsors':"none"
                    }

                    ]
    while(True):
	    action = input("What would you like to do?")	
	    
	    if action=='deleteIndex':
	        indexLabel = input("index label please:")	
	        EsTest.index_delete(indexLabel)
	    elif action =='deleteNode':
	    	nodeLabel = input('node label please:')
	    	EsTest.delete_node(nodeLabel)
	    elif action=='bulkInsert':
	        EsTest._bulk_insert(eventList)
	    elif(action=='getInfo'):
	        nodeindex = input("which node #?")
	        answer =EsTest.get_info(nodeindex)
	        print(answer)
	    elif(action=='count'):
	    	print(EsTest._count())
	    elif(action=='sd'):
	    	criteria = input("what you looking for?")
	    	solution=EsTest.description_search(criteria)
	    	print(solution)
	    else:
	        print("Unknown action:%s",action)
	    pass
