from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'dd6b2df8ca878fabec08548731962fa581dfce57118803f55cf3b56e26537b86'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

''''
    1 user has many post -> posts has only only user
    1 to many relationship
'''


class User(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    # A User's relationship with Post
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self) -> str:
        return f"User('{self.username}', '{self.email}, '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    posted_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    # each post's relationship with its user
    # user.id -> table name and column name
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self) -> str:
        return f" {self.title},{self.posted_on}"


posts = [
    {
        'author': 'Mohammad Zaman',
        'title': 'Learn Python 3.8+',
        'content': 'Learning python the hard way',
        'date_posted': 'April 21, 2021',
        'difficulty_level': 'intermediate'
    },
    {
        'author': 'Joe Shaperd',
        'title': 'Microservices with springboot',
        'content': 'Learning Java the hard way',
        'date_posted': 'April 24, 2022',
        'difficulty_level': 'intermediate'
    },
    {
        'author': 'James Dean',
        'title': 'Learn Kubernetes :  K8S',
        'content': 'Learning K8S the hard way',
        'date_posted': 'April 21, 2021',
        'difficulty_level': 'intermediate'
    },
    {
        'author': 'Neal Hundson',
        'title': 'AWS API Gateway and Lambda Function',
        'content': 'Build Nano-services with AWS API Gateway and Lambda Function',
        'date_posted': 'April 21, 2021',
        'difficulty_level': 'Advance'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home", posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title="About")


@app.route('/register', methods=['GET', 'POST'])
def register():
    registration_form = RegistrationForm()

    print(f'*** inside regsiter {registration_form.username.data}')

    if registration_form.validate_on_submit():
        print(
            f'*** user has been creatd for {registration_form.username.data}')
        flash(
            f'Account has been created for user {registration_form.username.data}!', category='success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Registration", form=registration_form)


@app.route('/login', methods=['GET', 'POSt'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'test@email.com' and login_form.password.data == 'password':
            flash(
                f'User {login_form.email.data} has successfully logged in.', category='success')
            return redirect(url_for('home'))

    return render_template('login.html', title="Login", form=login_form)
