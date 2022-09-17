from flask_app.models.user import User
from flask_app import app, render_template, request, redirect


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
def create():
    return render_template('Create.html')    

@app.route('/update/<int:id>')
def update(id):
    data={"id":id}
    return render_template('update.html',user=User.get_one(data))


@app.route('/handleupdate',methods=['POST'])
def handleupdate():
    print (request.form)
    User.update(request.form)
    return redirect('/')

@app.route('/user/<int:id>') 
def showuser(id):
    data={"id":id}
    return render_template('users.html',user=User.get_one(data))

@app.route('/delete/<int:id>')
def delete(id):
    data={"id":id}
    User.delete(data)
    return redirect('/')    
    