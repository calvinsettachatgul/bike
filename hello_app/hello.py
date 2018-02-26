from flask import Flask, render_template
import json 

app = Flask(__name__)

#Maybe create a user_input? Maybe pseudocode this 
#Is there any way to combine all of the riders? 

rider1 = { "name": "calvin", 
           "location": "San Mateo" } 
rider2 = {
	"name": "Wendy",
	"location": "Palo Alto" }         

rider3 = {
	"name": "Dana",
	"location": "Mountain View" }   

@app.route('/')
def hello_world():
    return render_template('user_show.html', rider=person1)
    # json.dumps(person1)

