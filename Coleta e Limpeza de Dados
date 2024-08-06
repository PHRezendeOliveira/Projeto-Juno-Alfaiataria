import pandas as pd

# Exemplo de leitura e limpeza de dados
dados = pd.read_csv('dados_juno_alfaiataria.csv')

# Remoção de duplicatas
dados = dados.drop_duplicates()

# Tratamento de valores ausentes
dados.fillna(method='ffill', inplace=True)

# Normalização de dados
dados['idade'] = (dados['idade'] - dados['idade'].mean()) / dados['idade'].std()

print(dados.head())
