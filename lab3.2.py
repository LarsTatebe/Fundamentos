numero_1 =(int(input("Digite o valor do primeiro produto: ")))
numero_2 =(int(input("Digite o valor do segundo produto: ")))
numero_3 =(int(input("Digite o valor do terceiro produto: ")))

total = numero_1 + numero_2 + numero_3

if total > 500.00:
    desconto = 0.2
    resultado = total * desconto
    print(f"Desconto: {resultado:.2f}")

else:
    desconto = 0.1
    resultado = total * desconto
    print(f"Desconto: {resultado:.2f}")