import json

from flask import Flask, request, current_app, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html', name="ALC- Autobots ")



@app.route('/user/<name>')
def user(name):
    return f'Hello, user: {name}'


@app.route('/user/<int:id>')
def user_by_id(id):
    return f'found user for id: {id}'


@app.route('/user/dob/<dob>')
def user_by_dob(dob):
    return f'found user wiht DOB: {dob}'


@app.route('/print-request-object')
def print_request_object():
    print('request object is an Instance of Request class: ', 'https://docs.python-requests.org/en/master/api/')

    print(f'*** request object class: {request.__class__}')
    print(f'*** request object repr: {request.__repr__()}')
    print(f'*** Object type request: {type(request)}')
    print(f'*** request-useragent: {request.user_agent}')
    print(f"*** request.headers.get(User-agent): {request.headers.get('User-Agent')}")
    print(f'request.method: {request.method}')
    print(f'request.cookies: {request.cookies} and Length of cookies: {len(request.cookies)}')
    print(f'request.data: {request.data}')
    print(f'request.url: {request.url}')
    print(f'get_json: {request.get_json()}')
    url_map_str = str(current_app.url_map)
    print('url_map_str', url_map_str)
    url_map_list = url_map_str.split('>,')
    request_values = f'*** request.values type: {type(request.values)} |  size:  {len(request.values)} | and values: {request.values}'
    request_form = f'*** request.form type: {type(request.form)} | size : {len(request.form)} | form : {request.form}'
    print(request_values)
    print(request_form)
    return {
        'body': {
            'request-object': 'https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request',
            'User-Agent': request.headers.get('User-Agent'),
            'json': request.get_json(),
            'url-map': url_map_list,
            'request_values': request_values,
            'request_form': request_form,
            'remote_addr': request.remote_addr,
            'remote_user': request.remote_user,
            'is_secure': request.is_secure,
            'endpoint[request-handler / method-name]': request.endpoint
        }
    }, 200


@app.route('/test-current-app')
def test_current_app():
    print(f'current_app: {current_app.name}')
    app_ctx = app.app_context()
    app_ctx.push()
    print(f'current_app: {current_app.name}')
    app_ctx.pop()
    return 'testing current app'

