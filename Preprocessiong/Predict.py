import pickle
from re import X
from Treatment import transform

def predict(s:str):


    vectorizer = pickle.load(open("vector.pickel", "rb"))

    x = transform(s)

    da = vectorizer.transform([x])
    print(da)

    pkl_filename = './sentiment_anal.pkl'

    with open(pkl_filename, 'rb') as file:
        pickle_model = pickle.load(file)


    pred = pickle_model.predict(da)
    return pred[0]