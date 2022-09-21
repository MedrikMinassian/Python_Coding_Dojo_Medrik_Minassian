from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask_app import flash


from pprint import pprint

DATABASE = 'recipes'

class Recipe:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']
        self.user_id = data['user_id']
        if 'first_name' in data:
            self.first_name = data['first_name']
        if 'last_name' in data:
            self.last_name = data['last_name']    
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # ! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_made, under_30, user_id) VALUES (%(name)s,%(description)s,%(instructions)s,%(date_made)s,%(under_30)s,%(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    # ! READ ALL
    @classmethod
    def get_all(cls):
        query = "SELECT recipes.*, first_name FROM recipes JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes

    # ! READ ONE
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        recipe = Recipe(result[0])
        return recipe

    # ! UPDATE
    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s,instructions = %(instructions)s,date_made = %(date_made)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    # ! DELETE
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

@classmethod
def get_recipe_with_users(cls, data):
    query = "SELECT * FROM recipes LEFT JOIN favorites ON favorites.recipe_id = recipes.id LEFT JOIN users ON favorites.user_id = users.id WHERE recipes.id = %(id)s;"
    results = connectToMySQL('recipes').query_db(query, data)
    # results will be a list of recipe objects with the user attached to each row.
    recipe = cls(results[0])
    for row_from_db in results:
        # Now we parse the recipe data to make instances of recipes ="keyword from-rainbow">and add them into our list.
        user_data = {
            "id": row_from_db["users.id"],
            "first_name": row_from_db["first_name"],
            "last_name": row_from_db["last_name"],
            "email": row_from_db["email"],
            "password": row_from_db["password"],
            "created_at": row_from_db["users.created_at"],
            "updated_at": row_from_db["users.updated_at"]
        }
        if row_from_db['first_name']:
            recipe.users.append(user.User(user_data))
        return recipe        