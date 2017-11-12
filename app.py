from flask import Flask, render_template
import numpy as np
from numpy.random import randn
#import ElasticSearchClient

app = Flask(__name__)
#client = ElasticSearchClient.es

@app.route('/')
def index():
    return render_template("/../frontEnd/index.htm")
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

def getEventById(id):
	