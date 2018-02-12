from flask import Flask
import json 

app = Flask(__name__)

person1 = { "name": "calvin", 
            "location": "San Mateo"}

@app.route('/')
def hello_world():
    return json.dumps(person1)
