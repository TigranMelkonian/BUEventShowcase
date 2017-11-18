from flask import Flask, render_template, request
import json
import ElasticSearchClient as client
import os

# app = Flask(__name__)
template_dir = os.path.abspath('static')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/create', methods=['POST'])
def create_index():
	client.index_create()

@app.route('/delete', methods=['POST'])
def delete_index():
	client.index_delete() 

@app.route('/searchID',  methods=["POST"])
def search_event_by_id():
	id=request.form['id']
	print("recieved id: ",id)
	info = client.get_event_by_id(id)

	if info == None:
		return "Event does not exist :("
	else:
		return info

@app.route('/search',  methods=["POST"])
def search_event(JSONObj):
	client = ES_Client("")
	JSONDict = json.loads(JSONObj)

	event_info = client.get_event(JSONDict)
	if event_info == None:
		return "Event does not exist :("
	else:
		return event_info

if __name__ == "__main__":
    app.run()