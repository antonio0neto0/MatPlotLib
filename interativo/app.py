import matplotlib.pyplot as plt
import pandas as pd

dados_faculdade = pd.read_csv('./interativo/cursos.csv')
dados_faculdade['Data'] = pd.to_datetime(dados_faculdade['Data'])
dados_faculdade['Ano'] = dados_faculdade['Data'].dt.year
cursos_noturnos = dados_faculdade[(dados_faculdade['Turno'] == 'Noturno') & (
    dados_faculdade['Ano'].isin([2018, 2019, 2020, 2021, 2022]))]
dados_agrupados = cursos_noturnos.groupby(['Curso', 'Ano']).agg(
    {'Mensalidade': 'median'}).reset_index()
dados_pivotados = dados_agrupados.pivot_table(
    index='Ano', columns='Curso', values='Mensalidade')

plt.figure(figsize=(13, 5), dpi=150)
plt.plot(dados_pivotados.index,  dados_pivotados['Enfermagem'],
         label='Enfermagem', marker='o', linestyle='solid', linewidth=2, color='green')
plt.plot(dados_pivotados.index,  dados_pivotados['Odontologia'],
         label='Odontologia', marker='o', linestyle='solid', linewidth=2, color='blue')
plt.plot(dados_pivotados.index,  dados_pivotados['Medicina'],
         label='Medicina', marker='o', linestyle='solid', linewidth=2, color='red')
plt.title('Média das mensalidades entre 2018 a 2022')
plt.xlabel('Ano')
plt.ylabel('Média de mensalidade')
plt.legend(title='Curso')
plt.grid(True)

plt.show()