"""
AULA 10: Visualização Básica de Dados com Pandas
=================================================

Objetivo: Aprender a criar visualizações básicas usando Pandas e Matplotlib
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("=" * 60)
print("AULA 10: VISUALIZAÇÃO BÁSICA DE DADOS")
print("=" * 60)

# Configurando estilo dos gráficos
plt.style.use('default')

# Criando dataset de exemplo
print("\n1. CRIANDO DATASET DE EXEMPLO")
print("-" * 60)
np.random.seed(42)
dados = {
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    'Vendas': [150, 170, 165, 180, 195, 210, 205, 220, 215, 230, 240, 250],
    'Custos': [100, 110, 105, 115, 120, 130, 125, 135, 130, 140, 145, 150],
    'Lucro': [50, 60, 60, 65, 75, 80, 80, 85, 85, 90, 95, 100]
}
df = pd.DataFrame(dados)
print(df)

print("\n2. GRÁFICO DE LINHAS - plot()")
print("-" * 60)
print("Criando gráfico de linha simples...")

# Gráfico de linha básico
df.plot(x='Mês', y='Vendas', kind='line', figsize=(10, 6))
plt.title('Vendas Mensais', fontsize=14, fontweight='bold')
plt.xlabel('Mês')
plt.ylabel('Vendas (milhares R$)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('grafico_linha.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Gráfico salvo como 'grafico_linha.png'")

print("\n3. MÚLTIPLAS LINHAS NO MESMO GRÁFICO")
print("-" * 60)

# Plotar várias colunas
df.plot(x='Mês', y=['Vendas', 'Custos', 'Lucro'], kind='line', figsize=(10, 6))
plt.title('Desempenho Financeiro Mensal', fontsize=14, fontweight='bold')
plt.xlabel('Mês')
plt.ylabel('Valores (milhares R$)')
plt.legend(title='Indicadores', loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('grafico_multiplas_linhas.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Gráfico salvo como 'grafico_multiplas_linhas.png'")

print("\n4. GRÁFICO DE BARRAS - bar()")
print("-" * 60)

# Gráfico de barras
df_trimestre = pd.DataFrame({
    'Trimestre': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Vendas': [485, 585, 640, 720]
})

df_trimestre.plot(x='Trimestre', y='Vendas', kind='bar', figsize=(10, 6), color='steelblue')
plt.title('Vendas por Trimestre', fontsize=14, fontweight='bold')
plt.xlabel('Trimestre')
plt.ylabel('Vendas (milhares R$)')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('grafico_barras.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Gráfico salvo como 'grafico_barras.png'")

print("\n5. GRÁFICO DE BARRAS HORIZONTAIS - barh()")
print("-" * 60)

# Dados de produtos
produtos = pd.DataFrame({
    'Produto': ['Notebook', 'Monitor', 'Teclado', 'Mouse', 'Webcam'],
    'Unidades_Vendidas': [45, 78, 120, 156, 89]
})

produtos.plot(x='Produto', y='Unidades_Vendidas', kind='barh', figsize=(10, 6), color='coral')
plt.title('Produtos Mais Vendidos', fontsize=14, fontweight='bold')
plt.xlabel('Unidades Vendidas')
plt.ylabel('Produto')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('grafico_barras_horizontal.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Gráfico salvo como 'grafico_barras_horizontal.png'")

print("\n6. GRÁFICO DE BARRAS AGRUPADAS")
print("-" * 60)

# Comparativo de vendas
vendas_comparativo = pd.DataFrame({
    'Categoria': ['Eletrônicos', 'Periféricos', 'Acessórios'],
    '2023': [350, 280, 190],
    '2024': [420, 310, 240]
})

vendas_comparativo.plot(
    x='Categoria', 
    y=['2023', '2024'], 
    kind='bar', 
    figsize=(10, 6),
    color=['lightblue', 'navy']
)
plt.title('Comparativo de Vendas: 2023 vs 2024', fontsize=14, fontweight='bold')
plt.xlabel('Categoria')
plt.ylabel('Vendas (milhares R$)')
plt.legend(title='Ano')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('grafico_barras_agrupadas.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Gráfico salvo como 'grafico_barras_agrupadas.png'")

print("\n7. GRÁFICO DE PIZZA - pie()")
print("-" * 60)

# Distribuição de vendas por região
regioes = pd.DataFrame({
    'Região': ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul'],
    'Vendas': [150, 200, 180, 450, 220]
})

regioes.set_index('Região')['Vendas'].plot(
    kind='pie',
    figsize=(8, 8),
    autopct='%1.1f%%',
    startangle=90,
    colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
)
plt.title('Distribuição de Vendas por Região', fontsize=14, fontweight='bold', pad=20)
plt.ylabel('')  # Remove o label do eixo Y
plt.tight_layout()
plt.savefig('grafico_pizza.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Gráfico salvo como 'grafico_pizza.png'")

print("\n8. HISTOGRAMA - hist()")
print("-" * 60)

# Distribuição de idades
np.random.seed(42)
idades = pd.DataFrame({
    'Idade': np.random.normal(35, 10, 200).astype(int)
})

idades['Idade'].plot(
    kind='hist',
    bins=15,
    figsize=(10, 6),
    color='skyblue',
    edgecolor='black'
)
plt.title('Distribuição de Idades dos Clientes', fontsize=14, fontweight='bold')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('histograma.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Gráfico salvo como 'histograma.png'")

print("\n9. GRÁFICO DE DISPERSÃO - scatter()")
print("-" * 60)

# Relação entre investimento e vendas
marketing = pd.DataFrame({
    'Investimento_Marketing': [10, 15, 20, 25, 30, 35, 40, 45, 50],
    'Vendas': [100, 130, 155, 180, 200, 230, 250, 280, 300]
})

marketing.plot(
    x='Investimento_Marketing',
    y='Vendas',
    kind='scatter',
    figsize=(10, 6),
    color='purple',
    s=100,
    alpha=0.6
)
plt.title('Relação: Investimento em Marketing vs Vendas', fontsize=14, fontweight='bold')
plt.xlabel('Investimento em Marketing (milhares R$)')
plt.ylabel('Vendas (milhares R$)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('grafico_dispersao.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Gráfico salvo como 'grafico_dispersao.png'")

print("\n10. BOX PLOT - box()")
print("-" * 60)

# Distribuição de vendas por categoria
vendas_categoria = pd.DataFrame({
    'Eletrônicos': np.random.normal(200, 30, 50),
    'Periféricos': np.random.normal(150, 25, 50),
    'Acessórios': np.random.normal(100, 20, 50)
})

vendas_categoria.plot(
    kind='box',
    figsize=(10, 6),
    grid=True
)
plt.title('Distribuição de Vendas por Categoria', fontsize=14, fontweight='bold')
plt.ylabel('Vendas (milhares R$)')
plt.tight_layout()
plt.savefig('boxplot.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Gráfico salvo como 'boxplot.png'")

print("\n11. ÁREA EMPILHADA - area()")
print("-" * 60)

# Evolução de vendas por produto
vendas_produtos = pd.DataFrame({
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    'Produto A': [30, 35, 40, 38, 45, 50],
    'Produto B': [25, 28, 30, 32, 35, 38],
    'Produto C': [20, 22, 25, 28, 30, 32]
})

vendas_produtos.plot(
    x='Mês',
    y=['Produto A', 'Produto B', 'Produto C'],
    kind='area',
    figsize=(10, 6),
    alpha=0.7
)
plt.title('Evolução de Vendas por Produto (Empilhado)', fontsize=14, fontweight='bold')
plt.xlabel('Mês')
plt.ylabel('Vendas (milhares R$)')
plt.legend(title='Produtos', loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('grafico_area.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Gráfico salvo como 'grafico_area.png'")

print("\n12. SUBPLOTS - MÚLTIPLOS GRÁFICOS")
print("-" * 60)

# Criar figura com múltiplos gráficos
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Dashboard de Vendas', fontsize=16, fontweight='bold')

# Gráfico 1: Linha
df.plot(x='Mês', y='Vendas', kind='line', ax=axes[0, 0], color='blue', legend=False)
axes[0, 0].set_title('Vendas Mensais')
axes[0, 0].grid(True, alpha=0.3)

# Gráfico 2: Barras
df.plot(x='Mês', y='Lucro', kind='bar', ax=axes[0, 1], color='green', legend=False)
axes[0, 1].set_title('Lucro Mensal')
axes[0, 1].set_xticklabels(df['Mês'], rotation=45)

# Gráfico 3: Área
df.plot(x='Mês', y=['Vendas', 'Custos'], kind='area', ax=axes[1, 0], alpha=0.5)
axes[1, 0].set_title('Vendas vs Custos')
axes[1, 0].grid(True, alpha=0.3)

# Gráfico 4: Scatter
df.plot(x='Custos', y='Vendas', kind='scatter', ax=axes[1, 1], color='red', s=50)
axes[1, 1].set_title('Relação Custos vs Vendas')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('dashboard.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Dashboard salvo como 'dashboard.png'")

print("\n13. PERSONALIZANDO GRÁFICOS")
print("-" * 60)

# Gráfico altamente personalizado
df_sample = df[['Mês', 'Vendas', 'Lucro']].head(6)

ax = df_sample.plot(
    x='Mês',
    y=['Vendas', 'Lucro'],
    kind='line',
    figsize=(12, 6),
    linewidth=3,
    marker='o',
    markersize=8
)

ax.set_title('Análise de Performance - Primeiro Semestre', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Período', fontsize=12, fontweight='bold')
ax.set_ylabel('Valores (milhares R$)', fontsize=12, fontweight='bold')
ax.legend(fontsize=11, loc='upper left', framealpha=0.9)
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_facecolor('#f9f9f9')

plt.tight_layout()
plt.savefig('grafico_personalizado.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Gráfico personalizado salvo!")

print("\n" + "=" * 60)
print("EXERCÍCIO PRÁTICO:")
print("=" * 60)
print("""
Crie um DataFrame com dados de vendas de 5 produtos diferentes
incluindo: Produto, Quantidade, Preço, Total

Depois crie:
1. Um gráfico de barras com as quantidades vendidas por produto
2. Um gráfico de pizza mostrando a participação de cada produto no total
3. Um gráfico de barras horizontais com o valor total por produto
4. (Bônus) Um dashboard com 2 gráficos diferentes
""")

# Solução do exercício:
print("\nSOLUÇÃO:")
print("-" * 60)

# Criando dados
vendas_produtos = pd.DataFrame({
    'Produto': ['Notebook', 'Monitor', 'Teclado', 'Mouse', 'Webcam'],
    'Quantidade': [25, 40, 85, 120, 60],
    'Preço': [2500, 800, 150, 50, 200]
})
vendas_produtos['Total'] = vendas_produtos['Quantidade'] * vendas_produtos['Preço']

print("Dados de vendas:")
print(vendas_produtos)

# 1. Gráfico de barras - Quantidade
print("\n1. Criando gráfico de barras...")
vendas_produtos.plot(
    x='Produto', 
    y='Quantidade', 
    kind='bar', 
    figsize=(10, 6),
    color='teal',
    legend=False
)
plt.title('Quantidade Vendida por Produto', fontsize=14, fontweight='bold')
plt.xlabel('Produto')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('exercicio_barras.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Salvo como 'exercicio_barras.png'")

# 2. Gráfico de pizza - Participação
print("\n2. Criando gráfico de pizza...")
vendas_produtos.set_index('Produto')['Total'].plot(
    kind='pie',
    figsize=(8, 8),
    autopct='%1.1f%%',
    startangle=90
)
plt.title('Participação no Faturamento Total', fontsize=14, fontweight='bold', pad=20)
plt.ylabel('')
plt.tight_layout()
plt.savefig('exercicio_pizza.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Salvo como 'exercicio_pizza.png'")

# 3. Barras horizontais - Valor total
print("\n3. Criando gráfico de barras horizontais...")
vendas_produtos_sorted = vendas_produtos.sort_values('Total')
vendas_produtos_sorted.plot(
    x='Produto',
    y='Total',
    kind='barh',
    figsize=(10, 6),
    color='orange',
    legend=False
)
plt.title('Faturamento por Produto', fontsize=14, fontweight='bold')
plt.xlabel('Faturamento Total (R$)')
plt.ylabel('Produto')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('exercicio_horizontal.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Salvo como 'exercicio_horizontal.png'")

# 4. Dashboard
print("\n4. Criando dashboard...")
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Dashboard de Vendas de Produtos', fontsize=16, fontweight='bold')

# Subplot 1: Quantidade
vendas_produtos.plot(x='Produto', y='Quantidade', kind='bar', ax=axes[0], color='steelblue', legend=False)
axes[0].set_title('Unidades Vendidas')
axes[0].set_xlabel('Produto')
axes[0].set_ylabel('Quantidade')
axes[0].set_xticklabels(vendas_produtos['Produto'], rotation=45)
axes[0].grid(axis='y', alpha=0.3)

# Subplot 2: Faturamento
vendas_produtos.plot(x='Produto', y='Total', kind='bar', ax=axes[1], color='coral', legend=False)
axes[1].set_title('Faturamento Total')
axes[1].set_xlabel('Produto')
axes[1].set_ylabel('Faturamento (R$)')
axes[1].set_xticklabels(vendas_produtos['Produto'], rotation=45)
axes[1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('exercicio_dashboard.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Dashboard salvo como 'exercicio_dashboard.png'")

print("\n" + "=" * 60)
print("RESUMO DOS TIPOS DE GRÁFICOS:")
print("=" * 60)
print("""
• plot(kind='line')    → Gráfico de linhas (tendências)
• plot(kind='bar')     → Gráfico de barras verticais
• plot(kind='barh')    → Gráfico de barras horizontais
• plot(kind='pie')     → Gráfico de pizza (proporções)
• plot(kind='hist')    → Histograma (distribuições)
• plot(kind='scatter') → Dispersão (correlações)
• plot(kind='box')     → Box plot (quartis)
• plot(kind='area')    → Gráfico de área (evolução empilhada)

Personalização:
• figsize=(largura, altura) → Tamanho da figura
• color                     → Cor do gráfico
• title, xlabel, ylabel     → Títulos e rótulos
• grid()                    → Grade
• legend()                  → Legenda
• tight_layout()            → Ajusta espaçamento
""")

print("\n" + "=" * 60)
print("FIM DA AULA 10")
print("=" * 60)
print("\n🎉 PARABÉNS! Você completou as 10 aulas de Pandas!")
print("Continue praticando e explorando mais recursos da biblioteca!")
