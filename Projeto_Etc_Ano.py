#Programa Verificador de Estações do Ano
#By: Bruno Ribeiro
from datetime import datetime

#INPUTS

day = int(input('Informe o Dia: '))
month = input('Escreva o Mês: ').strip().lower()

mesaf = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

#PROCESSAMENTO E SAÍDAS

if month in mesaf and day <= 31:
##MÊS VÁLIDO

#ESTRUTURA DE CONDICIONAMENTOS

    if month in mesaf[2:5]:
        if day < 20 and month == 'março':
            print(f'A Estação do dia {day} e mês de {month} é Verão')
        else:
            print(f'A Estação do dia {day} e mês de {month} é Outono')

    elif month in mesaf[5:8]:
        if day < 21 and month == 'junho':
            print(f'A Estação do dia {day} e mês de {month} é Outono')
        else:
            print(f'A Estação do dia {day} e mês de {month} é Inverno')

    elif month in mesaf[8:10]:
        if day < 23 and month == 'setembro':
            print(f'A Estação do dia {day} e mês de {month} é Inverno')
        else:
            print(f'A Estação do dia {day} e mês de {month} é Primavera')

    elif month == 'dezembro' or month == 'janeiro' or month == 'fevereiro':
        if day < 22 and month == 'dezembro':
            print(f'A Estação do dia {day} e mês de {month} é Primavera')

        else:
            print(f'A Estação do dia {day} e mês {month} é Verão')

#MÊS INVÁLIDADO
else:
    print('Certifique-se de inserir valores válidos!')


