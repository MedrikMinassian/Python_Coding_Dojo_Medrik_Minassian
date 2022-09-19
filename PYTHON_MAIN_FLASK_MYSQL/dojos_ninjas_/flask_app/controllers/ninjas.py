from flask_app import app, render_template, request, redirect
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo




@app.route("/ninjas")
def ninjas():
    return render_template("new_ninja.html", dojos = Dojo.get_all())

@app.route('/handle_new_ninja', methods=['POST'])
def handle_new_ninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect(f"/dojo/{request.form['dojo_id']}")


@app.route('/ninja/<int:id>')
def show_ninja(id):
    data = {'id': id}
    return render_template('show.html', ninja=Ninja.get_one(data))



@app.route('/readall')
def readall():
    return render_template('ninjas.html', ninjas = Ninja.get_all())
