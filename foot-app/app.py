from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def default_home():
    return "Home page - football application", 200


@app.route('/football', methods=['GET'])
def default_competition():
    return "This is for local football competition event", 200

@app.route('/printlogs', methods=['GET'])
def print():
    print('Get Secret Loaded from environment')
    print(os.environ['MY_SECRET'])
    print('Get ConfigMap Loaded from environment')
    print(os.environ['PLATFORM'])
    return "Printed", 200

# This is for debug mode on
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
