from gurobipy import *

# Create a new model
m = Model("produtos")

# Create variables
x1 = m.addVar(vtype=GRB.CONTINUOUS, name="x1")
x2 = m.addVar(vtype=GRB.CONTINUOUS, name="x2")
x3 = m.addVar(vtype=GRB.CONTINUOUS, name="x3")

# Set objective
m.setObjective(x1+x2+x3, GRB.MINIMIZE)

# Add constraint: x + y >= 1
m.addConstr(x1 >= 3000)
m.addConstr(0.03*x1 + 0.04*x2 >= 300)
m.addConstr(0.03*x1 + 0.1*x3 >= 300)
m.addConstr(x1+x2+x3 <= 10000)

m.optimize()

for v in m.getVars():
    print('%s %g' % (v.varName, v.x))

print('Obj: %g' % m.objVal)
