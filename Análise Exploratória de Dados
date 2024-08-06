import matplotlib.pyplot as plt
import seaborn as sns

# Exemplo de análise exploratória
plt.figure(figsize=(10, 6))
sns.histplot(dados['idade'], kde=True)
plt.title('Distribuição de Idade dos Clientes')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()

# Visualização de correlações
plt.figure(figsize=(10, 6))
sns.heatmap(dados.corr(), annot=True, cmap='coolwarm')
plt.title('Matriz de Correlação')
plt.show()
