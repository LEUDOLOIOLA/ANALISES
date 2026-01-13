"""
AULA 1: Introdução ao Pandas e Series
======================================

Objetivo: Aprender o básico sobre a biblioteca Pandas e o objeto Series
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("AULA 1: INTRODUÇÃO AO PANDAS E SERIES")
print("=" * 60)

# O que é Pandas?
# Pandas é uma biblioteca Python para análise e manipulação de dados
# Possui duas estruturas principais: Series e DataFrame

print("\n1. O QUE É UMA SERIES?")
print("-" * 60)
# Uma Series é como uma coluna de dados com índices
# É um array unidimensional com labels (rótulos)

# Criando uma Series a partir de uma lista
numeros = pd.Series([10, 20, 30, 40, 50])
print("Series a partir de lista:")
print(numeros)

print("\n2. SERIES COM ÍNDICES PERSONALIZADOS")
print("-" * 60)
# Podemos criar Series com índices personalizados
notas = pd.Series([8.5, 9.0, 7.5, 8.0], index=['João', 'Maria', 'Pedro', 'Ana'])
print("Notas dos alunos:")
print(notas)

print("\n3. CRIANDO SERIES A PARTIR DE DICIONÁRIO")
print("-" * 60)
# Um dicionário é facilmente convertido em Series
dados_dict = {'Python': 95, 'Java': 80, 'JavaScript': 85, 'C++': 75}
linguagens = pd.Series(dados_dict)
print("Popularidade de linguagens:")
print(linguagens)

print("\n4. ACESSANDO ELEMENTOS DA SERIES")
print("-" * 60)
print(f"Nota da Maria: {notas['Maria']}")
print(f"Primeira nota: {notas.iloc[0]}")  # iloc usa posição numérica
print(f"Últimas 2 notas:\n{notas.tail(2)}")

print("\n5. OPERAÇÕES BÁSICAS COM SERIES")
print("-" * 60)
print(f"Média das notas: {notas.mean():.2f}")
print(f"Maior nota: {notas.max()}")
print(f"Menor nota: {notas.min()}")
print(f"Soma das notas: {notas.sum()}")

print("\n6. OPERAÇÕES MATEMÁTICAS")
print("-" * 60)
# Podemos fazer operações em todos os elementos de uma vez
print("Notas multiplicadas por 10:")
print(notas * 10)

print("\nNotas com bônus de 0.5 pontos:")
print(notas + 0.5)

print("\n7. VERIFICANDO INFORMAÇÕES DA SERIES")
print("-" * 60)
print(f"Tipo de dados: {notas.dtype}")
print(f"Tamanho: {notas.size}")
print(f"Forma: {notas.shape}")
print(f"Índices: {list(notas.index)}")
print(f"Valores: {list(notas.values)}")

print("\n" + "=" * 60)
print("EXERCÍCIO PRÁTICO:")
print("=" * 60)
print("""
Crie uma Series com os seguintes dados:
- Temperaturas da semana: Seg=25, Ter=28, Qua=27, Qui=26, Sex=29, Sab=30, Dom=28
- Calcule a temperatura média
- Encontre o dia mais quente
- Mostre as temperaturas acima de 27 graus
""")

# Solução do exercício:
print("\nSOLUÇÃO:")
print("-" * 60)
temperaturas = pd.Series({
    'Segunda': 25,
    'Terça': 28,
    'Quarta': 27,
    'Quinta': 26,
    'Sexta': 29,
    'Sábado': 30,
    'Domingo': 28
})

print("Temperaturas da semana:")
print(temperaturas)
print(f"\nTemperatura média: {temperaturas.mean():.1f}°C")
print(f"Dia mais quente: {temperaturas.idxmax()} com {temperaturas.max()}°C")
print("\nDias com temperatura acima de 27°C:")
print(temperaturas[temperaturas > 27])

print("\n" + "=" * 60)
print("FIM DA AULA 1")
print("=" * 60)
