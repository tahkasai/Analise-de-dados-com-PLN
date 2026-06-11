# Análise de dados: Palavras mais utilizadas com PLN
O código analisa um conjunto de dados e traz as palavras mais frequentes.

### Termos
* **Tokenização** é o processo de dividir um texto em unidades menores, conhecidas como tokens.
* **Stopwords** são palavras comuns que normalmente não agregam muito significado ao texto, como artigos, preposições e pronomes.
* **Stemming** é o processo de reduzir uma palavra à sua forma base ou radical. Isso ajuda a lidar com variações de palavras e reduzir a dimensionalidade dos dados.
* **Nuvem de palavras** é uma forma visual de mostrar quais termos aparecem com mais frequência em um texto.

> Link para estudos: [Medium](https://medium.com/@dheiver.santos_10420/t%C3%ADtulo-introdu%C3%A7%C3%A3o-ao-processamento-de-linguagem-natural-pln-com-python-e-a-biblioteca-nltk-a6df2f06d395)

### Bibliotecas

* **pandas**: lê e manipula a planilha Excel com os dados de entrada.
* **nltk**: faz a tokenização, o download dos recursos linguísticos e o uso de stopwords em português.
* **openpyxl**: permite ao pandas ler arquivos `.xlsx`.
* **pyspellchecker**: corrige palavras antes da contagem e da geração da nuvem.
* **wordcloud**: cria a nuvem de palavras a partir do texto tratado.
* **matplotlib**: exibe e salva a imagem gerada pela nuvem de palavras.

### Arquivo de dados

O projeto espera um arquivo chamado `dados.xlsx` na raiz do repositório, com uma coluna de respostas textuais para análise. No script principal, a coluna precisa ser definida antes da leitura, substituindo `NOME_COLUNA` pelo nome real da coluna da planilha.


> Conhecer outras bibliotecas: [TextBlob](https://www.alura.com.br/artigos/textblob-alternativa-para-processamento-linguagem-natural?srsltid=AfmBOopeER9hGDBIQtzVUqTgBsW7nQuU_nFvBH7Z2cJdtoSAww2BkrIn)

## Passo a passo
Primeiro para evitar o erro de executar o código usando uma versão ou ambiente do Python diferente daquele onde instalou o Pandas, é interessante isolar o projeto de PLN criando ambiente virtual.

no terminal, execute:
```bash
python3 -m venv .venv # para criar o ambiente virtual na pasta do projeto
source .venv/bin/activate # para  ativar o ambiente virtual
```
Em seguida, instale as seguintes bibliotecas
```bash
pip install pandas
pip install nltk
pip install openpyxl # para poder ler arquivos xlsx
pip install pyspellchecker  # para corrigir os textos antes de analisar
pip install matplotlib wordcloud
```

Se precisar desinstalar um pacote em algum momento, digite no terminal, por exemplo
```bash
pip uninstall spellchecker pyspellchecker -y // o -y confirma da desinstalação
```
## Explicação do código base

```python
import pandas as pd 
import nltk 
from collections import Counter

# Baixa os recursos do NLTK usados na análise textual e na remoção de palavras comuns
nltk.download('punkt_tab') 
nltk.download('stopwords')

# Carrega a planilha com as respostas do formulário ou questionário
# O arquivo precisa existir na raiz do projeto

df = pd.read_excel("dados.xlsx") 

respostas = df[NOME_COLUNA].dropna().astype(str).tolist() # Remove valores vazios, converte as respostas para texto e monta uma lista

# Junta todas as respostas em um único texto para facilitar a análise
texto = " ".join(respostas)

# Separa o texto em sentenças no idioma português
frasesChaves = nltk.sent_tokenize(texto, language='portuguese')

# Divide o texto em palavras e mantém apenas as que têm mais de 5 caracteres
categorias = [
    frase.strip()
    for frase in texto.split()
    if len(frase.strip()) > 5 
]

# Conta quantas vezes cada palavra aparece no conjunto processado
frequencia = Counter(categorias)

# Exibe as 20 ocorrências mais frequentes
print(frequencia.most_common(20))
```

## Nuvem de Palavras
O código lê o arquivo `dados.xlsx` e, a partir dele, cria uma nuvem de palavras com os termos mais utilizados.

Antes de rodar a nuvem de palavras, é necessário instalar a seguinte biblioteca:
```bash
pip install nltk wordcloud matplotlib
```

```python
import pandas as pd 
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from spellchecker import SpellChecker
import re
import matplotlib
matplotlib.use('Agg')  # Define o backend do matplotlib para salvar imagens sem abrir janela gráfica

# Baixa os recursos necessários do NLTK: tokenizador, tokenizador por abas e stopwords
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Inicializa o corretor ortográfico em português
corretor = SpellChecker(language='pt')

# Carrega as stopwords em português (palavras muito comuns que não agregam significado, ex: "de", "a", "o")
stopwordsPortugues = set(stopwords.words('portuguese'))

# Adiciona palavras extras que também devem ser ignoradas na nuvem
palavrasExtras = {'pra', 'pro', 'tudo', 'nada', 'fazer', 'ter', 'ser', 'pode', 'sobre'}
stopwordsPortugues.update(palavrasExtras)

# Lê o arquivo Excel e armazena em um DataFrame
df = pd.read_excel("dados.xlsx")

# Extrai os valores da coluna, remove células vazias e converte tudo para string, gerando uma lista
respostas = df[NOME_COLUNA].dropna().astype(str).tolist()

def corrigeTexto(texto):
    # Extrai todas as palavras do texto em letras minúsculas, ignorando pontuação
    palavras = re.findall(r'\b\w+\b', texto.lower())
    palavras_corrigidas = []
    
    for palavra in palavras:
        # Tenta encontrar a correção ortográfica para a palavra
        correcao = corretor.correction(palavra)
        # Usa a correção se existir, caso contrário mantém a palavra original
        palavras_corrigidas.append(correcao if correcao else palavra)
        
    # Junta todas as palavras corrigidas de volta em um único texto
    return " ".join(palavras_corrigidas)

# Aplica a correção ortográfica em cada resposta da lista
respostasCorrigidas = [corrigeTexto(res) for res in respostas]

# Une todas as respostas corrigidas em um único texto contínuo
texto = " ".join(respostasCorrigidas)

# Divide o texto em tokens (palavras individuais) já em letras minúsculas
palavras = word_tokenize(texto.lower())

# Filtra apenas palavras alfanuméricas que não estejam na lista de stopwords
palavrasFiltradas = [p for p in palavras if p.isalnum() and p not in stopwordsPortugues]

# Junta as palavras filtradas em um texto limpo, pronto para gerar a nuvem
textoLimpo = " ".join(palavrasFiltradas)

# Configura e gera a nuvem de palavras com as definições visuais
nuvemPalavras = WordCloud(
    width=1000,       # Largura da imagem em pixels
    height=500,       # Altura da imagem em pixels
    background_color='black',  # Cor de fundo
    colormap='OrRd_r',         # Paleta de cores (laranja-vermelho invertido)
    max_words=100,             # Número máximo de palavras exibidas
    min_font_size=10,          # Tamanho mínimo da fonte
    contour_width=2,           # Espessura do contorno das palavras
    margin=10,                 # Margem entre as palavras
).generate(textoLimpo)         # Gera a nuvem a partir do texto limpo

# Cria a figura do matplotlib com o tamanho definido em polegadas
plt.figure(figsize=(12, 6))

# Exibe a nuvem de palavras com interpolação suave
plt.imshow(nuvemPalavras, interpolation='bilinear')

# Remove os eixos (x e y) da imagem para ficar apenas a nuvem
plt.axis('off')

# Ajusta o layout para remover espaços em branco ao redor
plt.tight_layout(pad=0)

# Salva a imagem como PNG com alta resolução e sem bordas extras
plt.savefig('nuvemDePalavras.png', dpi=300, bbox_inches='tight')

# Fecha a figura para liberar memória
plt.close()

print("salvou aqui.")
```