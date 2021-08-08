from flask import Flask, request, jsonify, redirect, url_for, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SUPER-SECRET-KEY'


@app.route('/json')
def get_json():
    print(f'print session: {session}')
    person_data = session.get('person_data')
    person = {
        'name': person_data.get('username'),
        'location': person_data.get('location'),
        'age': person_data.get('age'),
        'gender': person_data.get('gender'),
        'isActive': person_data.get('isActive')
    }
    print(f'person built form session data: {person}')
    py_dictionary_deconstruction(person)
    return jsonify(person)


@app.route('/query-person')
def using_query_string():
    name = request.args.get('name')
    gender = request.args.get('gender')
    age = request.args.get('age')
    is_active = request.args.get('isActive') in ['1', 'true', 'True']
    print(f'Type of is_active {type(is_active)} : value: {is_active}')
    print(f'bool(is_active): {bool(is_active)}')
    person_dict = {
        'name': name,
        'age': age,
        'gender': gender,
        'isActive': is_active
    }

    return jsonify(person_dict)


@app.route('/user-form')
def test_form():
    user_form = '''
        <form method="POST", action="/process">
            Username: <input type="text" name="username"/>
            Location: <input type="text" name="location"/>
            Age: <input type="text" name="age"/>
            Gender: <input type="text" name="gender"/>
            <label for="isActive">Is active</labele>
            <select name="isActive" id="isActive">
                <option value="True">True</option>
                <option value="False">False</option>
            </select>
            <input type="submit" value="submit">
        </form>
    '''
    return user_form


@app.route('/process', methods=["POST"])
def process():
    print('Processing form: ')
    print(request)
    print(request.form)
    print(f"username: {request.form['username']}")

    person_dict = {
        'username': request.form.get('username'),
        'gender': request.form.get('gender'),
        'age': request.form.get('age'),
        'location': request.form.get('location'),
        'isActive': request.form.get('isActive'),
    }
    print(f'person_dict: {person_dict}')
    session['person_data'] = person_dict
    return redirect(url_for('get_json'))


# http://www.seanbehan.com/destructuring-dictionaries-in-python/
def py_dictionary_deconstruction(person_dict):
    print('====> print dictionary keys:', list(person_dict.keys()))
    username, gender, age, location, is_active = [person_dict[key] for key in list(person_dict.keys())]
    print(f'username: {username}, location: {location},  gender: {gender}, age : {age} , is_active: {is_active}')
