import matplotlib.pyplot as plt

meses =  [6,7,8,9,10,11]
vendas = [190, 210, 180, 200, 195, 220]

plt.plot(meses, vendas)
plt.title('Vendas Mensais')
plt.xlabel('Meses')
plt.ylabel('Vendas')
# Como adicionar texto
plt.text(7.8, 178.5,"Pior mês",fontsize=10,color='red')
plt.text(10.5, 220,"Melhor mês",fontsize=10,color='green',backgroundcolor='black')
# xy - coordenadas de onde finaliza(ou para onde está apontando a seta)
# xytext - coordenadas de onde inicia a seta e o texto

plt.show()
