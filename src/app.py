from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("/../frontEnd/index.html")

# Alan pls check this - I think you don't pass in a database as a parameter, but instead directly reference it within the function e.g. referencing a mongod
# instance but I'm not sure cause I've never done that stuffs before
def checkEventID(event, database):
	if event.id in database:
		print("Event is already in database. Processing...")
	else
		database[event.id] = event
		print("Event is not in database. Adding to database...")

