import math

escolha = input("Você deseja calcular o volume do dodecaedro ou icosaedro: ")
aresta = int(input("Digite o valor da aresta a em metros: "))

if escolha == "dodecaedro":
    resultado = (15 + 7 * math.sqrt(5)) / 4 * aresta**3 
    print(f"O volume de um dodecaedro regular com {aresta:.2f} de aresta é: {resultado:.2f}")
elif escolha == "icosaedro":
    resultado = (5 / 12) * (3 + math.sqrt(5)) * aresta**3
    print(f"O volume de um icosaedro regular com {aresta:.2f} de aresta é: {resultado:.2f}")
else:
    print("forma inválida")
