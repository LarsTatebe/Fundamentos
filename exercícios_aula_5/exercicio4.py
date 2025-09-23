count = 0
maior = 0
while count < 6:
    num = int(input("Digite um número inteiro positivo:  "))
    if num > maior:
        maior = num
    count = count + 1

print("O maior número digitado foi: ", maior)