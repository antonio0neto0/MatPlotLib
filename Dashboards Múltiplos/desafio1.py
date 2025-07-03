# Desafio 1 - Baixe o código abaixo(desafio1.py) e coloque todos os gráficos abaixo dentro de um subplot
import matplotlib.pyplot as plt
import numpy as np

# Dados para o gráfico de barra
x = ['A', 'B', 'C', 'D', 'E']
y = [10, 24, 36, 40, 15]

# Cria o gráfico de barra
plt.bar(x, y)
plt.title('Gráfico de Barra')

# Dados para o gráfico de linha
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Cria o gráfico de linha
plt.plot(x, y)
plt.title('Gráfico de Linha')

# Dados para o gráfico de dispersão
x = np.random.rand(50)
y = np.random.rand(50)

# Cria o gráfico de dispersão
plt.scatter(x, y)
plt.title('Gráfico de Dispersão')

# Dados para o gráfico de pizza
labels = ['A', 'B', 'C', 'D', 'E']
sizes = [15, 30, 45, 10, 5]

# Cria o gráfico de pizza
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Gráfico de Pizza')

# Exibe os gráficos
plt.show()