from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500))
    done = db.Column(db.Boolean)

@app.route("/")
def home():
    return render_template("base.html")


@app.route("/timer")
def timer():
    return render_template("timer.html")


@app.route("/notes")
def notes():
    #show all notes
    notes_list = note.query.all()
    print(notes_list)
    return render_template("notes.html", notes_list=notes_list)

'''
Routes for operations on notes start
'''

#add a new note
@app.route("/add_note", methods=['GET', 'POST'])
def add_note():
    content = request.form.get('content')
    new_note = note(content=content, done=False)
    db.session.add(new_note)
    db.session.commit()
    return redirect(url_for('notes'))


#route to update a particular note
@app.route('/update/<int:note_id>')
def update(note_id):
    #update status of note from not done to done
    Note = note.query.filter_by(id=note_id).first()
    Note.done = not Note.done
    db.session.commit()
    return redirect(url_for('notes'))


#route to delete a particular note
@app.route('/delete_note/<int:note_id>')
def delete_note(note_id):
    #delete a note
    Note = note.query.filter_by(id=note_id).first()
    db.session.delete(Note)
    db.session.commit()
    return redirect(url_for('notes'))


'''
Routes for operations on notes end
'''

'''
Routes for operations on timer start
'''

#route to select a time period
@app.route('/select_time')
def select_time():
    return render_template("select_time.html")


#route for displaying the timer
@app.route('/timer', methods=['GET', 'POST'])
def start_timer():
    if request.form.get('15 min'):
        time = 900
    elif request.form.get('30 min'):
        time = 1800
    elif request.form.get('45 min'):
        time = 2700
    elif request.form.get('60 min'):
        time = 3600
    else:
        if(request.form.get('time')== ''):
            time = 600

        else:
            time = int(request.form.get('time'))*60


    return render_template("timer.html",time=time)


'''
Routes for operations on timer end
'''


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
