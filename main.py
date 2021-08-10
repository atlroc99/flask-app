from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates')

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
