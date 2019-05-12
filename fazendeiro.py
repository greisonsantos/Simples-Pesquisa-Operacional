from gurobipy import *

# Create a new model
m = Model("fazendeiro")

# Create variables
A = m.addVar(vtype=GRB.INTEGER, name="A")
P = m.addVar(vtype=GRB.INTEGER, name="P")
S = m.addVar(vtype=GRB.INTEGER, name="S")

# Set objective
m.setObjective(300*A + 400*P + 500*S, GRB.MAXIMIZE)

# Add constraint: x + y >= 1
m.addConstr(A+P+S <= 100)
m.addConstr(100000*P + 200000*S <= 12750000)
m.addConstr(100*P + 200*S <= 14000)

m.optimize()

for v in m.getVars():
    print('%s %g' % (v.varName, v.x))

print('Obj: %g' % m.objVal)
