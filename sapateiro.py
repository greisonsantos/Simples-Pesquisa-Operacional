from gurobipy import *

# Create a new model sapateiro
m = Model("sapateiro")

# Create variables
x1 = m.addVar(vtype=GRB.INTEGER, name="x1")
x2 = m.addVar(vtype=GRB.INTEGER, name="x2")

# Set function objective
m.setObjective(5*x1+2*x2, GRB.MAXIMIZE)

# Add restricoes:
m.addConstr( x1 >= 0, "constraint1")
m.addConstr( x2 >= 0, "constraint2")

m.addConstr(10 * x1 + 12 * x2 <= 60, "constraint3")
m.addConstr(2 * x1 + x2 <= 6, "constraint4")

#executa
m.optimize()


for v in m.getVars():
    print('%s %g' % (v.varName, v.x))
    
print('Obj: %g' % m.objVal)