a = 2
b = 3

### Operadores Aritmeticos ###

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a**b)
print("\n")

### Operadores Logicos ###

print(a == b or a != b)
print(a != b and a == b)
print(not(a > b),'\n')


### Operadores de comparacion ### 

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print("\n")

### Operadores de Asignacion ###

a += b
print(a)

b -= a
print(b)

a *= a
print(a)

b /= b
print(b)

a **= a
print(a)

b %= b
print(b)

print("\n")

### Operadores de identidad ###

print(a is b)
print(b is not a)

print("\n")


### Operadores de pertenencia ###

c = [1,3]
print(b in c)
print(a not in c)

### Operadores de bits a bits ###
a = 2 
b = 3

print(a ^ b)
print(a & b)
print(a | b)
print("\n")

for x in range(10, 51, 2):
    if x == 16 or x % 3 == 0:
        pass
    else:
        print(x)
