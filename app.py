from flask import Flask, render_template
import numpy as np
from numpy.random import randn
from ElasticSearchClient import ES_Client

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.htm")
'''
def checkEventID(event):
	if event.id in ElasticSearchClient.es:
		print("Event is already in database.")
	else:
		database[event.id] = event
		print("Event is not in database.")

def createIndex():
	random = np.random.randn(100000, 200000)
	while(random in client.indices):
		random = np.random.randn(100000, 200000)

	client.indices.create(index=random, ignore=200)

'''

def delete_by_index()

def get_event_by_id(id):
	client = ES_Client(id)

	info = client.get_info(id)
	if info = None:
		return "Event does not exist :("
	else:
		return info



