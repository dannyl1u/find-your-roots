from flask import Flask, render_template
import api_requests.py
doc_search(search_val)
app = Flask(__name__)


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
def get_tree():
    string = "hello world - main page \n The count of documents is:"
    return (string)


@app.route('/getNode/<personId>')
def get_person(personId):
    return ("the person you returned is " + personId)


@app.route('/addNode')
def add_person():
    return "adding a new person"


# @app.route()
if __name__ == '__main__':
    app.run(debug=True)
