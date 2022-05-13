import pickle
from re import X
from Treatment import transform

s = 'Bigode não confia em mim'

x = transform(s)

pkl_filename = './sentiment_anal.pkl'

with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)


pred = pickle_model.predict([[x]])

print ('A avaliação é: ' + pred)