# Q1: X = 2 e Y = 4
# Q2: X = -2 e Y = 4
# Q3: X = -3 e Y = -2
# Q4: X = 3 e Y = -2
# Origem: X = 0 e Y = 0



valorX = float(int(input("insira o valor de x: ")))
valorY = float(int(input("insira o valor de y: ")))


if valorX >0 and valorY >0:
    print("Q1")
elif valorX <0 and valorY >0:
    print("Q2")
elif valorX <0 and valorY <0:
    print("Q3")
elif valorX >0 and valorY <0:
    print("Q4")
elif valorX >0 and valorY == 0:
    print("Está sobre o eixo x")
elif valorX == 0 and valorY >0:
    print("Está sobre o eixo y")
else:
    print("Está sobre a origem")