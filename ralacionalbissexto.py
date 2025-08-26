# Faça um programa que lê um ano






ano = int(input("Digite o Ano: \n"))

if (ano % 400 == 0) or (ano % 4 == 0 and not(ano  % 100 == 0)):
    print("Bissexto")
else:
    print('Não é bissexto')