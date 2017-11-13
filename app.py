from flask import Flask, render_template
import json
import ElasticSearchClient as client
from Event import getJSON

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.htm")

@app.route('/create', methods=['POST'])
def create_index():
	client.index_create()

@app.route('/delete', methods=['POST'])
def delete_index():
	client.index_delete() 

@app.route('/search', methods=['GET'])
def search_event_by_id(id):
	info = client.get_event_by_id(id)

	if info = None:
		return "Event does not exist :("
	else:
		return info

@app.route('/search', methods=['GET'])
def search_event(JSONObj):
	client = ES_Client("")
	JSONDict = json.loads(JSONObj)

	event_info = client.search(JSONDict)
	if event_info = None:
		return "Event does not exist :("
	else:
		return event_info
