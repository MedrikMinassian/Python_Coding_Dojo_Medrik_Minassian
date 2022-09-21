from flask_app import app, render_template, request, redirect,session, bcrypt, flash
from flask_app.models.painting import Painting


# ! CREATE

@app.route("/painting/new")
def painting_new():
    return render_template("new_painting.html", paintings=Painting.get_all())

@app.route('/new_painting', methods=['POST'])
def new_painting():
    print(request.form)
    Painting.save(request.form)
    return redirect('/paintings')

# ! READ ONE

@app.route('/painting/<int:id>')
def show(id):
    data = {'id': id}
    return render_template('show.html', painting=Painting.get_one(data))


# ! READ/RETRIEVE ALL

@app.route('/painting')
def paintings():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('paintings.html', paintings=Painting.get_all())

# ! UPDATE

@app.route('/edit/<int:id>')
def edit_painting(id):
    data = {'id': id}
    return render_template('edit_painting.html', painting = Painting.get_one(data))

@app.route('/update/painting', methods = ['POST'])
def update_painting():
    print(request.form)
    Painting.update(request.form)
    return redirect('/paintings')

# ! DELETE

@app.route('/delete/<int:id>')
def delete_painting(id):
    data = {'id': id}
    Painting.destroy(data)
    return redirect('/paintings')

@app.route('/paintings')
def all_paintings():
    # Medrik, add this to any route the user must be logged in to view!
    if 'user_id' not in session:
        return redirect('/logout') 
    paintings = Painting.get_all()
    return render_template('paintings.html', paintings=paintings, page_title='Paintings')

