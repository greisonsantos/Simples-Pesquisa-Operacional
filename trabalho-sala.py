from gurobipy import *

m = Model("problema_televisao")

#criando variaveis e adicionando ao modelo vetor de producao e de demanda de vedenda de cada centro

producao = [1000,5000,6000]
demanda  = [6000, 5000, 2000, 1000, 3000]

# cidade=['sao paulo', 'joao pessoa', 'manaus']


#matriz de custo de tranposte
custo = [[1000,2000,3000, 3500, 4000],
         [4000,2000,1500, 1200, 4000],
         [6000,4000,3500, 3000, 2000]
        ]


#adicionando as variaveis  3 cidades para 5  centros de distribuicoes
vars = []
for cidade in range(3):
        for producao in range(5):
                vars.append(m.addVar(vtype=GRB.INTEGER, name="x"+str(cidade+1)+str(producao+1)))



#criando o objetivo mutiplicando cada custo[i][j]
objetivo = []
x = 0
for cidade in range(3):
        for producao in range(5):
                objetivo = objetivo + custo[cidade][producao]*vars[x]
                x += 1
m.setObjective(objetivo,GRB.MINIMIZE)



#criando restricoes fixando A cidade  e variando os centros de distribuicao
for producao in range(5):
        x=producao
        expr = 0
        for cidade in range(3):
                expr = expr + vars[x]
                x=x+5
                
        # tem que ser menor que producao no igual
        m.addConstr(expr, GRB.GREATER_EQUAL, demanda[producao])


#otimizando
m.optimize()

# #mostrando as variaveis
for v in m.getVars():
    print(v.varName, v.x)

 #mostrando o objetivo que foi otimizado
print('Funcao Objetivo:', m.ObjVal/1000)



