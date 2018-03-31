from data import users
from flask import jsonify
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

people = [rider1, rider2, rider3 ]

print(users)

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

@app.route('/users/<user_id>')
def get_user(user_id):
    user_id = int(user_id)
    print(user_id)
    return jsonify(users[user_id])

@app.route('/users/<user_id>/bikeways/<bikeway_id>')
def get_user_bikeway(user_id, bikeway_id):
    user_id = int(user_id)
    bikeway_id = int(bikeway_id)
    return jsonify(users[user_id]["bikeways"][bikeway_id])

if (__name__ == "__main__"):
  app.run(debug=True)  
