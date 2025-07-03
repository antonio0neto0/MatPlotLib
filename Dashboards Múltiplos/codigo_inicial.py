import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Preparação gráfico 1
cidades = ['São Paulo', 'Rio de Janeiro', 'Brasília', 'Salvador', 'Fortaleza']
populacao = [12180000, 6710000, 3050000, 2886000, 2800000]

# Plotar gráfico 1
plt.figure(figsize=(7,3))
plt.bar(cidades, populacao)
plt.title('População das Maiores Cidades do Brasil')
plt.xlabel('Cidade')
plt.ylabel('População')
plt.show()


# Preparação gráfico 2
idade_populacao = [22, 25, 30, 35, 40, 42, 45, 50, 55, 60, 65, 70, 75, 80, 85]
# Plotar gráfico 2
plt.hist(idade_populacao, bins=5, edgecolor='black')
plt.title('Distribuição da Idade da População')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()

# Preparação gráfico 3
altura = np.random.normal(170, 10, 100)
peso = altura * 0.7 + np.random.normal(0, 5, 100)
# Plotar gráfico 3
plt.scatter(altura, peso, color='blue')
plt.title('Altura vs. Peso')
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.show()

# Preparação gráfico 4
cursos = ['Engenharia', 'Ciências Sociais', 'Medicina', 'Economia']
quantidades_alunos = [300, 150, 450, 200]
# Plotagem do gráfico de linha 4
plt.pie(quantidades_alunos, labels=cursos, autopct='%1.1f%%')
plt.title('Distribuição de Alunos por Curso')

plt.show()