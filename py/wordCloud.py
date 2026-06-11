import pandas as pd 
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from spellchecker import SpellChecker
import re
import matplotlib
matplotlib.use('Agg') 

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

corretor = SpellChecker(language='pt')

stopwordsPortugues = set(stopwords.words('portuguese'))
palavrasExtras = {'pra', 'pro', 'tudo', 'nada', 'fazer', 'ter', 'ser', 'pode', 'sobre'}
stopwordsPortugues.update(palavrasExtras)

df = pd.read_excel("dados.xlsx")
respostas = df[NOME_COLUNA].dropna().astype(str).tolist()

def corrigeTexto(texto):
    palavras = re.findall(r'\b\w+\b', texto.lower())
    palavras_corrigidas = []
    
    for palavra in palavras:
        correcao = corretor.correction(palavra)
        palavras_corrigidas.append(correcao if correcao else palavra)
        
    return " ".join(palavras_corrigidas)

respostasCorrigidas = [corrigeTexto(res) for res in respostas]

texto = " ".join(respostasCorrigidas)
palavras = word_tokenize(texto.lower())

palavrasFiltradas = [p for p in palavras if p.isalnum() and p not in stopwordsPortugues]
textoLimpo = " ".join(palavrasFiltradas)

nuvemPalavras = WordCloud(
    width=1000, 
    height=500, 
    background_color='black',
    colormap='OrRd_r',
    max_words=100,
    min_font_size=10,
    contour_width=2,
    margin=10,
).generate(textoLimpo)

plt.figure(figsize=(12, 6))
plt.imshow(nuvemPalavras, interpolation='bilinear')
plt.axis('off') 
plt.tight_layout(pad=0)

plt.savefig('nuvemDePalavras.png', dpi=300, bbox_inches='tight')
plt.close()

print("salvou aqui.")