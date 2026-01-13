"""
AULA 8: Agrupamento e Agregação de Dados
=========================================

Objetivo: Aprender a agrupar dados e calcular estatísticas agregadas
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("AULA 8: AGRUPAMENTO E AGREGAÇÃO DE DADOS")
print("=" * 60)

# Criando DataFrame de vendas
print("\n1. CRIANDO DATASET DE VENDAS")
print("-" * 60)
np.random.seed(42)
dados = {
    'Data': pd.date_range('2024-01-01', periods=20, freq='D'),
    'Vendedor': np.random.choice(['Ana', 'Bruno', 'Carla'], 20),
    'Produto': np.random.choice(['Notebook', 'Mouse', 'Teclado', 'Monitor'], 20),
    'Quantidade': np.random.randint(1, 10, 20),
    'Preço': np.random.choice([50, 150, 800, 2500], 20),
    'Região': np.random.choice(['Norte', 'Sul', 'Sudeste'], 20)
}
df = pd.DataFrame(dados)
df['Total'] = df['Quantidade'] * df['Preço']
print(df)

print("\n2. GROUPBY BÁSICO - AGRUPANDO POR UMA COLUNA")
print("-" * 60)

# Agrupar por vendedor
print("Agrupando por Vendedor:")
grupos_vendedor = df.groupby('Vendedor')
print(f"Número de grupos: {len(grupos_vendedor)}")
print(f"Grupos: {list(grupos_vendedor.groups.keys())}")

# Ver tamanho de cada grupo
print("\nTamanho de cada grupo:")
print(grupos_vendedor.size())

print("\n3. AGREGAÇÕES SIMPLES")
print("-" * 60)

# Soma por vendedor
print("Total de vendas por vendedor:")
print(df.groupby('Vendedor')['Total'].sum())

# Média por vendedor
print("\nMédia de vendas por vendedor:")
print(df.groupby('Vendedor')['Total'].mean())

# Contagem
print("\nQuantidade de vendas por vendedor:")
print(df.groupby('Vendedor')['Total'].count())

print("\n4. MÚLTIPLAS AGREGAÇÕES COM .agg()")
print("-" * 60)

# Várias estatísticas ao mesmo tempo
print("Estatísticas de vendas por vendedor:")
resultado = df.groupby('Vendedor')['Total'].agg(['sum', 'mean', 'count', 'min', 'max'])
print(resultado)

# Renomear colunas do resultado
print("\nCom nomes personalizados:")
resultado = df.groupby('Vendedor')['Total'].agg([
    ('Total', 'sum'),
    ('Média', 'mean'),
    ('Vendas', 'count'),
    ('Mínimo', 'min'),
    ('Máximo', 'max')
])
print(resultado)

print("\n5. AGREGAÇÕES DIFERENTES POR COLUNA")
print("-" * 60)

# Diferentes funções para diferentes colunas
print("Agregações personalizadas por coluna:")
resultado = df.groupby('Vendedor').agg({
    'Total': ['sum', 'mean'],
    'Quantidade': 'sum',
    'Produto': 'count'
})
print(resultado)

print("\n6. AGRUPANDO POR MÚLTIPLAS COLUNAS")
print("-" * 60)

# Agrupar por vendedor E produto
print("Total de vendas por Vendedor e Produto:")
resultado = df.groupby(['Vendedor', 'Produto'])['Total'].sum()
print(resultado)

# Com múltiplas agregações
print("\nCom múltiplas estatísticas:")
resultado = df.groupby(['Vendedor', 'Produto']).agg({
    'Total': 'sum',
    'Quantidade': 'sum'
})
print(resultado)

print("\n7. RESET_INDEX() - TRANSFORMAR ÍNDICE EM COLUNAS")
print("-" * 60)

# Resultado com índice
resultado_com_indice = df.groupby('Vendedor')['Total'].sum()
print("Com índice:")
print(resultado_com_indice)

# Resetando o índice
resultado_sem_indice = df.groupby('Vendedor')['Total'].sum().reset_index()
print("\nApós reset_index():")
print(resultado_sem_indice)

print("\n8. AGRUPANDO POR DATAS")
print("-" * 60)

# Extrair componentes da data
df['Dia_Semana'] = df['Data'].dt.day_name()
df['Mes'] = df['Data'].dt.month

print("Vendas por dia da semana:")
vendas_por_dia = df.groupby('Dia_Semana')['Total'].sum().sort_values(ascending=False)
print(vendas_por_dia)

print("\n9. FILTRANDO GRUPOS")
print("-" * 60)

# Filtrar grupos com base em condição
print("Vendedores com total de vendas > 10000:")
grupos = df.groupby('Vendedor')['Total'].sum()
vendedores_top = grupos[grupos > 10000]
print(vendedores_top)

# Usando filter() para filtrar grupos inteiros
print("\nMostrando apenas vendas de vendedores com total > 10000:")
resultado = df.groupby('Vendedor').filter(lambda x: x['Total'].sum() > 10000)
print(resultado[['Vendedor', 'Total']])

print("\n10. TRANSFORMAÇÕES EM GRUPOS")
print("-" * 60)

# Adicionar média do grupo como nova coluna
df['Media_Vendedor'] = df.groupby('Vendedor')['Total'].transform('mean')
print("Total vs Média do vendedor:")
print(df[['Vendedor', 'Total', 'Media_Vendedor']].head(10))

# Calcular percentual sobre o total do vendedor
df['Percentual_Vendedor'] = (df['Total'] / df.groupby('Vendedor')['Total'].transform('sum') * 100)
print("\nPercentual de cada venda sobre o total do vendedor:")
print(df[['Vendedor', 'Total', 'Percentual_Vendedor']].head(10))

print("\n11. APLICANDO FUNÇÕES PERSONALIZADAS")
print("-" * 60)

# Função personalizada para aplicar no grupo
def amplitude(serie):
    return serie.max() - serie.min()

print("Amplitude de vendas por vendedor:")
resultado = df.groupby('Vendedor')['Total'].agg(amplitude)
print(resultado)

# Múltiplas funções personalizadas
def coef_variacao(serie):
    return serie.std() / serie.mean() if serie.mean() != 0 else 0

resultado = df.groupby('Vendedor')['Total'].agg([
    'mean',
    'std',
    ('amplitude', amplitude),
    ('cv', coef_variacao)
])
print("\nEstatísticas avançadas:")
print(resultado)

print("\n12. PIVOT TABLES")
print("-" * 60)

# Pivot table é outra forma de agrupar e agregar
print("Pivot: Vendedor vs Produto (valores = Total):")
pivot = df.pivot_table(
    values='Total',
    index='Vendedor',
    columns='Produto',
    aggfunc='sum',
    fill_value=0
)
print(pivot)

# Com múltiplas agregações
print("\nPivot com soma e contagem:")
pivot = df.pivot_table(
    values='Total',
    index='Vendedor',
    columns='Produto',
    aggfunc=['sum', 'count'],
    fill_value=0
)
print(pivot)

print("\n13. ESTATÍSTICAS DESCRITIVAS POR GRUPO")
print("-" * 60)

print("Describe por vendedor:")
resultado = df.groupby('Vendedor')['Total'].describe()
print(resultado)

print("\n14. RANKING DENTRO DE GRUPOS")
print("-" * 60)

# Ranking de vendas dentro de cada vendedor
df['Rank_Vendedor'] = df.groupby('Vendedor')['Total'].rank(ascending=False, method='dense')
print("Top 3 vendas de cada vendedor:")
top_vendas = df.sort_values(['Vendedor', 'Rank_Vendedor'])
print(top_vendas[top_vendas['Rank_Vendedor'] <= 3][['Vendedor', 'Produto', 'Total', 'Rank_Vendedor']])

print("\n" + "=" * 60)
print("EXERCÍCIO PRÁTICO:")
print("=" * 60)
print("""
Usando o DataFrame de vendas:
1. Qual vendedor teve o maior total de vendas?
2. Qual produto foi mais vendido em quantidade?
3. Qual a média de preço por produto?
4. Mostre o total de vendas por Região e Produto
5. Qual região teve a maior média de vendas?
6. Adicione uma coluna com o percentual de cada venda sobre o total da região
""")

# Solução do exercício:
print("\nSOLUÇÃO:")
print("-" * 60)

print("1. Vendedor com maior total de vendas:")
total_por_vendedor = df.groupby('Vendedor')['Total'].sum().sort_values(ascending=False)
print(total_por_vendedor)
print(f"   Vencedor: {total_por_vendedor.idxmax()} com R$ {total_por_vendedor.max():,.2f}")

print("\n2. Produto mais vendido em quantidade:")
quantidade_por_produto = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)
print(quantidade_por_produto)
print(f"   Vencedor: {quantidade_por_produto.idxmax()} com {quantidade_por_produto.max()} unidades")

print("\n3. Média de preço por produto:")
media_preco = df.groupby('Produto')['Preço'].mean().sort_values(ascending=False)
print(media_preco)

print("\n4. Total de vendas por Região e Produto:")
vendas_regiao_produto = df.groupby(['Região', 'Produto'])['Total'].sum().reset_index()
print(vendas_regiao_produto)

print("\n5. Região com maior média de vendas:")
media_por_regiao = df.groupby('Região')['Total'].mean().sort_values(ascending=False)
print(media_por_regiao)
print(f"   Vencedor: {media_por_regiao.idxmax()} com R$ {media_por_regiao.max():,.2f}")

print("\n6. Percentual sobre total da região:")
df['Percentual_Regiao'] = (df['Total'] / df.groupby('Região')['Total'].transform('sum') * 100)
print(df[['Região', 'Vendedor', 'Total', 'Percentual_Regiao']].head(10))

print("\n" + "=" * 60)
print("RESUMO DE MÉTODOS:")
print("=" * 60)
print("""
• .groupby('col')               → Cria grupos
• .agg(['func1', 'func2'])      → Múltiplas agregações
• .agg({'col1': 'func'})        → Agregações por coluna
• .sum(), .mean(), .count()     → Agregações básicas
• .size()                       → Tamanho dos grupos
• .filter(lambda x: condição)   → Filtra grupos
• .transform('func')            → Aplica função mantendo shape
• .apply(func)                  → Aplica função customizada
• .pivot_table()                → Tabela pivô
• .reset_index()                → Índice vira coluna
""")

print("\n" + "=" * 60)
print("FIM DA AULA 8")
print("=" * 60)
