from flask_app import app, render_template, request, redirect
from flask_app.models.dojo import Dojo

# ! CREATE

@app.route("/")
def index():
    return render_template("index.html", dojos = Dojo.get_all())

@app.route('/handle_new_dojo', methods=['POST'])
def handle_new_dojo():
    print(request.form)
    Dojo.save(request.form)
    return redirect('/')



@app.route('/dojo/<int:id>')
def show(id):
    data = {'id': id}
    return render_template('show.html', dojo=Dojo.get_one_with_ninjas(data))



@app.route('/dojos')
def dojos():
    return render_template('dojos.html', dojos = Dojo.get_all())




