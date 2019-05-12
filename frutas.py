from gurobipy import *

# Create a new model fruta
m = Model("fruta")

# Create variables
f1 = m.addVar(vtype=GRB.INTEGER, name="f1")
f2 = m.addVar(vtype=GRB.INTEGER, name="f2")
f3 = m.addVar(vtype=GRB.INTEGER, name="f3")


# Set function objective
m.setObjective(20 * f1 + 10 * f2 + 30 *f3, GRB.MAXIMIZE)

# Add restricoes:
m.addConstr( f1 >= 0, "constraint1")
m.addConstr( f2 >= 0, "constraint2")
m.addConstr( f3 >= 0, "constraint3")

m.addConstr(f1 >= 200, "constraint4")
m.addConstr(f2 >= 100, "constraint5")
m.addConstr(f3 <= 200, "constraint6")

m.addConstr(f1 + f2 + f3 <= 800, "constraint7")

#executa
m.optimize()

#result
for v in m.getVars():
    print('%s %g' % (v.varName, v.x))
    
print('Objetivo: %g' % m.objVal)