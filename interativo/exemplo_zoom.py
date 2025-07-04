import matplotlib.pyplot as plt
from mpl_interactions import zoom_factory

figure, axes = plt.subplots(figsize=(10,10))

idade_populacao = [22, 25, 30, 35, 40, 42, 45, 50, 55, 60, 65, 70, 75, 80, 85]

axes.hist(idade_populacao, bins=5, edgecolor='black')
axes.set_title('Distribuição da Idade da População')
axes.set_xlabel('Idade')
axes.set_ylabel('Frequência')

# Habilitar zoom
zoom_factory(axes)

plt.show()

# python  .\interativo\exemplo_zoom.py