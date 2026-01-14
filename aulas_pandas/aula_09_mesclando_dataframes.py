"""
AULA 9: Mesclando e Juntando DataFrames
========================================

Objetivo: Aprender a combinar múltiplos DataFrames usando merge, join e concat
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("AULA 9: MESCLANDO E JUNTANDO DATAFRAMES")
print("=" * 60)

# Criando DataFrames de exemplo
print("\n1. CRIANDO DATAFRAMES DE EXEMPLO")
print("-" * 60)

# DataFrame de clientes
clientes = pd.DataFrame({
    'ID_Cliente': [1, 2, 3, 4, 5],
    'Nome': ['Ana', 'Bruno', 'Carla', 'Diego', 'Elena'],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre']
})
print("DataFrame de Clientes:")
print(clientes)

# DataFrame de pedidos
pedidos = pd.DataFrame({
    'ID_Pedido': [101, 102, 103, 104, 105],
    'ID_Cliente': [1, 2, 1, 3, 6],  # Note: cliente 6 não existe em clientes
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Webcam'],
    'Valor': [2500, 50, 150, 800, 200]
})
print("\nDataFrame de Pedidos:")
print(pedidos)

print("\n2. MERGE - INNER JOIN (INTERSEÇÃO)")
print("-" * 60)
# Inner join: retorna apenas registros que têm correspondência em AMBOS os DataFrames

resultado = pd.merge(clientes, pedidos, on='ID_Cliente', how='inner')
print("Inner Join (apenas clientes que fizeram pedidos):")
print(resultado)
print(f"Linhas resultantes: {len(resultado)}")

print("\n3. MERGE - LEFT JOIN")
print("-" * 60)
# Left join: retorna TODOS os registros da esquerda, com ou sem correspondência

resultado = pd.merge(clientes, pedidos, on='ID_Cliente', how='left')
print("Left Join (todos os clientes, com ou sem pedidos):")
print(resultado)
print(f"Linhas resultantes: {len(resultado)}")
print("\nNote: Diego e Elena têm NaN pois não fizeram pedidos")

print("\n4. MERGE - RIGHT JOIN")
print("-" * 60)
# Right join: retorna TODOS os registros da direita, com ou sem correspondência

resultado = pd.merge(clientes, pedidos, on='ID_Cliente', how='right')
print("Right Join (todos os pedidos, com ou sem cliente cadastrado):")
print(resultado)
print(f"Linhas resultantes: {len(resultado)}")
print("\nNote: Pedido 105 tem NaN pois cliente 6 não existe")

print("\n5. MERGE - OUTER JOIN (UNIÃO)")
print("-" * 60)
# Outer join: retorna TODOS os registros de ambos os DataFrames

resultado = pd.merge(clientes, pedidos, on='ID_Cliente', how='outer')
print("Outer Join (todos os clientes E todos os pedidos):")
print(resultado)
print(f"Linhas resultantes: {len(resultado)}")

print("\n6. MERGE COM COLUNAS DE NOMES DIFERENTES")
print("-" * 60)

# DataFrames com nomes de colunas diferentes
funcionarios = pd.DataFrame({
    'ID_Func': [1, 2, 3],
    'Nome': ['Ana', 'Bruno', 'Carla'],
    'Cargo': ['Analista', 'Gerente', 'Coordenadora']
})

salarios = pd.DataFrame({
    'ID_Funcionario': [1, 2, 3],
    'Salário': [5000, 8000, 6500]
})

print("Funcionários:")
print(funcionarios)
print("\nSalários:")
print(salarios)

# Especificando as colunas diferentes
resultado = pd.merge(
    funcionarios, 
    salarios, 
    left_on='ID_Func', 
    right_on='ID_Funcionario',
    how='inner'
)
print("\nMerge com colunas de nomes diferentes:")
print(resultado)

print("\n7. MERGE COM MÚLTIPLAS COLUNAS")
print("-" * 60)

# Quando a chave é composta por múltiplas colunas
vendas_2023 = pd.DataFrame({
    'Produto': ['Notebook', 'Mouse', 'Teclado'],
    'Loja': ['Loja A', 'Loja A', 'Loja B'],
    'Vendas_2023': [100, 200, 150]
})

vendas_2024 = pd.DataFrame({
    'Produto': ['Notebook', 'Mouse', 'Monitor'],
    'Loja': ['Loja A', 'Loja A', 'Loja B'],
    'Vendas_2024': [120, 250, 80]
})

print("Vendas 2023:")
print(vendas_2023)
print("\nVendas 2024:")
print(vendas_2024)

resultado = pd.merge(
    vendas_2023, 
    vendas_2024, 
    on=['Produto', 'Loja'],
    how='outer'
)
print("\nComparativo 2023 vs 2024:")
print(resultado)

print("\n8. CONCATENANDO DATAFRAMES - VERTICALMENTE")
print("-" * 60)

# Empilhar DataFrames (adicionar linhas)
vendas_jan = pd.DataFrame({
    'Data': ['2024-01-01', '2024-01-02'],
    'Produto': ['Notebook', 'Mouse'],
    'Valor': [2500, 50]
})

vendas_fev = pd.DataFrame({
    'Data': ['2024-02-01', '2024-02-02'],
    'Produto': ['Teclado', 'Monitor'],
    'Valor': [150, 800]
})

print("Vendas Janeiro:")
print(vendas_jan)
print("\nVendas Fevereiro:")
print(vendas_fev)

# Concatenar verticalmente
resultado = pd.concat([vendas_jan, vendas_fev], ignore_index=True)
print("\nVendas Totais (concat vertical):")
print(resultado)

print("\n9. CONCATENANDO DATAFRAMES - HORIZONTALMENTE")
print("-" * 60)

# Adicionar colunas lado a lado
nomes = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carla']
})

idades = pd.DataFrame({
    'Idade': [25, 30, 28]
})

cidades = pd.DataFrame({
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
})

print("Nomes:", nomes['Nome'].values)
print("Idades:", idades['Idade'].values)
print("Cidades:", cidades['Cidade'].values)

# Concatenar horizontalmente
resultado = pd.concat([nomes, idades, cidades], axis=1)
print("\nDataFrame combinado (concat horizontal):")
print(resultado)

print("\n10. CONCATENANDO COM IDENTIFICAÇÃO DE ORIGEM")
print("-" * 60)

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

# Adicionar chave para identificar origem
resultado = pd.concat([df1, df2], keys=['fonte1', 'fonte2'])
print("\nConcatenado com identificação:")
print(resultado)

print("\n11. JOIN - JUNTANDO POR ÍNDICE")
print("-" * 60)

# DataFrames com índices correspondentes
df_a = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=['X', 'Y', 'Z'])

df_b = pd.DataFrame({
    'C': [7, 8, 9],
    'D': [10, 11, 12]
}, index=['X', 'Y', 'W'])

print("DataFrame A:")
print(df_a)
print("\nDataFrame B:")
print(df_b)

# Join por índice
resultado = df_a.join(df_b, how='inner')
print("\nJoin inner por índice:")
print(resultado)

resultado = df_a.join(df_b, how='outer')
print("\nJoin outer por índice:")
print(resultado)

print("\n12. MERGE COM SUFIXOS")
print("-" * 60)

# Quando há colunas com mesmo nome além da chave
vendedores = pd.DataFrame({
    'ID': [1, 2, 3],
    'Nome': ['Ana', 'Bruno', 'Carla'],
    'Vendas': [100, 150, 120]
})

metas = pd.DataFrame({
    'ID': [1, 2, 3],
    'Nome': ['Ana', 'Bruno', 'Carla'],
    'Vendas': [80, 140, 100]
})

print("Vendedores (Vendas realizadas):")
print(vendedores)
print("\nMetas (Vendas esperadas):")
print(metas)

resultado = pd.merge(
    vendedores, 
    metas, 
    on='ID',
    suffixes=('_Real', '_Meta')
)
print("\nComparativo Real vs Meta:")
print(resultado)

resultado['Atingimento'] = (resultado['Vendas_Real'] / resultado['Vendas_Meta'] * 100).round(1)
print("\nCom percentual de atingimento:")
print(resultado[['Nome_Real', 'Vendas_Real', 'Vendas_Meta', 'Atingimento']])

print("\n13. APPEND (ALTERNATIVA AO CONCAT)")
print("-" * 60)

df_base = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
nova_linha = pd.DataFrame({'A': [5], 'B': [6]})

print("DataFrame base:")
print(df_base)
print("\nNova linha:")
print(nova_linha)

# Append (deprecated, mas ainda usado)
# Melhor usar concat
resultado = pd.concat([df_base, nova_linha], ignore_index=True)
print("\nApós adicionar linha:")
print(resultado)

print("\n" + "=" * 60)
print("EXERCÍCIO PRÁTICO:")
print("=" * 60)
print("""
Você tem 3 DataFrames:

Produtos: ID_Produto, Nome_Produto, Preço
Vendas: ID_Venda, ID_Produto, Quantidade
Categorias: ID_Produto, Categoria

Tarefas:
1. Junte Vendas com Produtos (todos os produtos, mesmo sem vendas)
2. Adicione informações de Categoria
3. Calcule o valor total de cada venda
4. Mostre o total de vendas por categoria
""")

# Solução do exercício:
print("\nSOLUÇÃO:")
print("-" * 60)

# Criando os DataFrames
produtos = pd.DataFrame({
    'ID_Produto': [1, 2, 3, 4, 5],
    'Nome_Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Webcam'],
    'Preço': [2500, 50, 150, 800, 200]
})

vendas = pd.DataFrame({
    'ID_Venda': [101, 102, 103, 104],
    'ID_Produto': [1, 2, 1, 3],
    'Quantidade': [2, 5, 1, 3]
})

categorias = pd.DataFrame({
    'ID_Produto': [1, 2, 3, 4, 5],
    'Categoria': ['Computadores', 'Periféricos', 'Periféricos', 'Monitores', 'Periféricos']
})

print("Produtos:")
print(produtos)
print("\nVendas:")
print(vendas)
print("\nCategorias:")
print(categorias)

# 1. Juntar Vendas com Produtos (left join em produtos)
print("\n1. Vendas com informações dos produtos:")
resultado = pd.merge(produtos, vendas, on='ID_Produto', how='left')
print(resultado)

# 2. Adicionar Categorias
print("\n2. Adicionando categorias:")
resultado = pd.merge(resultado, categorias, on='ID_Produto', how='left')
print(resultado)

# 3. Calcular valor total
print("\n3. Calculando valor total:")
resultado['Valor_Total'] = resultado['Preço'] * resultado['Quantidade'].fillna(0)
print(resultado)

# 4. Total por categoria (apenas vendas realizadas)
print("\n4. Total de vendas por categoria:")
vendas_por_categoria = resultado[resultado['ID_Venda'].notna()].groupby('Categoria')['Valor_Total'].sum()
print(vendas_por_categoria)

print("\n" + "=" * 60)
print("RESUMO DOS TIPOS DE JOIN:")
print("=" * 60)
print("""
MERGE:
• how='inner'  → Apenas registros em comum (interseção)
• how='left'   → Todos da esquerda + correspondentes da direita
• how='right'  → Todos da direita + correspondentes da esquerda
• how='outer'  → Todos de ambos (união)

CONCAT:
• axis=0       → Empilha verticalmente (adiciona linhas)
• axis=1       → Junta horizontalmente (adiciona colunas)
• ignore_index → Recria índice numérico

JOIN:
• Junta por índice (similar ao merge mas usando índices)
""")

print("\n" + "=" * 60)
print("FIM DA AULA 9")
print("=" * 60)
