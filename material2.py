# -*- coding: utf-8 -*-
from gurobipy import *

m = Model("material")

custos = [[30,20,24,18], [12,36,30,24], [8,15,25,20]]
demanda = [50,80,40,100]

#criando as variáveis Xij
vars = []
for posto in range(3):
	for loja in range(4):
		vars.append(m.addVar(vtype=GRB.CONTINUOUS, name="x"+str(posto+1)+str(loja+1)))

#criando o objetivo mutiplicando cada custo[i][j] pela variavel[i][j]
objetivo = []
x = 0
for posto in range(3):
	for loja in range(4):
		objetivo = objetivo + custos[posto][loja]*vars[x]
		x += 1
m.setObjective(objetivo)

#criando restriçoes fixando o posto e variando a demanda de uma loja x11 + x21 + x21 >= demanda da loja 1
for loja in range(4):
	x=loja
	expr = 0
	for posto in range(3):
		expr = expr + vars[x]
		x=x+4
	m.addConstr(expr, GRB.GREATER_EQUAL, demanda[loja]/10) #dividir a demanda 
 #po 10 pois cada caminhão pode transportar 10 por viagem

#m.addConstr(vars[0]+vars[4]+vars[8], GRB.GREATER_EQUAL, 5) somando as variaveis do 3 postos q devem suprir a demanda da loja 1 

#otimizando
m.optimize()

# Write model to a file
m.write('material.lp')

#mostrando as variáveis
for v in m.getVars():
    print(v.varName, v.x)

#mostrando o objetivo
print('Objetivo:', m.ObjVal)

