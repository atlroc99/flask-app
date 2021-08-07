from flask import request, Flask, render_template, session, url_for, redirect, flash
from NameForm import NameForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MY_SECRET_KEY'

bootstrap = Bootstrap(app)


@app.route('/name-form', methods=['GET', 'POST'])
def name_form():
    name = None
    email = None
    gender = None
    name_form = NameForm()
    if name_form.validate_on_submit():
        name = name_form.name.data
        email = name_form.email.data
        gender = name_form.gender.data
        print(f'name: {name} | email: {email}) |  gender: {gender}')
        name_form.name.data = ''
        name_form.email.data = ''
        name_form.gender.data = ''

    return render_template('index.html', form=name_form, name=name, email=email, gender=gender)


# storing form data in a session
@app.route('/name-form-redirect-on-submit', methods=['GET', 'POST'])
def name_form_redirect_on_form_submit():
    print('*** request mehtod: ', request.method)
    name_form = NameForm()

    print('name_form.name.data: ', name_form.name.data)
    print('name_form.email.data: ', name_form.email.data)
    print('name_form.gender.data: ', name_form.gender.data)

    if request.method == 'GET':
        print('clearing out form data')
        session['name'] = ''
        session['gender'] = ''
        session['email'] = ''

    print(f'*** endpoint: name_form_redirect_on_form_submit')
    print(f'*** Before form submitted session: {session}')
    if name_form.validate_on_submit():
        session['name'] = name_form.name.data

        session['gender'] = name_form.gender.data
        session['email'] = name_form.email.data
        return redirect(url_for('display_user_info'))

    print(f'*** after form submitted session: {session}')
    return render_template('index.html', form=name_form, name=session.get('name'), my_session=session)


@app.route('/user-info')
def display_user_info():
    print(f'*** *** *** user-info page- request.session: {session}')
    return render_template('user.html', my_session=session)