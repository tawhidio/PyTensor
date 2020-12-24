from sympy import Symbol, solve

x = Symbol('x')
y = Symbol('y')

## 2x + 3 = 4x - 9# 

eq001 = 2 * x - 4 * x - (-9 - 3)

result = solve(eq001)
print("result => ", result)

eq002 = y - 10 * x + 1234
result2 = solve(eq002)
print("reuslt2 => ", eq002)
