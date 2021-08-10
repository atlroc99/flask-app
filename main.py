from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates')

posts = [
    {
        'author': 'Mohammad Zaman',
        'title': 'learn python',
        'content': 'Learning python the hard way',
        'created_on': 'April 21, 2021',
        'difficulty_level': 'intermediate'
    },
    {
        'author': 'Joe Shaperd',
        'title': 'learn Java',
        'content': 'Learning Java the hard way',
        'created_on': 'April 24, 2022',
        'difficulty_level': 'intermediate'
    },
    {
        'author': 'James Dean',
        'title': 'Learn Kubernetes',
        'content': 'Learning K8S the hard way',
        'created_on': 'April 21, 2021',
        'difficulty_level': 'intermediate'
    },

]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home", posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title="About")
