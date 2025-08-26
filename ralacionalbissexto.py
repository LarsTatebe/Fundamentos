# Faz a leitura de um numero do usuario e armazena na variavel






ano = int(input("Digite o Ano: \n"))

# verifica se o ano é ou não bissexto

if (ano % 400 == 0) or (ano % 4 == 0 and not(ano  % 100 == 0)):
    print("Bissexto")
else:
    print('Não é bissexto')