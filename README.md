# Análise de dados: Filtro de palavras chaves com PLN
O código análisa um conjunto de dados e trás as frases/palavras mais frequentes

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
```

## Explicação de termos

* **Tokenização** é o processo de dividir um texto em unidades menores, conhecidas como tokens. 
* **Stopwords** são palavras comuns que não agregam muito significado ao texto, como artigos, preposições e pronomes.
* **Stemming** é o processo de reduzir uma palavra à sua forma base ou radical. Isso ajuda a lidar com variações de palavras e reduzir a dimensionalidade dos dados.

Link para estudos: https://medium.com/@dheiver.santos_10420/t%C3%ADtulo-introdu%C3%A7%C3%A3o-ao-processamento-de-linguagem-natural-pln-com-python-e-a-biblioteca-nltk-a6df2f06d395

## Explicação do código

```python
import pandas as pd 
import nltk 
from collections import Counter

# Baixar Modelo de tokenização treinado não supervisionado usado para dividir textos em sentenças individuais
nltk.download('punkt_tab') 

# Leitura de um arquivo excel 
df = pd.read_excel("dados.xlsx") 
# Atribui os dados da coluna "O que poderia ser melhorado na organização do trabalho ou na distribuição das atividades?", removendo os dados nulos (dropna), converte dados pra string (astype(str)) e transforma a série em uma lista (tolist).
respostas = df['O que poderia ser melhorado na organização do trabalho ou na distribuição das atividades?'].dropna().astype(str).tolist()

texto = " ".join(respostas)

frasesChaves = nltk.sent_tokenize(texto, language='portuguese')

categorias = [
    frase.strip()
    for frase in texto.split()
    if len(frase.strip()) > 5 
]

# Atribui a contagem da frequência dos itens a variável frequência
frequencia = Counter(categorias)

# Mostra os 20 mais frequentes
print(frequencia.most_common(20))
```