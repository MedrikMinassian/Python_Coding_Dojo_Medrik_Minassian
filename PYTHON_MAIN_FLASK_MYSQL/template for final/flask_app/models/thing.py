
from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint

DATABASE = 'schema_name'

class Thing:

    def __init__(self, data) -> None:
        self.id = data['id']
        self.column1 = data['column1']
        self.column2 = data['column2']
        self.column3 = data['column3']
        self.column4 = data['column4']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # ! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO things (column1, column2, column3, column4) VALUES (%(column1)s,%(column2)s,%(column3)s,%(column4)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    # ! READ ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM things"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        things = []
        for thing in results:
            things.append(cls(thing))
        return things

    # ! READ ONE
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM things WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        thing = Thing(result[0])
        return thing

    # ! UPDATE
    @classmethod
    def update(cls,data):
        query = "UPDATE things SET column1 = %(column1)s, column2 = %(column2)s,column3 = %(column3)s,column4 = %(column4)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    # ! DELETE
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM things WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

