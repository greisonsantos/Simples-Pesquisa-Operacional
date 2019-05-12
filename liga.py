from gurobipy import *

# Create a new model
m = Model("liga")

# Create variables
mr1 = m.addVar(vtype=GRB.CONTINUOUS, name="mr1")
mr2 = m.addVar(vtype=GRB.CONTINUOUS, name="mr2")

F = m.addVar(vtype=GRB.CONTINUOUS, name="F")
C = m.addVar(vtype=GRB.CONTINUOUS, name="C")
S = m.addVar(vtype=GRB.CONTINUOUS, name="S")
N = m.addVar(vtype=GRB.CONTINUOUS, name="N")

# Set objective
m.setObjective(0.30*F + 0.20*C + 0.28*S + 0.5*N + 0.2*mr1 + 0.25*mr2, GRB.MINIMIZE)

# Add constraint: x + y >= 1
m.addConstr(0.6*mr1 + 0.7*mr2 + F >= 0.60)
m.addConstr(0.6*mr1 + 0.7*mr2 + F <= 0.65)

# Add constraint: x + y >= 1
m.addConstr(0.2*mr1 + 0.2*mr2 + C >= 0.15)
m.addConstr(0.2*mr1 + 0.2*mr2 + C <= 0.20)

# Add constraint: x + y >= 1
m.addConstr(0.2*mr1 + 0.05*mr2 + S >= 0.15)
m.addConstr(0.2*mr1 + 0.05*mr2 + S <= 0.20)

# Add constraint: x + y >= 1
m.addConstr(0.05*mr2 + N >= 0.05)
m.addConstr(0.05*mr2 + N <= 0.08)

m.optimize()

for v in m.getVars():
    print('%s %g' % (v.varName, v.x))

print('Obj: %g' % m.objVal)
