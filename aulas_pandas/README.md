# Aulas de Pandas - Curso Introdutório

Este diretório contém 10 aulas iniciais para aprender a biblioteca Pandas do Python, focada em análise e manipulação de dados.

## 📚 Estrutura das Aulas

### Aula 1: Introdução ao Pandas e Series
- O que é Pandas
- Criando Series
- Operações básicas com Series
- Acessando elementos
- Estatísticas descritivas

### Aula 2: DataFrames - Criando e Operações Básicas
- O que é um DataFrame
- Criando DataFrames de diferentes formas
- Visualizando informações
- Acessando linhas e colunas
- Estatísticas descritivas

### Aula 3: Leitura e Escrita de Dados
- Salvando e lendo arquivos CSV
- Trabalhando com Excel
- Opções avançadas de leitura
- Lidando com valores faltantes em arquivos
- Exportando para diferentes formatos (JSON, HTML)

### Aula 4: Seleção e Indexação de Dados
- Selecionando colunas
- `.loc[]` - seleção por label
- `.iloc[]` - seleção por posição
- `.at[]` e `.iat[]` para valores individuais
- Diferenças entre métodos de seleção

### Aula 5: Filtragem e Consulta de Dados
- Filtragem simples e complexa
- Operadores lógicos (E, OU, NÃO)
- Métodos `.isin()`, `.between()`
- Método `.query()` para consultas
- Filtragem com strings

### Aula 6: Tratamento de Dados Faltantes
- Identificando valores nulos
- `.isnull()` e `.notnull()`
- Removendo valores faltantes com `.dropna()`
- Preenchendo valores com `.fillna()`
- Estratégias de preenchimento (média, mediana, moda)
- Interpolação de valores

### Aula 7: Manipulação de Dados - Colunas
- Adicionando novas colunas
- Cálculos com colunas
- Colunas condicionais
- Renomeando colunas
- Removendo colunas
- Reordenando colunas

### Aula 8: Agrupamento e Agregação
- `.groupby()` - agrupando dados
- Agregações simples (sum, mean, count)
- Múltiplas agregações com `.agg()`
- Agrupamento por múltiplas colunas
- Tabelas pivô com `.pivot_table()`
- Transformações em grupos

### Aula 9: Mesclando e Juntando DataFrames
- `.merge()` - inner, left, right, outer joins
- Merge com múltiplas colunas
- `.concat()` - concatenação vertical e horizontal
- `.join()` - juntando por índice
- Trabalhando com sufixos

### Aula 10: Visualização Básica de Dados
- Gráficos de linha, barra, pizza
- Histogramas e gráficos de dispersão
- Box plots e gráficos de área
- Subplots - múltiplos gráficos
- Personalização de gráficos

## 🚀 Como Usar

Cada aula é um arquivo Python independente que pode ser executado diretamente:

```bash
# Instale o pandas e matplotlib primeiro
pip install pandas matplotlib openpyxl

# Execute qualquer aula
python aula_01_introducao_series.py
python aula_02_dataframes.py
# ... e assim por diante
```

## 📋 Pré-requisitos

- Python 3.7 ou superior
- Bibliotecas necessárias:
  ```bash
  pip install pandas numpy matplotlib openpyxl
  ```

## 💡 Dicas de Estudo

1. **Siga a ordem**: As aulas foram projetadas para serem seguidas em sequência
2. **Execute o código**: Rode cada exemplo e observe os resultados
3. **Faça os exercícios**: Cada aula tem exercícios práticos no final
4. **Experimente**: Modifique os exemplos e teste suas próprias ideias
5. **Pratique**: A melhor forma de aprender é praticando com dados reais

## 📖 Recursos Adicionais

- [Documentação oficial do Pandas](https://pandas.pydata.org/docs/)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

## ✅ Próximos Passos

Após completar estas 10 aulas, você estará pronto para:
- Trabalhar com datasets reais
- Explorar análises mais complexas
- Aprender sobre machine learning com Scikit-learn
- Estudar visualizações avançadas com Seaborn e Plotly

---

**Bons estudos! 📊🐼**
