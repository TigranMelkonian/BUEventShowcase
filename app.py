from flask import Flask, render_template, request
import json
import ElasticSearch
import Event
import os

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
def create_event(org, loc, time, name):
	event = [Event.event(org=org, loc=loc, time=time, name=name)]
	client.send_events_to_ES(event)

@app.route('/delete', methods=['POST'])
def delete_event():
	client.delete_node() 

@app.route('/searchID',  methods=["POST"])
def search_event_by_id():
	id=request.form['id']
	print("recieved id: ",id)
	info = client.get_info(id)
	print(info)

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