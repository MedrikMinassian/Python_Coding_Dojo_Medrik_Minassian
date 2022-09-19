from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint


from flask_app.models.ninja import Ninja
DATABASE = 'dojos_ninjas'

class Dojo:

    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(DATABASE).query_db(query, data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        dojo = Dojo(result[0])
        return dojo


    

    
    @classmethod
    def get_one_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id= %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        pprint(results)
        dojo = Dojo(results[0])
        print(dojo.ninjas)

        for result in results:
            temp_ninja = {
                "id" : result['ninjas.id'],
                "first_name" : result['first_name'],
                "last_name" : result['last_name'],
                "age" : result['age'],
                "dojo_id" : result['dojo_id'],
                "created_at" : result['ninjas.created_at'],
                "updated_at" : result['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(temp_ninja))
        print(dojo.ninjas)
        return dojo