from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from preprocessing.Predict import predict

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def helloworld():
    return "API LINDA!"

@app.route('/macaco', methods=["GET"])
def monkeyday():
    return render_template('index.html')

@app.route('/ocrdobigas', methods=["POST"])
@cross_origin()
def reviewpost():
     input_json = request.get_json(force=True) 
     CU = predict(input_json['text'])
     match CU:
        case 1:
            final = "POSITIVO?"
        case 0:
            final = "NEGATIVO?"
     res = { 'CU' : str(final) } 
     return res
