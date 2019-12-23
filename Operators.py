a = 12
b = 3

# An expression in python is anything that can be calculated to return a value
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b) #integer division, rounded down towards minus infinity
print(a % b) # 0 modulo: the remainder after integer division

print()

for i in range(1, a // b):
	print(i)

# Python follows PEMDAS
# Python allows use of parenthesis with expressions
print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 *12))
print ((((a + b) / 3) - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

input()
