from pymongo import Connection
from tdmodel import tdlist_todict

db_host = 'localhost'
db_port = 27017


def persist(tdlist):
    connection = Connection(db_host, db_port)
    db = connection.td
    tdlist_collection = db.tdlist

    #tdlist_doc = {"date" : "2012-FEB-06", 
    #              "tds": [ {"status": "DONE", "number": 1, "text" : "elso feladat"},
    #                       {"status": "TODO", "number": 2, "text" : "masodik feladat"}]}


    tdlist_collection.insert(tdlist_todict(tdlist))
    connection.disconnect()




    