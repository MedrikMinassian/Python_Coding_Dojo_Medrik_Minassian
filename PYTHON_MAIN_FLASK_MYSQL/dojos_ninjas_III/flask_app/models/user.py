# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
# model the class after the user table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users').query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append( cls(user) )
        return users
    @classmethod
    def save(cls,data):
        query= "INSERT INTO users (first_name, last_name, email)VALUES(%(first_name)s,%(last_name)s,%(email)s);"
        return connectToMySQL('users').query_db(query,data)
    @classmethod
    def update(cls,data):
        query="Update users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s WHERE id=%(id)s"    
        return connectToMySQL('users').query_db(query,data)

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users').query_db(query,data)
        pprint(results)
        # Create an empty list to append our instances of users
        user=User(results[0])
        print(user.first_name)
        return user
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM users WHERE id=%(id)s;"
        print('user was deleted')
        return connectToMySQL('users').query_db(query,data)
        
