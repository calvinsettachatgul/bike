from flask import Flask, render_template
import json 
from data import people

app = Flask(__name__)

@app.route('/')
def index():
    print(people)
    return render_template('index.html', people=people)

@app.route('/users')
def get_users():
    return render_template('index.html', people=people)


@app.route('/calvin')
def hello_world_calvin():
    return render_template('user_show.html', rider=people[0])
    # json.dumps(person1)

@app.route('/wendy')
def hello_world_wendy():
    return render_template('user_show.html', rider=people[1])

if (__name__ == "__main__"):
  app.run(debug=True)
