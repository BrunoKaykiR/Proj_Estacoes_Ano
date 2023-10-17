#Programa Verificador de Estações do Ano
#By: Bruno Ribeiro
from datetime import datetime

#INPUTS

day = int(input('Informe o Dia: '))
month = input('Escreva o Mês: ').strip().lower()

mesaf = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

#PROCESSAMENTO E SAÍDAS

if month in mesaf:
##MÊS VÁLIDO

#ESTRUTURA DE CONDICIONAMENTOS

    if month in mesaf[2:5]:
        if day < 20 and month == 'março':
            print('Verão')
        else:
            print('Outono')

    elif month in mesaf[5:8]:
        if day < 21 and month == 'junho':
            print('Outono')
        else:
            print('Inverno')

    elif month in mesaf[8:11]:
        if day < 23 and month == 'setembro':
            print('Inverno')
        else:
            print('Primavera')

    else:
        print('Verão')

#MÊS INVÁLIDADO
else:
    print('Mês Inválido!')


