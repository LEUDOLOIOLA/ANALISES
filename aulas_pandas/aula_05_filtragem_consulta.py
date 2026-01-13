"""
AULA 5: Filtragem e Consulta de Dados
======================================

Objetivo: Dominar técnicas avançadas de filtragem e consulta de dados
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("AULA 5: FILTRAGEM E CONSULTA DE DADOS")
print("=" * 60)

# Criando um DataFrame mais completo para exemplos
print("\n1. CRIANDO DATASET DE EXEMPLO")
print("-" * 60)
np.random.seed(42)
dados = {
    'ID': range(1, 21),
    'Nome': [f'Cliente_{i}' for i in range(1, 21)],
    'Idade': np.random.randint(20, 60, 20),
    'Cidade': np.random.choice(['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba'], 20),
    'Produto': np.random.choice(['Notebook', 'Tablet', 'Smartphone', 'Monitor'], 20),
    'Valor': np.random.randint(500, 5000, 20),
    'Quantidade': np.random.randint(1, 5, 20),
    'Status': np.random.choice(['Aprovado', 'Pendente', 'Cancelado'], 20)
}
df = pd.DataFrame(dados)
print(df)

print("\n2. FILTRAGEM SIMPLES")
print("-" * 60)

# Filtro por valor exato
print("Compras de Notebook:")
print(df[df['Produto'] == 'Notebook'])

# Filtro por valor diferente
print("\nCompras que NÃO são de Tablet:")
print(df[df['Produto'] != 'Tablet'].head(3))

# Filtros numéricos
print("\nCompras com valor acima de 3000:")
print(df[df['Valor'] > 3000])

print("\n3. FILTRAGEM COM MÚLTIPLAS CONDIÇÕES")
print("-" * 60)

# E lógico (&)
print("Notebooks com valor acima de 2000:")
filtro_e = (df['Produto'] == 'Notebook') & (df['Valor'] > 2000)
print(df[filtro_e])

# OU lógico (|)
print("\nCompras de São Paulo OU Rio de Janeiro:")
filtro_ou = (df['Cidade'] == 'São Paulo') | (df['Cidade'] == 'Rio de Janeiro')
print(df[filtro_ou].head(5))

# NÃO lógico (~)
print("\nCompras que NÃO estão Pendentes:")
filtro_nao = ~(df['Status'] == 'Pendente')
print(df[filtro_nao].head(5))

print("\n4. FILTRAGEM COM MÚLTIPLAS CONDIÇÕES COMPLEXAS")
print("-" * 60)

# Três condições
print("Notebooks OU Tablets, Aprovados, valor > 1500:")
filtro_complexo = (
    (df['Produto'].isin(['Notebook', 'Tablet'])) &
    (df['Status'] == 'Aprovado') &
    (df['Valor'] > 1500)
)
print(df[filtro_complexo])

print("\n5. USANDO .isin() PARA FILTROS MÚLTIPLOS")
print("-" * 60)

# Filtrar por múltiplos valores
cidades_sudeste = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
print(f"Compras em cidades do Sudeste: {cidades_sudeste}")
print(df[df['Cidade'].isin(cidades_sudeste)].head(5))

# Negação com isin()
print("\nCompras NÃO em São Paulo:")
print(df[~df['Cidade'].isin(['São Paulo'])].head(5))

print("\n6. USANDO .between() PARA INTERVALOS")
print("-" * 60)

# Valores em um intervalo
print("Compras com valor entre 1000 e 2500:")
print(df[df['Valor'].between(1000, 2500)])

# Idades entre 25 e 40
print("\nClientes entre 25 e 40 anos:")
print(df[df['Idade'].between(25, 40)].head(5))

print("\n7. FILTRAGEM COM STRINGS")
print("-" * 60)

# Strings que começam com algo
print("Cidades que começam com 'São':")
print(df[df['Cidade'].str.startswith('São')].head(3))

# Strings que contêm algo
print("\nCidades que contêm 'Rio':")
print(df[df['Cidade'].str.contains('Rio')].head(3))

# Strings que terminam com algo
print("\nCidades que terminam com 'Paulo':")
print(df[df['Cidade'].str.endswith('Paulo')].head(3))

print("\n8. USANDO .query() PARA CONSULTAS")
print("-" * 60)

# Sintaxe mais legível para consultas complexas
print("Consulta: Valor > 2000 e Status == 'Aprovado'")
resultado = df.query('Valor > 2000 and Status == "Aprovado"')
print(resultado)

# Usando variáveis na query
valor_minimo = 1500
print(f"\nConsulta com variável: Valor > {valor_minimo}")
resultado = df.query('Valor > @valor_minimo')
print(resultado.head(3))

# Query com múltiplas condições
print("\nNotebook ou Tablet com valor entre 1000 e 3000:")
resultado = df.query('(Produto == "Notebook" or Produto == "Tablet") and 1000 <= Valor <= 3000')
print(resultado)

print("\n9. FILTRANDO COM MÉTODOS DE STRINGS")
print("-" * 60)

# Case insensitive
print("Produtos que contêm 'note' (case insensitive):")
print(df[df['Produto'].str.contains('note', case=False)])

# Múltiplos padrões
print("\nCidades que começam com 'São' ou 'Rio':")
print(df[df['Cidade'].str.startswith(('São', 'Rio'))].head(5))

print("\n10. CONTANDO RESULTADOS DE FILTROS")
print("-" * 60)

print("Quantidade de compras por status:")
for status in df['Status'].unique():
    count = len(df[df['Status'] == status])
    print(f"  {status}: {count}")

print("\nQuantidade de compras aprovadas por produto:")
df_aprovado = df[df['Status'] == 'Aprovado']
print(df_aprovado['Produto'].value_counts())

print("\n11. FILTRAGEM E CÁLCULOS")
print("-" * 60)

# Calcular totais após filtro
df['Total'] = df['Valor'] * df['Quantidade']

print("Total de vendas aprovadas:")
total_aprovado = df[df['Status'] == 'Aprovado']['Total'].sum()
print(f"R$ {total_aprovado:,.2f}")

print("\nMédia de valor por cidade:")
for cidade in df['Cidade'].unique():
    media = df[df['Cidade'] == cidade]['Valor'].mean()
    print(f"  {cidade}: R$ {media:.2f}")

print("\n12. FILTRAGEM COM VALORES NULOS")
print("-" * 60)

# Criando DataFrame com valores nulos para exemplo
df_exemplo = df.copy()
df_exemplo.loc[0:2, 'Status'] = None
df_exemplo.loc[5:7, 'Valor'] = None

print("Linhas com Status nulo:")
print(df_exemplo[df_exemplo['Status'].isnull()])

print("\nLinhas SEM Status nulo:")
print(df_exemplo[df_exemplo['Status'].notnull()].head(3))

print("\n" + "=" * 60)
print("EXERCÍCIO PRÁTICO:")
print("=" * 60)
print("""
Usando o DataFrame criado:
1. Encontre todas as compras de Smartphone OU Monitor com status 'Aprovado'
2. Liste compras de São Paulo com valor acima de 2000
3. Quantas compras canceladas existem?
4. Qual a soma total (Valor × Quantidade) de compras aprovadas?
5. Encontre clientes entre 30 e 45 anos que compraram Notebook
""")

# Solução do exercício:
print("\nSOLUÇÃO:")
print("-" * 60)

print("1. Smartphone OU Monitor com status 'Aprovado':")
solucao1 = df[
    (df['Produto'].isin(['Smartphone', 'Monitor'])) &
    (df['Status'] == 'Aprovado')
]
print(solucao1)
print(f"   Total: {len(solucao1)} compras")

print("\n2. Compras de São Paulo com valor acima de 2000:")
solucao2 = df[
    (df['Cidade'] == 'São Paulo') &
    (df['Valor'] > 2000)
]
print(solucao2)
print(f"   Total: {len(solucao2)} compras")

print("\n3. Quantidade de compras canceladas:")
canceladas = len(df[df['Status'] == 'Cancelado'])
print(f"   {canceladas} compras canceladas")

print("\n4. Soma total de compras aprovadas:")
total = df[df['Status'] == 'Aprovado']['Total'].sum()
print(f"   R$ {total:,.2f}")

print("\n5. Clientes 30-45 anos que compraram Notebook:")
solucao5 = df[
    (df['Idade'].between(30, 45)) &
    (df['Produto'] == 'Notebook')
]
print(solucao5)
print(f"   Total: {len(solucao5)} compras")

print("\n" + "=" * 60)
print("DICAS IMPORTANTES:")
print("=" * 60)
print("""
✓ Use parênteses () em condições múltiplas com &, |, ~
✓ & = E lógico, | = OU lógico, ~ = NÃO lógico
✓ .isin() é mais eficiente que múltiplos ORs
✓ .between() é mais legível para intervalos
✓ .query() pode ser mais legível para consultas complexas
✓ .str.contains() é útil para buscar padrões em texto
""")

print("\n" + "=" * 60)
print("FIM DA AULA 5")
print("=" * 60)
