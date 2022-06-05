import pulp

"""

DV : x1 = number of wooden soldiers produced each week
     x2 = number of wooden trains produced each week
obj:
    max 3x1 + 2*x2
st.:
    10x1 + 9x2 <= 900
    2x1 + x2 <= 100
    x1 + x2 <= 80
    All var. >= 0
"""

model = pulp.LpProblem("Giapetto Production Problem", pulp.LpMaximize)
X1 = pulp.LpVariable('X1', lowBound=0, cat=pulp.LpContinuous)
X2 = pulp.LpVariable('X2', lowBound=0, cat=pulp.LpInteger)

model += 3 * X1 + 2 * X2

model += 10 * X1 + 9 * X2 <= 900, 'Raw Metarial'
model += 2 * X1 + X2 <= 100, 'Finishing Hour'
model += X1 + X2 <= 80, 'Carpentry Hour'

model.solve()

if model.status == 1:
    print('Solution is optimal: %s' %pulp.LpStatus[model.status])
    print(f'Number of wooden soldiers = {X1.varValue}')
    print(f'Number of wooden train = {X2.varValue}')
else:
    print('Failed to find solution: %s' %pulp.LpStatus[model.status])
print('Objective function value =', pulp.value(model.objective))

