"""
AULA 3: Leitura e Escrita de Dados (CSV, Excel)
================================================

Objetivo: Aprender a ler e escrever dados em diferentes formatos
"""

import pandas as pd
import numpy as np
import os

print("=" * 60)
print("AULA 3: LEITURA E ESCRITA DE DADOS")
print("=" * 60)

# Vamos criar alguns dados de exemplo para trabalhar
print("\n1. CRIANDO DADOS DE EXEMPLO")
print("-" * 60)

# Dados de vendas para nossos exemplos
vendas = {
    'Data': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Webcam'],
    'Quantidade': [2, 10, 5, 3, 7],
    'Preço': [2500.00, 50.00, 150.00, 800.00, 200.00],
    'Vendedor': ['João', 'Maria', 'João', 'Pedro', 'Maria']
}
df_vendas = pd.DataFrame(vendas)
print("DataFrame de vendas criado:")
print(df_vendas)

print("\n2. SALVANDO EM ARQUIVO CSV")
print("-" * 60)
# CSV = Comma Separated Values (Valores Separados por Vírgula)
# É o formato mais comum para dados tabulares

# Criar diretório para os arquivos se não existir
os.makedirs('dados_exemplo', exist_ok=True)

# Salvando em CSV
df_vendas.to_csv('dados_exemplo/vendas.csv', index=False)
print("✓ Arquivo 'vendas.csv' salvo com sucesso!")
print("  Parâmetro index=False evita salvar a coluna de índice")

# Salvando com separador diferente
df_vendas.to_csv('dados_exemplo/vendas_ponto_virgula.csv', index=False, sep=';')
print("✓ Arquivo com separador ';' salvo!")

# Salvando com encoding específico
df_vendas.to_csv('dados_exemplo/vendas_utf8.csv', index=False, encoding='utf-8')
print("✓ Arquivo com encoding UTF-8 salvo!")

print("\n3. LENDO ARQUIVO CSV")
print("-" * 60)
# Lendo o CSV que acabamos de criar
df_lido = pd.read_csv('dados_exemplo/vendas.csv')
print("DataFrame lido do CSV:")
print(df_lido)

print("\nVerificando tipo de dados:")
print(df_lido.dtypes)

# Lendo CSV com separador diferente
df_pv = pd.read_csv('dados_exemplo/vendas_ponto_virgula.csv', sep=';')
print("\nLido com separador ';':")
print(df_pv.head(2))

print("\n4. LENDO CSV COM OPÇÕES AVANÇADAS")
print("-" * 60)

# Lendo apenas algumas colunas
df_parcial = pd.read_csv('dados_exemplo/vendas.csv', usecols=['Produto', 'Preço'])
print("Apenas colunas Produto e Preço:")
print(df_parcial)

# Lendo apenas as primeiras linhas
df_sample = pd.read_csv('dados_exemplo/vendas.csv', nrows=3)
print("\nApenas primeiras 3 linhas:")
print(df_sample)

print("\n5. TRABALHANDO COM DATAS")
print("-" * 60)
# Convertendo coluna para datetime
df_com_datas = pd.read_csv('dados_exemplo/vendas.csv', parse_dates=['Data'])
print("DataFrame com datas convertidas:")
print(df_com_datas)
print("\nTipo da coluna Data:", df_com_datas['Data'].dtype)

print("\n6. SALVANDO E LENDO EXCEL")
print("-" * 60)
# Para trabalhar com Excel, você pode precisar instalar: pip install openpyxl

try:
    # Salvando em Excel
    df_vendas.to_excel('dados_exemplo/vendas.xlsx', index=False, sheet_name='Vendas')
    print("✓ Arquivo Excel 'vendas.xlsx' salvo com sucesso!")
    
    # Lendo de Excel
    df_excel = pd.read_excel('dados_exemplo/vendas.xlsx', sheet_name='Vendas')
    print("\nDataFrame lido do Excel:")
    print(df_excel.head(3))
    
except ImportError:
    print("⚠ Para trabalhar com Excel, instale: pip install openpyxl")
    print("  Pulando exemplos de Excel por enquanto")

print("\n7. INFORMAÇÕES SOBRE O ARQUIVO")
print("-" * 60)
import os
tamanho = os.path.getsize('dados_exemplo/vendas.csv')
print(f"Tamanho do arquivo CSV: {tamanho} bytes")

print("\n8. LIDANDO COM VALORES FALTANTES")
print("-" * 60)
# Criando dados com valores faltantes
dados_incompletos = {
    'Nome': ['Ana', 'Bruno', 'Carla', None, 'Eduardo'],
    'Idade': [25, None, 30, 28, None],
    'Cidade': ['SP', 'RJ', None, 'MG', 'SP']
}
df_incompleto = pd.DataFrame(dados_incompletos)
print("DataFrame com valores faltantes:")
print(df_incompleto)

# Salvando - valores None viram NaN
df_incompleto.to_csv('dados_exemplo/dados_incompletos.csv', index=False)

# Lendo e identificando valores faltantes
df_lido_incompleto = pd.read_csv('dados_exemplo/dados_incompletos.csv')
print("\nValores faltantes por coluna:")
print(df_lido_incompleto.isnull().sum())

print("\n9. EXPORTANDO PARA DIFERENTES FORMATOS")
print("-" * 60)
# JSON
df_vendas.to_json('dados_exemplo/vendas.json', orient='records', indent=2)
print("✓ Salvo em JSON")

# HTML (útil para relatórios)
df_vendas.to_html('dados_exemplo/vendas.html', index=False)
print("✓ Salvo em HTML")

print("\n10. LENDO DADOS DA WEB (EXEMPLO)")
print("-" * 60)
print("Você também pode ler CSV diretamente de URLs:")
print("Exemplo: pd.read_csv('https://exemplo.com/dados.csv')")
print("(Requer conexão com internet)")

print("\n" + "=" * 60)
print("EXERCÍCIO PRÁTICO:")
print("=" * 60)
print("""
Usando os dados de vendas:
1. Calcule o valor total de cada venda (Quantidade × Preço)
2. Adicione essa coluna ao DataFrame
3. Salve o resultado em 'vendas_completas.csv'
4. Leia o arquivo de volta e mostre o total de vendas por vendedor
""")

# Solução do exercício:
print("\nSOLUÇÃO:")
print("-" * 60)

# 1 e 2. Calcular e adicionar coluna
df_vendas['Total'] = df_vendas['Quantidade'] * df_vendas['Preço']
print("DataFrame com coluna Total:")
print(df_vendas)

# 3. Salvar
df_vendas.to_csv('dados_exemplo/vendas_completas.csv', index=False)
print("\n✓ Arquivo 'vendas_completas.csv' salvo!")

# 4. Ler e agrupar por vendedor
df_completo = pd.read_csv('dados_exemplo/vendas_completas.csv')
print("\nTotal de vendas por vendedor:")
vendas_por_vendedor = df_completo.groupby('Vendedor')['Total'].sum()
print(vendas_por_vendedor)

print(f"\nVendedor com maior total: {vendas_por_vendedor.idxmax()}")
print(f"Valor: R$ {vendas_por_vendedor.max():.2f}")

print("\n" + "=" * 60)
print("FIM DA AULA 3")
print("=" * 60)
print("\n📁 Arquivos criados no diretório 'dados_exemplo/'")
