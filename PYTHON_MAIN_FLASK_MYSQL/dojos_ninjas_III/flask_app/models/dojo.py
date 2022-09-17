from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
DATABASE='dojosandninjasschema'
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of users
        dojos = []
        # Iterate over the db results and create instances of users with cls.
        for row in results:
            dojos.append( Dojo(row) )
        return dojos
    
    @classmethod
    def save(cls,data):
        query= "INSERT INTO dojos (name)VALUES(%(name)s);"
        return connectToMySQL(DATABASE).query_db(query,data)
        