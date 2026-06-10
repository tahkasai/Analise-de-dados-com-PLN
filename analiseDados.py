import pandas as pd 
import nltk 
from collections import Counter

nltk.download('punkt_tab')

df = pd.read_excel("dados.xlsx")
respostas = df['O que poderia ser melhorado na organização do trabalho ou na distribuição das atividades?'].dropna().astype(str).tolist()

texto = " ".join(respostas)

frasesChaves = nltk.sent_tokenize(texto, language='portuguese')

categorias = [
    frase.strip()
    for frase in texto.split()
    if len(frase.strip()) > 5 
]

frequencia = Counter(categorias)

print(frequencia.most_common(30))