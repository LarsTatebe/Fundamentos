tempo_gasto = int(input("Quanto tempo, em minutos, você ficou no telefone:"))

if tempo_gasto >= 400:
    valor = tempo_gasto * 0.15

else:
    if tempo_gasto <= 200:
        valor = tempo_gasto * 0.20
    else:
        valor = tempo_gasto * 0.18

print("O valor da ligação é: R$  ", valor)

