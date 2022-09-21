
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash
from pprint import pprint
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask_app.models.painting import Painting

DATABASE = 'artistspaintings'

class User:

    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.paintings = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # ! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # ! READ ONE FROM EMAIL
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) > 0:
            return User(result[0])
        else:
            return False
        
    # @classmethod
    # def get_one_with_paintings(cls, data):

    #     query = "SELECT * FROM users LEFT JOIN paintings ON users.id = paintings.user_id WHERE users.id= %(id)s;"
    #     results = connectToMySQL(DATABASE).query_db(query, data)
    #     pprint(results)
    #     user = User(results[0])
    #     print(user.paintings)
    #     for result in results:

    #         temp_painting = {
    #             "id" : result['paintings.id'],
    #             "title" : result['title'],
    #             "description" : result['description'],
    #             "price" : result['price'],
    #             "date_made" : result['date_made'],
    #             "sold" : result['sold'],
    #             "user_id" : result['user_id'],
    #             "created_at" : result['paintings.created_at'],
    #             "updated_at" : result['paintings.updated_at']
    #         }
    #         user.paintings.append(Painting(temp_painting))
    #     print(user.paintings)

    #     return user
        
    @classmethod
    def edit_one_with_paintings(cls, data):

        query = "SELECT * FROM users LEFT JOIN paintings ON users.id = paintings.user_id WHERE users.id= %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        pprint(results)
        user = User(results[0])
        print(user.painting)
        for result in results:

            temp_painting = {
                "id" : result['paintings.id'],
                "name" : result['name'],
                "description" : result['description'],
                "price" : result['price'],
                "date_made" : result['date_made'],
                "user_id" : result['user_id'],
                "created_at" : result['paintings.created_at'],
                "updated_at" : result['paintings.updated_at']
            }
            user.paintings.append(Painting(temp_painting))
        print(user.paintings)

        return user    
    
    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 2:
            is_valid = False
            flash("Sorry, use at least 2 characters for first name")
        if len(user['last_name']) < 2:
            is_valid = False
            flash("Sorry, use at least 2 characters for last name")    
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if len(user['password']) < 8:
            is_valid = False
            flash("your password is not strong enough, please use a minimum of 8 characters.")
        if len(user['password']) != len(user['password']):
            is_valid = False 
            flash("your password does not match")
        return is_valid

    # @staticmethod
    # def registration_validator(self, post_data):
    # errors = {}
    # user_birthday = datetime.strptime(post_data['birthday'], '%Y-%m-%d')
    #     if user_birthday > datetime.today():
    #         errors["release_date"] = "User birthday must be in the past!"
    #     return errors_login   