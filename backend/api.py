from flask import Flask, render_template
from pymongo import MongoClient
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app = Flask(__name__, template_folder="templates")

client = MongoClient("mongodb+srv://test:test@rootdata.glqu7s9.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('familyTree_db')
records = db.tree_nodes
doc_count = records.count_documents({})

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


@app.route('/index')
@cross_origin()
def get_tree():
    # return render_template('temp.html')
    return {"name": "bob"}


@app.route('/getNode/<personId>')
def get_person(personId):
    return ("the person you returned is " + personId)


@app.route('/addNode')
def add_person():
    return "adding a new person"


# @app.route()
if __name__ == '__main__':
    app.run(debug=True)