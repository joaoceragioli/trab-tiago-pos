#tokenizing and lowercasing

from .__core__ import no_alphas, remontar_frase, remove_stops, remove_acento
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation


def transform(s:str):
        
    p1 = word_tokenize(s.lower(), language= 'portuguese')
    print(p1)


    #removing numbers
    p2 = no_alphas(p1)

    #removing stopwords and pontuation
    stw = stopwords.words('portuguese')
    pontuacao = list(punctuation)
    stw_pt = set( stw + pontuacao )

    stw_pt = remove_acento(stw_pt)

    p3 = remove_acento(p2)

    p4 = remove_stops(p3,stopwords_pt=stw_pt)


    #rebuilding the phrase
    p5 = remontar_frase(p4)
    return p5
