from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def helloworld():
    return "API LINDA!"

@app.route('/macaco')
def monkeyday():
    return render_template('index.html')

@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number+1)
    
@app.route('/<string:name>/')
def hello(name):
    return "Hello " + name


if __name__ == '__main__':
    app.run(debug=True)