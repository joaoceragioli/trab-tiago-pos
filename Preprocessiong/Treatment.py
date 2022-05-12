#tokenizing and lowercasing

from Preprocessiong.__core__ import no_alphas, remontar_frase
from nltk.tokenize import word_tokenize

p1 = .str.lower().apply(word_tokenize)

#removing numbers
p2 = p1.pt_token.apply(no_alphas)

#removing stopwords and pontuation
from nltk.corpus import stopwords
from string import punctuation

stw = stopwords.words('portuguese')
pontuacao = list(punctuation)
stw_pt = set( stw + pontuacao )

stw_pt = remove_acento(stw_pt)

p3 = p2.pt_noalpha.apply(remove_acento)

p4 = p3.pt_noalpha_acento.apply(remove_stops, stopwords_pt=stw_pt )

p5 = p4.apply(remontar_frase)
