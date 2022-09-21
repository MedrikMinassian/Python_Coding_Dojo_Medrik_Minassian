from flask_app import app, render_template, request, redirect,session, bcrypt, flash
from flask_app.models.tvshow import Tvshow


# ! CREATE

@app.route("/tvshow/new")
def tvshow_new():
    return render_template("new_tvshow.html", tvshows=Tvshow.get_all())

@app.route('/new_tvshow', methods=['POST'])
def new_tvshow():
    print(request.form)
    if not Tvshow.validate_tvshow(request.form):
        return redirect('/tvshow/new')
    else:
        Tvshow.save(request.form)
        return redirect('/tvshows')

@app.route('/tvshow/new', methods=['POST'])
def validate_new_tvshow(user_data):
    print(request.form)
    
    
    user_data = {
        'name': request.form['name'],
        'description': request.form['description'],
        
    }
    user_id = Tvshow.save(user_data)
    session['user_id'] = user_id
    session['name'] = request.form['name']
    session['description'] = request.form['description']
    
    return redirect('/tvshows')
# ! READ ONE

@app.route('/tvshow/<int:id>')
def show(id):
    data = {'id': id}
    return render_template('show.html', tvshow=Tvshow.get_one(data))


# ! READ/RETRIEVE ALL

@app.route('/tvshows')
def tvshows():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('tvshows.html', tvshows=Tvshow.get_all())

# ! UPDATE

@app.route('/edit/<int:id>')
def edit_tvshow(id):
    data = {'id': id}
    return render_template('edit_tvshow.html', tvshow = Tvshow.get_one(data))

@app.route('/update/tvshow', methods = ['POST'])
def update_tvshow():
    if 'user_id' not in session:
        return redirect('/logout')
    print(request.form)
    if not Tvshow.validate_tvshow(request.form):
        return redirect(f"/edit/{request.form['id']}")
    Tvshow.update(request.form)
    return redirect('/tvshows')

# ! DELETE

@app.route('/delete/<int:id>')
def delete_tvshow(id):
    data = {'id': id}
    Tvshow.destroy(data)
    return redirect('/tvshows')

@app.route('/tvshows')
def all_tvshows():
    if 'user_id' not in session:
        return redirect('/logout')
    tvshows = Tvshow.get_all()
    return render_template('tvshows.html', tvshows=tvshows, page_title='Tvshows')

