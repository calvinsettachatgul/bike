from flask import Flask, render_template
import json 

app = Flask(__name__)
people = [
            { "name": "calvin",
            "location": "San Mateo"}, 
            { "name": "wendy",
            "location": "Redwood City"}, 
]

@app.route('/')
def index():
    print(people)
    return render_template('index.html', people=people)

@app.route('/calvin')
def hello_world_calvin():
    return render_template('user_show.html', rider=people[0])
    # json.dumps(person1)

@app.route('/wendy')
def hello_world_wendy():
    return render_template('user_show.html', rider=people[1])
