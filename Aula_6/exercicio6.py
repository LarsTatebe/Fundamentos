import math

def area (x, y,z):
    res = math.sqrt(x) + math.sqrt(y) + math.sqrt(z) + ((x + y)/2) + ((y + z)/2) + ((x + z)/2) 

    return res

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))
print("resultado = ", area(x,y,z))