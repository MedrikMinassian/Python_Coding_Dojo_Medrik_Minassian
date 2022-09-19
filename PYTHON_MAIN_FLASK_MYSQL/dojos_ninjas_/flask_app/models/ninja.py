from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint

DATABASE = 'dojos_ninjas'

class Ninja:

    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    def do_something_cool(self):
        return "I'm cool"


    
    @classmethod
    def save(cls, data) -> int:
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        ninja = Ninja(result[0])
        return ninja

    