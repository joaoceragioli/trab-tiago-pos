import pickle
from Preprocessiong.Treatment import p5


pkl_filename = 'sentiment_anal'

with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)


pred = pickle_model.predict(p5)

print ('A avaliação é: ' + pred)