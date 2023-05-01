# there is module flask and class is Flask
from flask import Flask, render_template, jsonify

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$150,000'
  }
]

# creating an instance of the Flask class
app = Flask(__name__)

# here we are using decorator basically we are passing the below function as argument to app.route funnction
@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS)

@app.route("/jobs")
def listJobs():
  # jsonify helps to convert the data in the json format
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)