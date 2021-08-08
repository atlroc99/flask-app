from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/json')
def get_json():
    person = {'name': 'Jamal', 'age': 23, 'gender': 'male', 'isActive': True}
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
