import config

from models import db, Note, Tag

from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm

from wtforms import StringField, SelectField, TextAreaField, SubmitField

app = Flask(config.app_name)
app.config['SQLALCHEMY_DATABASE_URI'] = config.database_uri
app.config['SECRET_KEY'] = config.secret_key

bootstrap = Bootstrap5(app)

db.init_app(app)


with app.app_context():
    tag_choices = Tag.query.with_entities(Tag.text)
    tag_choices = [tag[0] for tag in tag_choices]

    class NoteForm(FlaskForm):
        title = StringField('')
        text = TextAreaField('')

        tag = SelectField('Tag:', choices=tag_choices)

        submit = SubmitField('Save')

    class TagForm(FlaskForm):
        text = StringField('')

        submit = SubmitField('Save')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        Note.query.delete()
        db.session.commit()

    notes = Note.query.all()

    return render_template('index.html', notes=notes)


@app.route('/<int:note_id>/', methods=['GET', 'POST'])
def show(note_id):
    if request.method == 'POST':
        return redirect(url_for('edit_note', note_id=note_id))
    
    note = Note.query.get_or_404(note_id)

    return render_template('show.html', note=note)


@app.route('/<int:note_id>/edit', methods=['GET', 'POST'])
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)
    form = NoteForm(obj=note)

    if request.method == 'POST':
        note.title = request.form.get('title')
        note.text = request.form.get('text')
        note.tag = [Tag.query.filter_by(text=request.form.get('tag')).first()]
        db.session.commit()

        return redirect(url_for('show', note_id=note.id))

    return render_template('edit.html', note=note, form=form)


@app.route('/note/new', methods=['GET', 'POST'])
def create_note():
    form = NoteForm()

    if request.method == 'POST':
        db.session.add(Note(
            text=request.form.get('text'),
            title=request.form.get('title'),
            tag=[Tag.query.filter_by(text=request.form.get('tag')).first()]
        ))
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit.html', action='Create Note', form=form)

@app.route('/tags/', methods=['GET'])
def index_tags():
    tags = Tag.query.all()
    return render_template('tags.html', tags=tags)

@app.route('/tag/new', methods=['GET', 'POST'])
def create_tag():
    form = TagForm()

    if request.method == 'POST':
        db.session.add(Tag(text=request.form.get('text')))
        db.session.commit()

        return redirect(url_for('index'))
    
    return render_template('edit.html', action='Create Tag', form=form)
