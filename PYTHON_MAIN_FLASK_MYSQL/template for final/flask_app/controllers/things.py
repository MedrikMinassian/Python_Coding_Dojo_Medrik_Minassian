
from flask_app import app, render_template, request, redirect,session
from flask_app.models.thing import Thing

# ! CREATE

@app.route("/thing/new")
def thing_new():
    # call the get all classmethod to get all friends
    return render_template("index.html")

@app.route('/handle_new_thing', methods=['POST'])
def handle_new_thing():
    print(request.form)
    Thing.save(request.form)
    return redirect('/things')

# ! READ ONE

@app.route('/thing/<int:id>')
def show(id):
    data = {'id': id}
    return render_template('show.html', thing=Thing.get_one(data))


# ! READ/RETRIEVE ALL

@app.route('/things')
def things():
    return f"It worked,{session['first_name']} {session['last_name']} !!!"
    # return render_template('things.html', things = Thing.get_all())

# ! UPDATE

@app.route('/edit/<int:id>')
def edit_thing(id):
    data = {'id': id}
    return render_template('edit_thing.html', thing = Thing.get_one(data))

@app.route('/update/thing', methods = ['POST'])
def update_thing():
    print(request.form)
    Thing.update(request.form)
    return redirect('/things')

# ! DELETE

@app.route('/delete/<int:id>')
def delete_thing(id):
    data = {'id': id}
    Thing.destroy(data)
    return redirect('/things')
Footer
