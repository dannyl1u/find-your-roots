from pymongo import MongoClient

client = MongoClient("mongodb+srv://test:test@rootdata.glqu7s9.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('familyTree_db')
records = db.tree_nodes


def get_doc_count():
    """
    returns number of documents(objects) in the database
    :return: doc_count: number of documents(objects) in database
    """
    doc_count = records.count_documents({})
    return doc_count

def insert_doc(doc: dict):
    """
    Inserts document(object) into database, should follow: doc = {_id': 64038dea5d2358542af66a7c, 'age': 4, ...}
    Required Key parameters: '_id':,'age':,'name':,'childrenId':,'dob':, 'isAlive','parentId':
    :param: doc: dictionary that you want to insert to database (should contain all required parameters)
    """
    records.insert_one(doc)

def get_doc_all():
    """
    Returns all current documents(objects) into database
    :return: doc_dict: list of all dictionaries that contain the search_val parameter
    """
    doc_dict = list(records.find())
    return doc_dict

def search_doc(search_val: dict):
    """
    Searches and returns document(object) that contains specified search value
    :param: search_val: dictionary value that you want to find in documents(objects), should follow: search_val = {'key': keyVal}
    :return: doc_dict: list of all dictionaries that contain the search_val parameter
    """
    doc_dict = records.find_one(search_val)
    return doc_dict

def update_doc(to_update: dict, changes: dict):
    """
    Updates document(object) for specified hash parameter with specified hash changes
    :param: to_update: dictionary containing key and keyVal of document(object) to be updated, should follow: to_update = {'key': keyVal}
    :param: changes: dictionary containing changed key and keyVal, should follow: changes = {'key': keyVal}
    """
    records.update_one(to_update, {'$set': changes})