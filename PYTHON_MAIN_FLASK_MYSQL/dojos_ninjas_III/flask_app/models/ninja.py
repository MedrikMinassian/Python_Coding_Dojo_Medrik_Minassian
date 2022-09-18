from sqlite3 import Row
from this import d
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'dojosandninjasschema'
class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data ['last_name']
        self.age = data ['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DATABASE).query_db(query)
        ninjas =[]
        for row in results:
            ninjas.append(Ninja(row))
        return ninjas

    @classmethod 
    def save( cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id)VALUES(%(first_name)s, %(age)s,%(dojo_id)s);"
        row = connectToMySQL(DATABASE).query_db(query, data)
        return row
    @classmethod
    def show_one(cls, data):
        query="SELECT * FROM ninjas WHERE id= %(id)s;"
        row= connectToMySQL(DATABASE).query_db(query,data)
        return Ninja(row[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, password=%(password)s WHERE id = %(id)s; "
        row= connectToMySQL(DATABASE). query_db(query,data)
        return row

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        row= connectToMySQL(DATABASE).query_db(query,data)
        return row
