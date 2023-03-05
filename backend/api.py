from flask import Flask, render_template, request
from pymongo import MongoClient
# import api_requests.py

# from flask import (Flask, render_template)
from flask_cors import CORS, cross_origin
from flask import Flask, render_template
import json



app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

client = MongoClient("mongodb+srv://test:test@rootdata.glqu7s9.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('familyTree_db')
records = db.get_collection('tree_nodes')


# app = Flask(__name__ template_folder="templates")



# How to make new document (INSERTING) -------------------------

# new = {

#     '_id': 64038dea5d2358542af66a7c,            #ID NUM
#     'age': 4,                                   #AGE
#     'name': "john",                             #NAME
#     'childrenId': 6403900c5d2358542af66a7e,     #CHILD_ID
#     'dob': 2019-03-03T08:00:00.000+00:00,       #Date of Birth
#     'isAlive': true,                            #currentState
#     'parentId': 640390095d2358542af66a7d        #PARENT_ID

# }

# records.insert_one(new)           - for only one document insert
# records.insert_many(new)          - takes list of documents to insert   new = [{ ... }, { ... }, ...]

# Find documents ------------------------------------

# list(records.find())                - returns list of documents (objects, in dictionary)
# record.find_one({'Name': 'john'})   - returns all documents that have name = john

# Update documents ----------------------------------

# updates = {
#     'name': 'Ben'
# }

# records.update_one({'name': 'john'}, {'$set': updates})   - updats key value within dictionary

@app.route('/getNodes/')
def getnames():
    nodes_json = []
    if records.find({}):
        for node in records.find({}).sort("name"):
            # { id: 1, pids: [2], name: 'asdf', gender: 'female', img: 'https://cdn.balkan.app/shared/2.jpg'  }
            #if node["pids"]
            nodes_json.append({"id": node['id'], "pids": node['pids'], "mid": node['mid'], "fid": node['fid'], "name": node['name'], "gender": node['gender']})
    return json.dumps(nodes_json)
    

@app.route('/index')
@cross_origin()
def get_tree():
    return {"name": "bob"}
  #  return render_template('temp.html')


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
