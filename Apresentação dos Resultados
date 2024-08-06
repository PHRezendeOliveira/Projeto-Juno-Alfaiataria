# Exemplo de relatório em Jupyter Notebook
from IPython.display import display, Markdown

# Relatório simples com Markdown
display(Markdown("# Análise e Recomendações para Juno Alfaiataria"))
display(Markdown("## Análise Exploratória"))
display(Markdown("### Distribuição de Idade dos Clientes"))
plt.figure(figsize=(10, 6))
sns.histplot(dados['idade'], kde=True)
plt.title('Distribuição de Idade dos Clientes')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()

display(Markdown("### Matriz de Correlação"))
plt.figure(figsize=(10, 6))
sns.heatmap(dados.corr(), annot=True, cmap='coolwarm')
plt.title('Matriz de Correlação')
plt.show()

display(Markdown("## Modelagem Preditiva"))
display(Markdown(f"### Predições de Gastos: {predicoes}"))

display(Markdown("## Segmentação de Clientes"))
plt.figure(figsize=(10, 6))
sns.scatterplot(x='idade', y='renda', hue='segmento', data=dados, palette='viridis')
plt.title('Segmentação de Clientes')
plt.xlabel('Idade')
plt.ylabel('Renda')
plt.show()
