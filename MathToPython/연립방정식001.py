from sympy import Symbol, solve

x = Symbol('x')

# eq001 = 2 * x - 4 * x - 9 - 3
# 2x + 3 = 4x - 9
# 
eq001 = 2 * x - 4 * x - (-9 - 3)

result = solve(eq001)
print(result)

