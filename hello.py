from flask import Flask, session, render_template, url_for, redirect
from NameForm import NameForm
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message

import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))  # /Users/Mohammad.Zaman/PycharmProjects/flasky
print('basedir: ', basedir)
# sqlite:////absolute/path/to/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'MY-SECRET-KEY'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = '587'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = "[FlaskY]"
app.config['FLASKY_MAIL_SENDER'] = '<MOHAMMAD ZAMAN> mzaman.aws@gmail.com'

boostrap = Bootstrap(app)
# The db object instantiated from the class SQLAlchemy
# represents the database and provides access
# to all the functionality of Flask-SQLAlchemy.
db = SQLAlchemy(app)
mail = Mail(app)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True, index=True)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    # a role has many users -> one to many
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r >' % self.name


@app.route('/', methods=['GET', 'POST'])
def index():
    name_form = NameForm()
    print('username:', name_form.name.data)
    # checking if the user already exsits in the db
    if name_form.validate_on_submit():
        user = User.query.filter_by(username=name_form.name.data).first()
        print('user', user)
        if user is None:
            user = User(username=name_form.name.data)
            db.session.add(user)
            session['known'] = False
            db.session.commit()
        else:
            session['known'] = True
            session['name'] = user.username
            name_form.name.data = ''
            return redirect(url_for('display_user'))

    return render_template('index.html', name=session.get('name'), form=name_form)


@app.route('/user-info')
def display_user():
    return render_template('user.html', my_session=session)


# @app.shell_context_processors
# def make_shell_context():
#     return dict(db=db, User=User, Role=Role)


@app.route('/mail/<to>', methods=['POST'])
def send_mail(to):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + 'flask-mail',
                  sender=app.config['FLASKY_MAIL_SENDER'])
    msg.body('this is a plain text body')
    msg.body('this is a plain <b>HMTL</b> body')
    msg.subject('flask-mail')
    mail.send(msg)
