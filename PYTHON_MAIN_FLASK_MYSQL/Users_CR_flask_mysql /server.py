
from flask import Flask, render_template, request,redirect, session
app = Flask(__name__)
app.secret_key="usercr"  

from user import User

DATABASE='users'
@app.route('/')          
def Read_All():
    
    return render_template ('Read_All.html',users=User.get_all())
            
@app.route('/ReadAll', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    User.save(request.form)
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    # session['First_name']=request.form['name']
    # session['Last_name']=request.form['name']
    # session['email']=request.form['email']
    return redirect('/')


@app.route('/Create')
def results():
    return render_template('Create.html')    



# @app.route('/Create', methods=["POST"])
# def create_user():
#     # First we make a data dictionary from our request.form coming from our template.
#     # The keys in data need to line up exactly with the variables in our query string.
#     data = {
#         "fname": request.form["fname"],
#         "lname" : request.form["lname"],
#         "occ" : request.form["email"]
#     }
#     # We pass the data dictionary into the save method from the Friend class.
#     User.save(data)
#     # Don't forget to redirect after saving to the database.
#     return redirect('/ReadAll')
if __name__== "__main__":       
    app.run(debug=True, port=5001)