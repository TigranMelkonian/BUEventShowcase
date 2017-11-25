from flask import Flask, render_template, request
import json
import ElasticSearch
import Event
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

@app.route('/createEvent', methods=["POST"])
def create_event():
	org = request.form['org']
	loc = request.form['location']
	time = request.form['time']
	name = request.form['name']
	mystring = org+name
	# Assumes the default UTF-8
	#hash_object = hashlib.md5(mystring.encode())
	#print(hash_object.hexdigest())
	#scaryid=int(hash_object.hexdigest(),16)
	#print(scaryid)
	event = [Event.Event(org=org, loc=loc, startDate=time, name=name).getDictionary()]
	client.send_events_to_ES(event)

@app.route('/delete', methods=['POST'])
def delete_event():
	client.delete_node() 

@app.route('/searchID',  methods=["POST"])
def search_event_by_id():
	ourID = request.form['id']
	print("received id: ", ourID)
	info = client.get_info(ourI)
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