from flask import render_template, redirect, url_for, flash
from blogpost import app
from blogpost.forms import RegistrationForm, LoginForm
from blogpost.models import User, Post

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

emails = [
    {'test@email.com': 'password'},
    {'test@gmail.com': 'password2'},
    {'user@nowhere.com': 'password2'},
    {'jeffry.zaman@gmail.com': 'password4'},
    {'user5@gmail.com': 'password5'},
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
