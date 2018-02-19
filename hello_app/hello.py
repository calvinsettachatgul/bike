from flask import Flask, render_template
import json 

app = Flask(__name__)

person1 = { "name": "calvin", 
            "location": "San Mateo"}

@app.route('/')
def hello_world():
    return render_template('user_show.html', rider=person1)
    # json.dumps(person1)
