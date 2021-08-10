from flask import Flask, render_template, url_for, flash, redirect
from werkzeug.wrappers import request
from forms import RegistrationForm, LoginForm

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'dd6b2df8ca878fabec08548731962fa581dfce57118803f55cf3b56e26537b86'

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
        print(f'*** user has been creatd for {registration_form.username.data}')
        flash(f'Account has been created for user {registration_form.username.data}!', category='success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Registration", form=registration_form)


@app.route('/login')
def login():
    login_form = LoginForm()
    return render_template('login.html', title="Login", form=login_form)
