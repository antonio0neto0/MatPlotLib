import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_interactions import zoom_factory

figure, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 10))
figure.suptitle('Visualizações Recentes') 

cidades = ['São Paulo', 'Rio de Janeiro', 'Brasília', 'Salvador', 'Fortaleza']
populacao = [12180000, 6710000, 3050000, 2886000, 2800000]

# Plotar gráfico 1
axes[0, 0].bar(cidades, populacao)
axes[0, 0].set_title('População das Maiores Cidades do Brasil')
axes[0, 0].set_xlabel('Cidade')
axes[0, 0].set_ylabel('População')

# Preparação gráfico 4
produtos = pd.read_csv('./interativo/produtos.csv')

# Plotando cada linha
axes[1, 1].plot(produtos['Mes'], produtos['Produto A'],label='Produto A', marker='o', color='red')
axes[1, 1].plot(produtos['Mes'], produtos['Produto B'],label='Produto B', marker='s', color='blue')
axes[1, 1].plot(produtos['Mes'], produtos['Produto C'],label='Produto C', marker='^', color='green')

# Adicionando elementos gráficos
axes[1, 1].set_title('Vendas de Produtos ao longo dos meses')
axes[1, 1].set_xlabel('Mês')
axes[1, 1].set_ylabel('Vendas')
plt.legend()  # Exibe a legenda
plt.grid(True)

# Preparação gráfico 3

idade_populacao = [22, 25, 30, 35, 40, 42, 45, 50, 55, 60, 65, 70, 75, 80, 85]
# Plotar gráfico 3
axes[0, 1].hist(idade_populacao, bins=5, edgecolor='black')
axes[0, 1].set_title('Distribuição da Idade da População')
axes[0, 1].set_xlabel('Idade')
axes[0, 1].set_ylabel('Frequência')

# Preparação gráfico 4
altura = np.random.normal(170, 10, 100)
peso = altura * 0.7 + np.random.normal(0, 5, 100)
# Plotar gráfico 4

axes[1, 0].scatter(altura, peso, color='blue')
axes[1, 0].set_title('Altura vs. Peso')
axes[1, 0].set_xlabel('Altura (cm)')
axes[1, 0].set_ylabel('Peso (kg)')

for ax in axes.flat:
    zoom_factory(ax)
    
plt.show()
