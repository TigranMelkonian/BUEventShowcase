from flask import Flask, render_template, request
import json
import ElasticSearch
import os

import hashlib

passwords = json.load(open("auth.json"))
access_code = passwords["AWSAccessKeyId"]
secret_code = passwords["AWSSecretKey"]

client = ElasticSearch.ES_Client(access_code, secret_code)

# app = Flask(__name__)
template_dir = os.path.abspath('static')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/create', methods=['POST'])
def create_index():
	client.index_create()

#this makes the event from the form and sends it to elastic search
@app.route('/createEvent', methods=["GET", "POST"])
def create_event():
	events = []
	event = {}
	event['organizer'] = request.form['org']
	event['location'] = request.form['location']
	event['time'] = request.form['time']
	event['eventName'] = request.form['name']
	events.append(event)
	#mystring = org+name
	# Assumes the default UTF-8
	#hash_object = hashlib.md5(mystring.encode())
	#print(hash_object.hexdigest())
	#scaryid=int(hash_object.hexdigest(),16)
	#print(scaryid)
	
	client.send_events_to_ES(events)
	return "Not sure if successful or not but I need to return something so here you go."

@app.route('/delete', methods=['POST'])
def delete_event():
	client.delete_node() 

@app.route('/searchID',  methods=["POST"])
def search_event_by_id():
	ourID = request.form['id']
	print("received id: ", ourID)
	info = client.get_info(ourID)
	print(info)
	print(json.dumps(info))

	if info == None:
		return "Event does not exist :("
	else:
		return json.dumps(info)

@app.route('/search',  methods=["POST"])
def search_event(jsonStr):
	client = ES_Client("")
	JSONDict = json.loads(JSONObj)

	event_info = client.description_search(JSONDict)
	if event_info == None:
		return "Event does not exist :("
	else:
		return event_info

if __name__ == "__main__":
    app.run()