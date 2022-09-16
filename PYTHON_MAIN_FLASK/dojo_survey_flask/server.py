from crypt import methods
from flask import Flask, render_template, request,redirect, session
app = Flask(__name__)
app.secret_key="survey"  


@app.route('/')          
def index():
    if 'survey' not in session:
        session['count']=1 
    else:
        session ['count']+=1
    return render_template ('index.html')




@app.route('/counting',methods=['POST'] )
def counterfunction():
    if request.form['click']=='add':
        session['count']+=1
    elif request.form['click']=='reset':
        session['count']=0
    return redirect('/')

from flask import Flask, render_template, request, redirect # added request and redirect
            
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    session['name']=request.form['name']
    session['email']=request.form['email']
    session['location']=request.form['location']
    return redirect('/results')


@app.route('/results')
def results():
    return render_template('result.html')    


    
if __name__== "__main__":       
    app.run(debug=True, port=5001)