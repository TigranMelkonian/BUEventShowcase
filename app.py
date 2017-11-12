from flask import Flask, render_template
import numpy as np
from numpy.random import randn
from ElasticSearchClient import ES_Client

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.htm")

def create_index():
	client = ES_Client()
	client.index_create()

def delete_index():
	client = ES_Client("")
	client.index_delete()

def get_event_by_id(id):
	client = ES_Client(id)

	info = client.get_info(id)
	if info = None:
		return "Event does not exist :("
	else:
		return info



