from pymongo import Connection
from tdmodel import tdlist_todict

db_host = 'localhost'
db_port = 27017

class MongoPersistence():
    
    def __init__(self):
        pass
    
    def setup(self):
        self.__connection = Connection(db_host, db_port)
        db = self.__connection.td
        self.__tdlist_collection = db.tdlist
        
    def teardown(self):
        self.__connection.disconnect()
    
    def persist(self, tdlist):
        #tdlist_doc = {"date" : "2012-FEB-06", 
        #              "tds": [ {"status": "DONE", "number": 1, "text" : "elso feladat"},
        #                       {"status": "TODO", "number": 2, "text" : "masodik feladat"}]}
        
        self.__tdlist_collection.insert(tdlist_todict(tdlist))
    
    
    def search(self, date_str):
        result = self.__tdlist_collection.find_one({"date": date_str})
        return result
    
    def remove(self, date_str):
        self.__tdlist_collection.remove({"date": date_str})

    