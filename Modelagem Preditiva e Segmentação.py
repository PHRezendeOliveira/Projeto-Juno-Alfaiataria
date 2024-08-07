from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

# Exemplo de regressão linear para prever gastos dos clientes
X = dados[['idade', 'renda']]
y = dados['gastos']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo_regressao = LinearRegression()
modelo_regressao.fit(X_train, y_train)

predicoes = modelo_regressao.predict(X_test)
print("Predições:", predicoes)

# Exemplo de clustering para segmentação de clientes
modelo_clustering = KMeans(n_clusters=3)
dados['segmento'] = modelo_clustering.fit_predict(dados[['idade', 'renda']])

plt.figure(figsize=(10, 6))
sns.scatterplot(x='idade', y='renda', hue='segmento', data=dados, palette='viridis')
plt.title('Segmentação de Clientes')
plt.xlabel('Idade')
plt.ylabel('Renda')
plt.show()
