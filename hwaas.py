from flask import Flask
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_world(user):
    return 'Hello ' + user +'!' +' \n' 