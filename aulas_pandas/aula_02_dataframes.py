"""
AULA 2: DataFrames - Criando e Operações Básicas
=================================================

Objetivo: Aprender a criar e manipular DataFrames em Pandas
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("AULA 2: DATAFRAMES - CRIANDO E OPERAÇÕES BÁSICAS")
print("=" * 60)

# O que é um DataFrame?
# É uma estrutura bidimensional (como uma tabela ou planilha Excel)
# Possui linhas e colunas com labels

print("\n1. CRIANDO UM DATAFRAME A PARTIR DE DICIONÁRIO")
print("-" * 60)
# A forma mais comum de criar um DataFrame
dados = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'Carlos'],
    'Idade': [25, 30, 35, 28, 32],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre'],
    'Salário': [3000, 4500, 3800, 4200, 5000]
}

df = pd.DataFrame(dados)
print(df)

print("\n2. VISUALIZANDO INFORMAÇÕES DO DATAFRAME")
print("-" * 60)
print(f"Forma (linhas, colunas): {df.shape}")
print(f"Número de linhas: {len(df)}")
print(f"Número de colunas: {len(df.columns)}")
print(f"\nNomes das colunas: {list(df.columns)}")
print(f"\nTipos de dados:\n{df.dtypes}")

print("\n3. PRIMEIRAS E ÚLTIMAS LINHAS")
print("-" * 60)
print("Primeiras 3 linhas:")
print(df.head(3))
print("\nÚltimas 2 linhas:")
print(df.tail(2))

print("\n4. INFORMAÇÕES GERAIS DO DATAFRAME")
print("-" * 60)
print("\nResumo do DataFrame:")
df.info()

print("\n5. ESTATÍSTICAS DESCRITIVAS")
print("-" * 60)
print("\nEstatísticas das colunas numéricas:")
print(df.describe())

print("\n6. ACESSANDO COLUNAS")
print("-" * 60)
# Existem várias formas de acessar colunas
print("Coluna 'Nome' (como Series):")
print(df['Nome'])

print("\nVárias colunas ao mesmo tempo:")
print(df[['Nome', 'Salário']])

print("\n7. ACESSANDO LINHAS")
print("-" * 60)
# iloc: acessa por posição numérica
print("Primeira linha (iloc[0]):")
print(df.iloc[0])

print("\nLinhas 1 a 3 (iloc[1:3]):")
print(df.iloc[1:3])

# loc: acessa por label/índice
print("\nLinha de índice 2 (loc[2]):")
print(df.loc[2])

print("\n8. CRIANDO DATAFRAME COM ÍNDICE PERSONALIZADO")
print("-" * 60)
dados_produtos = {
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor'],
    'Preço': [2500, 50, 150, 800],
    'Estoque': [15, 50, 30, 20]
}
df_produtos = pd.DataFrame(dados_produtos, index=['P001', 'P002', 'P003', 'P004'])
print(df_produtos)

print("\nAcessando produto P002:")
print(df_produtos.loc['P002'])

print("\n9. OPERAÇÕES COM COLUNAS")
print("-" * 60)
print("Salários originais:")
print(df['Salário'])

print("\nSalários com aumento de 10%:")
print(df['Salário'] * 1.10)

print("\nSalário médio:", df['Salário'].mean())
print("Salário máximo:", df['Salário'].max())
print("Salário mínimo:", df['Salário'].min())

print("\n10. CRIANDO DATAFRAME A PARTIR DE LISTA DE LISTAS")
print("-" * 60)
dados_matriz = [
    ['Ana', 'F', 28],
    ['Bruno', 'M', 32],
    ['Carla', 'F', 25],
    ['Diego', 'M', 30]
]
df_matriz = pd.DataFrame(dados_matriz, columns=['Nome', 'Sexo', 'Idade'])
print(df_matriz)

print("\n" + "=" * 60)
print("EXERCÍCIO PRÁTICO:")
print("=" * 60)
print("""
Crie um DataFrame com as seguintes informações de livros:
- Título: 'Python Basics', 'Data Science', 'Machine Learning', 'Web Development'
- Autor: 'João Silva', 'Maria Santos', 'Pedro Costa', 'Ana Lima'
- Ano: 2020, 2019, 2021, 2020
- Páginas: 300, 450, 500, 350

Depois:
1. Mostre as primeiras 2 linhas
2. Calcule a média de páginas
3. Encontre o livro mais antigo
4. Mostre apenas as colunas 'Título' e 'Ano'
""")

# Solução do exercício:
print("\nSOLUÇÃO:")
print("-" * 60)
livros = {
    'Título': ['Python Basics', 'Data Science', 'Machine Learning', 'Web Development'],
    'Autor': ['João Silva', 'Maria Santos', 'Pedro Costa', 'Ana Lima'],
    'Ano': [2020, 2019, 2021, 2020],
    'Páginas': [300, 450, 500, 350]
}
df_livros = pd.DataFrame(livros)

print("DataFrame completo:")
print(df_livros)

print("\n1. Primeiras 2 linhas:")
print(df_livros.head(2))

print(f"\n2. Média de páginas: {df_livros['Páginas'].mean():.0f}")

print(f"\n3. Livro mais antigo (ano {df_livros['Ano'].min()}):")
livro_antigo = df_livros[df_livros['Ano'] == df_livros['Ano'].min()]
print(livro_antigo[['Título', 'Ano']])

print("\n4. Apenas colunas 'Título' e 'Ano':")
print(df_livros[['Título', 'Ano']])

print("\n" + "=" * 60)
print("FIM DA AULA 2")
print("=" * 60)
