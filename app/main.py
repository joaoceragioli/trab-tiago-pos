from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def helloworld():
    return "API LINDA!"

@app.route('/macaco', methods=["GET"])
def monkeyday():
    return render_template('index.html')

@app.route('/ocrdobigas', methods=["POST"])
def reviewpost():
     input_json = request.get_json(force=True) 
     dictToReturn = {'text':input_json['text']}
     return jsonify(dictToReturn)
