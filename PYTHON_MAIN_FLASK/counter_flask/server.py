from crypt import methods
from flask import Flask, render_template, request,redirect, session
app = Flask(__name__)
app.secret_key="count"  


@app.route('/')          
def index():
    if 'count' not in session:
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






    
if __name__== "__main__":       
    app.run(debug=True, port=5001)