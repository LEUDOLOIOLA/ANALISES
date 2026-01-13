"""
AULA 7: Manipulação de Dados - Adicionando e Removendo Colunas
===============================================================

Objetivo: Aprender a adicionar, modificar e remover colunas em DataFrames
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("AULA 7: MANIPULAÇÃO - ADICIONANDO E REMOVENDO COLUNAS")
print("=" * 60)

# Criando DataFrame de exemplo
print("\n1. CRIANDO DATAFRAME INICIAL")
print("-" * 60)
dados = {
    'Nome': ['Ana', 'Bruno', 'Carla', 'Diego', 'Elena'],
    'Idade': [25, 30, 28, 35, 27],
    'Salário': [5000, 8000, 6000, 7000, 5500]
}
df = pd.DataFrame(dados)
print(df)

print("\n2. ADICIONANDO UMA COLUNA SIMPLES")
print("-" * 60)

# Adicionar coluna com valor fixo
df['Departamento'] = 'TI'
print("Adicionando coluna 'Departamento' com valor fixo:")
print(df)

# Adicionar coluna com lista de valores
df['Cidade'] = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre']
print("\nAdicionando coluna 'Cidade' com lista:")
print(df)

print("\n3. ADICIONANDO COLUNA COM CÁLCULO")
print("-" * 60)

# Calcular a partir de outras colunas
df['Salário_Anual'] = df['Salário'] * 12
print("Salário anual (Salário × 12):")
print(df)

# Múltiplos cálculos
df['Bonus'] = df['Salário'] * 0.1
df['Salário_Total'] = df['Salário'] + df['Bonus']
print("\nAdicionando Bonus e Salário Total:")
print(df[['Nome', 'Salário', 'Bonus', 'Salário_Total']])

print("\n4. ADICIONANDO COLUNA CONDICIONAL")
print("-" * 60)

# Usando condição simples
df['Faixa_Salarial'] = df['Salário'].apply(
    lambda x: 'Alto' if x > 6000 else 'Médio' if x > 5000 else 'Baixo'
)
print("Classificação por faixa salarial:")
print(df[['Nome', 'Salário', 'Faixa_Salarial']])

# Usando np.where (condição ternária)
df['Senior'] = np.where(df['Idade'] >= 30, 'Sim', 'Não')
print("\nClassificação por seniority (idade >= 30):")
print(df[['Nome', 'Idade', 'Senior']])

print("\n5. USANDO .assign() PARA MÚLTIPLAS COLUNAS")
print("-" * 60)

# assign() cria novas colunas e retorna uma cópia
df_novo = df.assign(
    Salário_Mensal=df['Salário'],
    Imposto=df['Salário'] * 0.15,
    Salário_Líquido=df['Salário'] * 0.85
)
print("Usando assign() para criar múltiplas colunas:")
print(df_novo[['Nome', 'Salário_Mensal', 'Imposto', 'Salário_Líquido']])

print("\n6. ADICIONANDO COLUNA COM .loc[]")
print("-" * 60)

# Alternativa para adicionar coluna
df.loc[:, 'País'] = 'Brasil'
print("Adicionando coluna 'País':")
print(df.head(3))

print("\n7. MODIFICANDO VALORES DE COLUNA")
print("-" * 60)

# Modificar coluna inteira
print("Salários originais:")
print(df['Salário'].values)

df['Salário'] = df['Salário'] * 1.05  # Aumento de 5%
print("\nApós aumento de 5%:")
print(df['Salário'].values)

# Modificar valores específicos com condição
df.loc[df['Idade'] > 30, 'Bonus'] = df['Salário'] * 0.15
print("\nBonus aumentado para pessoas > 30 anos:")
print(df[['Nome', 'Idade', 'Bonus']])

print("\n8. RENOMEANDO COLUNAS")
print("-" * 60)

# Renomear uma ou mais colunas
df_renomeado = df.rename(columns={
    'Nome': 'Nome_Completo',
    'Salário': 'Salário_Mensal'
})
print("Colunas renomeadas:")
print(df_renomeado.columns.tolist())
print(df_renomeado.head(2))

# Renomear todas as colunas
df_temp = df[['Nome', 'Idade', 'Salário']].copy()
df_temp.columns = ['NOME', 'IDADE', 'SALÁRIO']
print("\nTodas as colunas em maiúsculas:")
print(df_temp.head(2))

print("\n9. REMOVENDO COLUNAS - drop()")
print("-" * 60)

print("Colunas atuais:", df.columns.tolist())

# Remover uma coluna
df_sem_pais = df.drop('País', axis=1)
print("\nApós remover 'País':")
print(df_sem_pais.columns.tolist())

# Remover múltiplas colunas
df_limpo = df.drop(['Departamento', 'País', 'Senior'], axis=1)
print("\nApós remover múltiplas colunas:")
print(df_limpo.columns.tolist())
print(df_limpo)

# Remover colunas inplace (modifica o DataFrame original)
df_teste = df.copy()
df_teste.drop('País', axis=1, inplace=True)
print("\nRemovendo inplace (modifica original):")
print(df_teste.columns.tolist())

print("\n10. REMOVENDO COLUNAS COM del")
print("-" * 60)

df_copia = df.copy()
print("Antes:", df_copia.columns.tolist())
del df_copia['País']
print("Depois de del:", df_copia.columns.tolist())

print("\n11. REMOVENDO COLUNAS COM .pop()")
print("-" * 60)

df_copia = df.copy()
print("Antes:", df_copia.columns.tolist())
coluna_removida = df_copia.pop('Departamento')
print("Depois de pop:", df_copia.columns.tolist())
print("Valores removidos:", coluna_removida.values)

print("\n12. SELECIONANDO APENAS COLUNAS DESEJADAS")
print("-" * 60)

# Forma mais limpa de "remover" colunas
colunas_desejadas = ['Nome', 'Idade', 'Salário', 'Cidade']
df_selecionado = df[colunas_desejadas]
print("Selecionando apenas colunas específicas:")
print(df_selecionado)

print("\n13. REORDENANDO COLUNAS")
print("-" * 60)

print("Ordem original:", df.columns.tolist())

# Definir nova ordem
nova_ordem = ['Nome', 'Cidade', 'Idade', 'Departamento', 'Salário', 'Bonus', 
              'Salário_Anual', 'Salário_Total', 'Faixa_Salarial', 'Senior', 'País']
df_reordenado = df[nova_ordem]
print("Nova ordem:", df_reordenado.columns.tolist())
print(df_reordenado.head(2))

print("\n14. INSERINDO COLUNA EM POSIÇÃO ESPECÍFICA")
print("-" * 60)

df_insercao = df[['Nome', 'Idade', 'Salário']].copy()
print("DataFrame original:")
print(df_insercao)

# Inserir coluna na posição 1 (entre Nome e Idade)
df_insercao.insert(1, 'ID', range(1, len(df_insercao) + 1))
print("\nApós inserir 'ID' na posição 1:")
print(df_insercao)

print("\n15. APLICANDO FUNÇÕES A COLUNAS")
print("-" * 60)

# Criar nova coluna aplicando função
def classificar_idade(idade):
    if idade < 25:
        return 'Jovem'
    elif idade < 35:
        return 'Adulto'
    else:
        return 'Senior'

df['Categoria_Idade'] = df['Idade'].apply(classificar_idade)
print("Classificação por idade:")
print(df[['Nome', 'Idade', 'Categoria_Idade']])

# Aplicar função a múltiplas colunas
df['Nome_Cidade'] = df.apply(lambda row: f"{row['Nome']} - {row['Cidade']}", axis=1)
print("\nCombinando colunas:")
print(df[['Nome', 'Cidade', 'Nome_Cidade']])

print("\n" + "=" * 60)
print("EXERCÍCIO PRÁTICO:")
print("=" * 60)
print("""
Crie um DataFrame de produtos com: Nome, Preço, Quantidade

Depois:
1. Adicione coluna 'Valor_Total' (Preço × Quantidade)
2. Adicione coluna 'Categoria' baseada no preço:
   - < 100: 'Econômico'
   - 100-500: 'Intermediário'  
   - > 500: 'Premium'
3. Adicione coluna 'Desconto': 5% para Econômico, 10% para Premium
4. Calcule 'Preço_Final' (Preço - Desconto)
5. Remova a coluna 'Desconto'
6. Renomeie 'Valor_Total' para 'Total'
""")

# Solução do exercício:
print("\nSOLUÇÃO:")
print("-" * 60)

# Criando DataFrame
produtos = {
    'Nome': ['Mouse', 'Teclado', 'Monitor', 'Webcam', 'Fone'],
    'Preço': [50, 150, 800, 200, 120],
    'Quantidade': [10, 5, 3, 7, 8]
}
df_produtos = pd.DataFrame(produtos)
print("1. DataFrame inicial:")
print(df_produtos)

# 1. Adicionar Valor_Total
df_produtos['Valor_Total'] = df_produtos['Preço'] * df_produtos['Quantidade']
print("\n2. Com Valor_Total:")
print(df_produtos)

# 2. Adicionar Categoria
def categorizar(preco):
    if preco < 100:
        return 'Econômico'
    elif preco <= 500:
        return 'Intermediário'
    else:
        return 'Premium'

df_produtos['Categoria'] = df_produtos['Preço'].apply(categorizar)
print("\n3. Com Categoria:")
print(df_produtos)

# 3. Adicionar Desconto
df_produtos['Desconto'] = df_produtos.apply(
    lambda row: row['Preço'] * 0.05 if row['Categoria'] == 'Econômico' 
           else row['Preço'] * 0.10 if row['Categoria'] == 'Premium'
           else 0,
    axis=1
)
print("\n4. Com Desconto:")
print(df_produtos)

# 4. Calcular Preço_Final
df_produtos['Preço_Final'] = df_produtos['Preço'] - df_produtos['Desconto']
print("\n5. Com Preço_Final:")
print(df_produtos)

# 5. Remover Desconto
df_produtos = df_produtos.drop('Desconto', axis=1)
print("\n6. Sem coluna Desconto:")
print(df_produtos)

# 6. Renomear
df_produtos = df_produtos.rename(columns={'Valor_Total': 'Total'})
print("\n7. Com coluna renomeada:")
print(df_produtos)

print("\n" + "=" * 60)
print("RESUMO DE MÉTODOS:")
print("=" * 60)
print("""
ADICIONAR:
• df['nova_coluna'] = valor       → Adiciona nova coluna
• df.assign(col=valor)            → Adiciona e retorna cópia
• df.insert(pos, nome, valores)   → Insere em posição específica

MODIFICAR:
• df['coluna'] = novos_valores    → Modifica coluna
• df.rename(columns={})           → Renomeia colunas
• df.columns = nova_lista         → Renomeia todas

REMOVER:
• df.drop('coluna', axis=1)       → Remove coluna (retorna cópia)
• df.drop([...], axis=1)          → Remove múltiplas
• del df['coluna']                → Remove (modifica original)
• df.pop('coluna')                → Remove e retorna valores
""")

print("\n" + "=" * 60)
print("FIM DA AULA 7")
print("=" * 60)
