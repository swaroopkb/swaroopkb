from flask import *
from werkzeug.middleware.proxy_fix import ProxyFix
import json, time

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Page': 'Home', 'Message': 'Successfully Loaded the Home page', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump

@app.route('/user/', methods=['GET'])
def usere_page():
    user_query = str(request.args.get('user')) # /user/?user=USER_NAME
    data_set = {'Page': 'request', 'Message': f'Successfully Loaded the request page for { user_query}', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)

