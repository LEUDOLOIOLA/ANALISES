"""
AULA 4: Seleção e Indexação de Dados
=====================================

Objetivo: Aprender as diferentes formas de selecionar e acessar dados
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("AULA 4: SELEÇÃO E INDEXAÇÃO DE DADOS")
print("=" * 60)

# Criando um DataFrame de exemplo
print("\n1. CRIANDO DATAFRAME DE EXEMPLO")
print("-" * 60)
dados = {
    'Nome': ['Ana', 'Bruno', 'Carla', 'Diego', 'Elena', 'Felipe'],
    'Idade': [25, 30, 28, 35, 27, 32],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre', 'Salvador'],
    'Profissão': ['Engenheira', 'Médico', 'Professora', 'Advogado', 'Designer', 'Programador'],
    'Salário': [5000, 8000, 4500, 7000, 5500, 6000],
    'Anos_Exp': [3, 8, 5, 10, 4, 7]
}
df = pd.DataFrame(dados)
print(df)

print("\n2. SELECIONANDO COLUNAS")
print("-" * 60)

# Uma única coluna (retorna Series)
print("Uma coluna (retorna Series):")
print(df['Nome'])
print(f"Tipo: {type(df['Nome'])}")

# Uma coluna (retorna DataFrame)
print("\nUma coluna (retorna DataFrame):")
print(df[['Nome']])
print(f"Tipo: {type(df[['Nome']])}")

# Múltiplas colunas
print("\nMúltiplas colunas:")
print(df[['Nome', 'Profissão', 'Salário']])

print("\n3. USANDO .loc[] - SELEÇÃO POR LABEL")
print("-" * 60)
# .loc[linhas, colunas] - usa labels/nomes

# Uma linha específica
print("Linha 0:")
print(df.loc[0])

# Múltiplas linhas
print("\nLinhas 0 a 2:")
print(df.loc[0:2])  # Note: inclui o índice final!

# Linhas e colunas específicas
print("\nLinhas 0-2, colunas Nome e Idade:")
print(df.loc[0:2, ['Nome', 'Idade']])

# Todas as linhas, algumas colunas
print("\nTodas as linhas, colunas Nome e Salário:")
print(df.loc[:, ['Nome', 'Salário']])

print("\n4. USANDO .iloc[] - SELEÇÃO POR POSIÇÃO")
print("-" * 60)
# .iloc[linhas, colunas] - usa posições numéricas (0-based)

# Uma linha
print("Primeira linha (posição 0):")
print(df.iloc[0])

# Múltiplas linhas
print("\nLinhas 0 a 2 (não inclui 3):")
print(df.iloc[0:3])  # Note: NÃO inclui o índice final!

# Linhas e colunas por posição
print("\nLinhas 0-2, primeiras 3 colunas:")
print(df.iloc[0:3, 0:3])

# Última linha
print("\nÚltima linha:")
print(df.iloc[-1])

# Últimas 2 linhas, últimas 2 colunas
print("\nÚltimas 2 linhas e 2 colunas:")
print(df.iloc[-2:, -2:])

print("\n5. SELEÇÃO COM LISTAS DE POSIÇÕES")
print("-" * 60)

# Linhas específicas
print("Linhas nas posições 0, 2, 4:")
print(df.iloc[[0, 2, 4]])

# Linhas e colunas específicas
print("\nLinhas 0,2 e colunas 0,2,4:")
print(df.iloc[[0, 2], [0, 2, 4]])

print("\n6. DIFERENÇAS ENTRE .loc e .iloc")
print("-" * 60)
print("DataFrame com índice personalizado:")
df_custom = df.set_index('Nome')
print(df_custom)

print("\nUsando .loc['Bruno'] (acessa por nome do índice):")
print(df_custom.loc['Bruno'])

print("\nUsando .iloc[1] (acessa pela posição numérica):")
print(df_custom.iloc[1])

print("\n7. SELECIONANDO CÉLULAS INDIVIDUAIS")
print("-" * 60)

# Usando .at[] (rápido para valor único por label)
valor = df.at[0, 'Nome']
print(f"Nome na linha 0: {valor}")

# Usando .iat[] (rápido para valor único por posição)
valor = df.iat[0, 0]
print(f"Valor na posição [0, 0]: {valor}")

print("\n8. SELEÇÃO POR CONDIÇÕES BOOLEANAS")
print("-" * 60)

# Pessoas com mais de 28 anos
print("Pessoas com mais de 28 anos:")
mascara = df['Idade'] > 28
print(df[mascara])

# Ou de forma mais direta:
print("\nSalários acima de 6000:")
print(df[df['Salário'] > 6000])

# Múltiplas condições (E)
print("\nIdade > 28 E Salário > 6000:")
print(df[(df['Idade'] > 28) & (df['Salário'] > 6000)])

# Múltiplas condições (OU)
print("\nIdade < 27 OU Salário > 7000:")
print(df[(df['Idade'] < 27) | (df['Salário'] > 7000)])

print("\n9. MÉTODO .query()")
print("-" * 60)
# Forma alternativa de filtrar usando strings

print("Pessoas com idade entre 28 e 32:")
print(df.query('28 <= Idade <= 32'))

print("\nProgramadores ou Designers:")
print(df.query('Profissão == "Programador" or Profissão == "Designer"'))

print("\n10. SELEÇÃO COM .isin()")
print("-" * 60)

cidades_sudeste = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
print(f"Pessoas em cidades do Sudeste {cidades_sudeste}:")
print(df[df['Cidade'].isin(cidades_sudeste)])

profissoes_tech = ['Programador', 'Designer', 'Engenheira']
print(f"\nProfissões de tecnologia {profissoes_tech}:")
print(df[df['Profissão'].isin(profissoes_tech)])

print("\n11. SELEÇÃO COM .between()")
print("-" * 60)

print("Salários entre 5000 e 7000:")
print(df[df['Salário'].between(5000, 7000)])

print("\n12. COMBINANDO SELEÇÕES")
print("-" * 60)

# Filtrar e selecionar colunas específicas
print("Nome e Salário de pessoas com mais de 5 anos de experiência:")
resultado = df.loc[df['Anos_Exp'] > 5, ['Nome', 'Salário', 'Anos_Exp']]
print(resultado)

print("\n" + "=" * 60)
print("EXERCÍCIO PRÁTICO:")
print("=" * 60)
print("""
Usando o DataFrame criado:
1. Selecione apenas Nome e Profissão das 3 primeiras pessoas
2. Encontre todas as pessoas com salário entre 5000 e 6500
3. Mostre Nome, Cidade e Salário das pessoas que moram em 
   São Paulo ou Rio de Janeiro e têm mais de 6 anos de experiência
4. Qual é o salário da pessoa na posição 4?
""")

# Solução do exercício:
print("\nSOLUÇÃO:")
print("-" * 60)

print("1. Nome e Profissão das 3 primeiras pessoas:")
print(df.loc[0:2, ['Nome', 'Profissão']])
# ou: df.iloc[0:3, [0, 3]]

print("\n2. Pessoas com salário entre 5000 e 6500:")
print(df[df['Salário'].between(5000, 6500)])

print("\n3. SP ou RJ com mais de 6 anos de experiência:")
filtro_cidades = df['Cidade'].isin(['São Paulo', 'Rio de Janeiro'])
filtro_exp = df['Anos_Exp'] > 6
resultado = df[filtro_cidades & filtro_exp][['Nome', 'Cidade', 'Salário']]
print(resultado)

print("\n4. Salário da pessoa na posição 4:")
print(f"R$ {df.iloc[4]['Salário']}")
# ou: df.iat[4, 4]

print("\n" + "=" * 60)
print("RESUMO DOS MÉTODOS:")
print("=" * 60)
print("""
• df['coluna']          → Seleciona uma coluna (Series)
• df[['col1', 'col2']]  → Seleciona múltiplas colunas (DataFrame)
• df.loc[linha, coluna] → Seleção por labels
• df.iloc[pos, pos]     → Seleção por posições numéricas
• df[condição]          → Seleção por condição booleana
• df.query('expressão') → Seleção por expressão string
• df.at[linha, coluna]  → Acesso rápido a valor único (label)
• df.iat[pos, pos]      → Acesso rápido a valor único (posição)
""")

print("\n" + "=" * 60)
print("FIM DA AULA 4")
print("=" * 60)
