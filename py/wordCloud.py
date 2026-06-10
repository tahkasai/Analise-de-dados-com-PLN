import pandas as pd 
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib
matplotlib.use('Agg') 

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

df = pd.read_excel("dados.xlsx")
coluna_alvo = 'O que poderia ser melhorado na organização do trabalho ou na distribuição das atividades?'
respostas = df[coluna_alvo].dropna().astype(str).tolist()

texto = " ".join(respostas)
palavras = word_tokenize(texto.lower())
stopwordsPortugues = set(stopwords.words('portuguese'))
palavras_extras = {'pra', 'pro', 'tudo', 'nada', 'fazer', 'ter', 'ser', 'pode', 'sobre'}
stopwordsPortugues.update(palavras_extras)

palavras_filtradas = [p for p in palavras if p.isalnum() and p not in stopwordsPortugues]
textoLimpo = " ".join(palavras_filtradas)

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