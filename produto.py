from gurobipy import *

# Create a new model produto
m = Model("produto")

# Create variables
p1 = m.addVar(vtype=GRB.INTEGER, name="p1")
p2 = m.addVar(vtype=GRB.INTEGER, name="p2")


# Set function objective
m.setObjective(100 * p1 + 150 * p2, GRB.MAXIMIZE)

# Add restricoes:
m.addConstr( p1 >= 0, "constraint1")
m.addConstr( p2 >= 0, "constraint2")

m.addConstr(p1 <= 40, "constraint3")
m.addConstr(p2 <= 30, "constraint3")

m.addConstr(2 * p1 + 3*p2 <= 120, "constraint4")

#executa
m.optimize()


for v in m.getVars():
    print('%s %g' % (v.varName, v.x))
    
print('Obj: %g' % m.objVal)