from gurobipy import *

# Using Vector - structure
# Create Model
m = Model("liga")

# Vetores e Matrizes
distanciasEntrePostosELojas = [[30,20,24,18], [12,36,30,24], [8,15,25,20]]
demandaDeAreia = [50,80,40,100]

# Criando um vetor para as variáveis e adicionando ao modelo
vars=[]
for posto in range(3):
    for loja in range(4):
        vars.append(m.addVar(vtype=GRB.CONTINUOUS, name="Numero de Viagens do Posto "+str(posto+1)+" para a Loja "+str(loja+1)))

# Setando o Objetivo - Menor Distancia percorrida de posto i para loja j
goal = []
variavel=0
for posto in range(3):
    for loja in range(4):
        goal = goal + distanciasEntrePostosELojas[posto][loja]*vars[variavel]
        variavel += 1
m.setObjective(goal,GRB.MINIMIZE)

# Adicionando restrições
# Demanda das Lojas
for loja in range(4):
    variavel=loja
    exprDemandaDaLoja=0
    for posto in range(3):
        exprDemandaDaLoja= exprDemandaDaLoja + vars[variavel]
        variavel=variavel+4
    m.addConstr(exprDemandaDaLoja, GRB.GREATER_EQUAL, demandaDeAreia[loja]/10) 

#otimizando
m.optimize()

#mostrando as variáveis
for v in m.getVars():
    print(v.varName, v.x)

#mostrando o objetivo
print('Distância (km):', m.ObjVal)

