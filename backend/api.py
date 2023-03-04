from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__, template_folder="templates")


@app.route('/index')
def get_tree():
    return render_template('temp.html')


@app.route('/getNode/<personId>')
def get_person(personId):
    return ("the person you returned is " + personId)


@app.route('/addNode', methods=['POST', 'GET'])
def add_person():
    output = request.form.to_dict()
    name = output["name"]
    return render_template('temp.html', name=name)


# @app.route()
if __name__ == '__main__':
    app.run(debug=True)
