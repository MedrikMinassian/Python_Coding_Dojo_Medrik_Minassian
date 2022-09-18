from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
from pprint import pprint
DATABASE='dojosandninjasschema'
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.ninjas=[]
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
        #or you can type the below lines as well#
        # row= connectToMySQL(DATABASE).query_db(query, data)
        # return row 

    @classmethod
    def show_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query,data)

        dojo =Dojo(results [0])

        for row in results:
            ninja_dict = {
                'id': row ['ninjas.id'],
                'first_name': row ['first_name'],
                'last_name' : row ['last_name'],
                'age': row ['age'],
                'dojo_id': row ['dojo_id'],
                'created_at': row ['ninjas.created_at'],
                'updated_at': row ['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(ninja_dict))
            return dojo