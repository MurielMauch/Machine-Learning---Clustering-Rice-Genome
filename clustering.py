# -*- coding: utf-8 -*-
import pandas as pd
from pandas import Series

########## abre os arquivos csv ##########
amilose = pd.read_csv('DADOS-CNAE-Qualidade.csv')
genoma = pd.read_csv('cromoRice2.csv')

########## pega o indice de identificaçao e salva em coluna_ident ##########
coluna_ident = amilose['Denominacao - GBS']
#print type(coluna_ident)
#print coluna_ident
#print coluna_ident[0]

########## pega o teor de amilose de cada indice e guarda em célula ##########
celula = []
cont = 0

for i in coluna_ident:
    celula.append(amilose.at[cont,'TA Goiania 2005'])
    cont = cont + 1
#print celula

########## bases receberá as bases nitrogenadas de um dado indice ##########
cont = 0
#HÁ ALGUNS INDICES DOS QUAIS NÃO EXISTE BASE NITROGENADA
#O 248 E O 100 NÃO EXISTEM
for i in coluna_ident:
    if  str(coluna_ident[cont]) != str(248) and str(coluna_ident[cont]) != str(100):
        bases = genoma[str(coluna_ident[cont])]
    cont = cont + 1
#print genoma
#print bases

'''
#A IDEIA DO TRECHO A SEGUIR ERA CRIAR UMA LISTA COM O TEOR DE AMILOSE E
#A BASE NITROGENADA, NO ENTANTO, NESSE MOMENTO HÁ DOIS PROBLEMAS
#1 - NÃO DOU O SHIFT DA PRIMEIRA POSIÇÃO
#2 - TENHO UM VETOR "celula" NA PRIMEIRA POSIÇÃO, E NÃO SEI RELACIONÁ-LO AS bases
#TAMBÉM NÃO SEI SE ESSE TRECHO SERÁ NECESSÁRIO
print 'EXEMPLO'

exemplar = bases
print exemplar
conversor = pd.Series(str(celula))
exemplar[0] = conversor[0]
print exemplar
'''
