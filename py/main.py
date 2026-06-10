# Análise das palavras 
import pandas as pd 
import nltk 
from collections import Counter
import re
from spellchecker import SpellChecker
from nltk.corpus import stopwords

nltk.download('punkt_tab')
nltk.download('stopwords')

corretor = SpellChecker(language='pt')
palavras_vazias = set(stopwords.words('portuguese'))

df = pd.read_excel("dados.xlsx")
respostas = df['O que poderia ser melhorado na organização do trabalho ou na distribuição das atividades?'].dropna().astype(str).tolist()

def corrigeTexto(texto):
    palavras = re.findall(r'\b\w+\b', texto.lower())
    palavras_corrigidas = []
    
    for palavra in palavras:
        correcao = corretor.correction(palavra)
        palavras_corrigidas.append(correcao if correcao else palavra)
        
    return " ".join(palavras_corrigidas)

respostasCorrigidas = [corrigeTexto(res) for res in respostas]

texto = " ".join(respostasCorrigidas)

palavras = nltk.word_tokenize(texto, language='portuguese')

categorias = [
    palavra
    for palavra in palavras
    if palavra not in palavras_vazias and len(palavra) > 5 
]

frequencia = Counter(categorias)

print(frequencia.most_common(40))