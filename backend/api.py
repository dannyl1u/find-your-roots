from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__, template_folder="templates")


@app.route('/index')
def get_tree():
    return render_template('temp.html')


@app.route('/getNode/<personId>')
def get_person(personId):
    return ("the person you returned is " + personId)


@app.route('/addNode')
def add_person():
    return "adding a new person"


# @app.route()
if __name__ == '__main__':
    app.run(debug=True)
