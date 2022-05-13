# Recebe como parametro uma lista de palavras
def no_alphas( frase_tokenizada ):
  return [palavra for palavra in frase_tokenizada if (palavra.isalpha())]

def remove_stops( frase_tokenizada, stopwords_pt ):
  w_token_1_sem_stopwords = [palavra for palavra in frase_tokenizada if palavra not in stopwords_pt]
  return w_token_1_sem_stopwords

import re
import unicodedata

def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

# ============= Cuidado ao usar, ela é lenta! ===============
def removerAcentosECaracteresEspeciais(palavra):

    # Unicode normalize transforma um caracter em seu equivalente em latin.
    nfkd = unicodedata.normalize('NFKD', palavra)
    palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])

    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)
# ============= Cuidado ao usar, ela é lenta! ===============

def remove_acento( frase_tokenizada ):
  frase = []
  for palavra in frase_tokenizada:
    palavra = palavra.replace('á','a')
    palavra = palavra.replace('é','e')
    palavra = palavra.replace('í','i')
    palavra = palavra.replace('ó','o')
    palavra = palavra.replace('ú','u')
    palavra = palavra.replace('ã','a')
    palavra = palavra.replace('õ','o')
    palavra = palavra.replace('ç','c')
    palavra = palavra.replace('â','a')
    palavra = palavra.replace('ê','e')
    palavra = palavra.replace('î','i')
    palavra = palavra.replace('ô','o')
    palavra = palavra.replace('û','u')
    palavra = palavra.replace('à','a')
    palavra = palavra.replace('è','e')
    palavra = palavra.replace('ì','i')
    palavra = palavra.replace('ò','o')
    palavra = palavra.replace('ù','u')
    frase.append( palavra )
  return frase

def stemming_custom( frase_tokenizada, stemmer ):
  frase = []
  for palavra in frase_tokenizada:
    frase.append( stemmer.stem(palavra) )

  return frase

def remontar_frase(frase_tokenizada):
    return ' '.join(frase_tokenizada)