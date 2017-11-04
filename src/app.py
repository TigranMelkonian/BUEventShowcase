from flask import Flask, render_template

import ElasticSearchClient
ElasticSearchClient.path.append("/..")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("/../frontEnd/index.html")

def checkEventID(event):
	if event.id in ElasticSearchClient.es:
		print("Event is already in database.")
	else
		database[event.id] = event
		print("Event is not in database.")

def createIndex():
	ElasticSearchClient.createIndex()

