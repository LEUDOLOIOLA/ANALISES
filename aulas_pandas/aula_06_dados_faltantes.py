"""
AULA 6: Tratamento de Dados Faltantes
======================================

Objetivo: Aprender a identificar e tratar valores faltantes (missing data)
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("AULA 6: TRATAMENTO DE DADOS FALTANTES")
print("=" * 60)

# Criando DataFrame com valores faltantes
print("\n1. CRIANDO DATASET COM VALORES FALTANTES")
print("-" * 60)
dados = {
    'Nome': ['Ana', 'Bruno', None, 'Diego', 'Elena', 'Felipe', None, 'Gabriela'],
    'Idade': [25, 30, 28, None, 27, 32, 29, None],
    'Cidade': ['São Paulo', None, 'Belo Horizonte', 'Curitiba', None, 'Salvador', 'Recife', 'Fortaleza'],
    'Salário': [5000, 8000, None, 7000, 5500, None, 6200, 7500],
    'Departamento': ['TI', 'Vendas', 'TI', None, 'Marketing', 'TI', 'Vendas', None]
}
df = pd.DataFrame(dados)
print(df)

print("\n2. IDENTIFICANDO VALORES FALTANTES")
print("-" * 60)

# isnull() retorna True onde há valores faltantes
print("Identificando valores nulos (isnull()):")
print(df.isnull())

# isna() é sinônimo de isnull()
print("\nSoma de valores nulos por coluna:")
print(df.isnull().sum())

print("\nPorcentagem de valores nulos por coluna:")
porcentagem = (df.isnull().sum() / len(df)) * 100
print(porcentagem)

print("\n3. IDENTIFICANDO LINHAS COM VALORES FALTANTES")
print("-" * 60)

# Linhas que têm algum valor faltante
print("Linhas com ALGUM valor faltante:")
linhas_com_nulos = df[df.isnull().any(axis=1)]
print(linhas_com_nulos)

# Linhas completamente preenchidas
print("\nLinhas SEM valores faltantes:")
linhas_completas = df[df.notnull().all(axis=1)]
print(linhas_completas)

print("\n4. REMOVENDO VALORES FALTANTES - dropna()")
print("-" * 60)

# Remover linhas com QUALQUER valor faltante
print("Original tem", len(df), "linhas")
df_sem_nulos = df.dropna()
print("Após dropna(), tem", len(df_sem_nulos), "linhas")
print(df_sem_nulos)

# Remover linhas onde TODOS os valores são nulos
df_exemplo = pd.DataFrame({
    'A': [1, None, None],
    'B': [4, None, None],
    'C': [7, 8, None]
})
print("\nDataFrame exemplo:")
print(df_exemplo)
print("\nRemovendo linhas onde TODOS são nulos:")
print(df_exemplo.dropna(how='all'))

# Remover linhas com nulos em colunas específicas
print("\nRemovendo linhas com Nome ou Idade nulos:")
df_filtrado = df.dropna(subset=['Nome', 'Idade'])
print(df_filtrado)

print("\n5. REMOVENDO COLUNAS COM VALORES FALTANTES")
print("-" * 60)

# Remover colunas com qualquer valor faltante
print("Original tem", len(df.columns), "colunas")
df_sem_col_nulas = df.dropna(axis=1)
print("Após dropna(axis=1), tem", len(df_sem_col_nulas.columns), "colunas")
print(df_sem_col_nulas)

# Remover colunas com muitos valores faltantes
print("\nRemovendo colunas com mais de 2 valores nulos:")
df_filtrado = df.dropna(axis=1, thresh=len(df)-2)
print(df_filtrado)

print("\n6. PREENCHENDO VALORES FALTANTES - fillna()")
print("-" * 60)

# Preencher com um valor específico
print("Preenchendo nulos com 'Desconhecido':")
df_preenchido = df.fillna('Desconhecido')
print(df_preenchido)

# Preencher cada coluna com um valor diferente
print("\nPreenchendo com valores específicos por coluna:")
valores = {
    'Nome': 'Sem Nome',
    'Idade': 0,
    'Cidade': 'Não Informado',
    'Salário': 0,
    'Departamento': 'Indefinido'
}
df_preenchido = df.fillna(valores)
print(df_preenchido)

print("\n7. PREENCHENDO COM ESTATÍSTICAS")
print("-" * 60)

# Preencher com a média
print("Idade média:", df['Idade'].mean())
df_media = df.copy()
df_media['Idade'] = df_media['Idade'].fillna(df['Idade'].mean())
print("\nIdades após preencher com média:")
print(df_media[['Nome', 'Idade']])

# Preencher com a mediana
print("\nSalário mediano:", df['Salário'].median())
df_mediana = df.copy()
df_mediana['Salário'] = df_mediana['Salário'].fillna(df['Salário'].median())
print("\nSalários após preencher com mediana:")
print(df_mediana[['Nome', 'Salário']])

# Preencher com a moda (valor mais frequente)
print("\nDepartamento mais frequente:", df['Departamento'].mode()[0])
df_moda = df.copy()
df_moda['Departamento'] = df_moda['Departamento'].fillna(df['Departamento'].mode()[0])
print("\nDepartamentos após preencher com moda:")
print(df_moda[['Nome', 'Departamento']])

print("\n8. PREENCHIMENTO FORWARD FILL E BACKWARD FILL")
print("-" * 60)

# Criar série temporal como exemplo
serie_tempo = pd.Series([1, None, None, 4, None, 6, 7, None])
print("Série original:")
print(serie_tempo)

# Forward fill (propaga o último valor válido para frente)
print("\nForward fill (ffill):")
print(serie_tempo.fillna(method='ffill'))

# Backward fill (propaga o próximo valor válido para trás)
print("\nBackward fill (bfill):")
print(serie_tempo.fillna(method='bfill'))

print("\n9. INTERPOLAÇÃO DE VALORES")
print("-" * 60)

# Interpolação linear
print("Série com interpolação linear:")
print(serie_tempo.interpolate())

# Útil para séries numéricas temporais
df_temp = pd.DataFrame({
    'Dia': [1, 2, 3, 4, 5, 6],
    'Temperatura': [20, None, None, 26, None, 30]
})
print("\nTemperaturas originais:")
print(df_temp)

df_temp['Temp_Interpolada'] = df_temp['Temperatura'].interpolate()
print("\nCom interpolação:")
print(df_temp)

print("\n10. SUBSTITUINDO VALORES ESPECÍFICOS")
print("-" * 60)

# Criar DataFrame com valores especiais
df_especial = pd.DataFrame({
    'A': [1, -999, 3, -999, 5],
    'B': ['OK', 'N/A', 'OK', 'N/A', 'OK']
})
print("DataFrame com valores especiais:")
print(df_especial)

# Substituir valores específicos por NaN
print("\nSubstituindo -999 e 'N/A' por NaN:")
df_especial_limpo = df_especial.replace([-999, 'N/A'], np.nan)
print(df_especial_limpo)

# Depois pode preencher
print("\nPreenchendo NaN com 0 e 'Desconhecido':")
df_final = df_especial_limpo.fillna({'A': 0, 'B': 'Desconhecido'})
print(df_final)

print("\n11. ESTRATÉGIAS COMBINADAS")
print("-" * 60)

print("DataFrame original:")
print(df)

# Estratégia combinada
df_tratado = df.copy()

# 1. Preencher nomes com 'Anônimo'
df_tratado['Nome'] = df_tratado['Nome'].fillna('Anônimo')

# 2. Preencher idades com a média
df_tratado['Idade'] = df_tratado['Idade'].fillna(df_tratado['Idade'].mean())

# 3. Preencher cidades com 'Não Informado'
df_tratado['Cidade'] = df_tratado['Cidade'].fillna('Não Informado')

# 4. Preencher salários com a mediana
df_tratado['Salário'] = df_tratado['Salário'].fillna(df_tratado['Salário'].median())

# 5. Preencher departamentos com a moda
df_tratado['Departamento'] = df_tratado['Departamento'].fillna(df_tratado['Departamento'].mode()[0])

print("\nDataFrame após tratamento:")
print(df_tratado)
print("\nVerificando valores nulos restantes:")
print(df_tratado.isnull().sum())

print("\n" + "=" * 60)
print("EXERCÍCIO PRÁTICO:")
print("=" * 60)
print("""
Crie um DataFrame de vendas com valores faltantes:
- 10 linhas
- Colunas: Produto, Quantidade, Preço, Desconto
- Adicione alguns valores nulos
Depois:
1. Mostre quantos valores nulos há em cada coluna
2. Remova linhas onde Produto é nulo
3. Preencha Quantidade nula com 1
4. Preencha Preço nulo com a média dos preços
5. Preencha Desconto nulo com 0
6. Mostre o resultado final sem nulos
""")

# Solução do exercício:
print("\nSOLUÇÃO:")
print("-" * 60)

# Criando dados
vendas = {
    'Produto': ['Notebook', None, 'Mouse', 'Teclado', None, 'Monitor', 'Webcam', 'Fone', None, 'SSD'],
    'Quantidade': [2, 5, None, 3, 1, None, 4, 2, 1, None],
    'Preço': [2500, 50, 80, None, 800, 1200, None, 150, 200, 400],
    'Desconto': [100, None, 0, 20, None, 150, 30, None, 0, 50]
}
df_vendas = pd.DataFrame(vendas)

print("DataFrame original:")
print(df_vendas)

print("\n1. Valores nulos por coluna:")
print(df_vendas.isnull().sum())

print("\n2. Removendo linhas onde Produto é nulo:")
df_vendas = df_vendas.dropna(subset=['Produto'])
print(df_vendas)

print("\n3. Preenchendo Quantidade nula com 1:")
df_vendas['Quantidade'] = df_vendas['Quantidade'].fillna(1)

print("\n4. Preenchendo Preço nulo com a média:")
media_preco = df_vendas['Preço'].mean()
print(f"   Média de preços: R$ {media_preco:.2f}")
df_vendas['Preço'] = df_vendas['Preço'].fillna(media_preco)

print("\n5. Preenchendo Desconto nulo com 0:")
df_vendas['Desconto'] = df_vendas['Desconto'].fillna(0)

print("\n6. Resultado final:")
print(df_vendas)
print("\nVerificação - valores nulos restantes:")
print(df_vendas.isnull().sum())

print("\n" + "=" * 60)
print("RESUMO DE MÉTODOS:")
print("=" * 60)
print("""
• .isnull() ou .isna()     → Identifica valores nulos
• .notnull() ou .notna()   → Identifica valores não-nulos
• .dropna()                → Remove linhas/colunas com nulos
• .fillna(valor)           → Preenche nulos com valor
• .fillna(method='ffill')  → Preenche propagando para frente
• .fillna(method='bfill')  → Preenche propagando para trás
• .interpolate()           → Interpola valores faltantes
• .replace()               → Substitui valores específicos
""")

print("\n" + "=" * 60)
print("FIM DA AULA 6")
print("=" * 60)
