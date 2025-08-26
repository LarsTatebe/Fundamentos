nota1 = float(int(input("insira a nota da primeira prova: ")))
nota2 = float(int(input("insira a nota da segunda prova: ")))
media = (nota1 + nota2)/2

if media < 5:
    print("Reprovado kkkkk")

else:
    if media == 10:
        print("Aprovado com distinção")

    else:
        print("Aprovado")