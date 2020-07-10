from flask import Flask
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_world(user):
    return 'Hello ' + user +'!' +' \n' 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
