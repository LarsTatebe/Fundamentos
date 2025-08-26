salario = float(int(input("insira o valor do seu salário: ")))

if salario >=0 and salario >=400.00:
    novo_salario = salario * 1.15
    reajuste = salario * 0.15
    print("seu reajuste é de: ", reajuste)
    print("seu salário é de: ", novo_salario)
elif salario >=400.01 and salario >=800.00:
    novo_salario = salario * 1.12
    reajuste = salario * 0.12
    print("seu reajuste é de: ", reajuste)
    print("seu salário é de: ", novo_salario)
elif salario >=800.01 and salario >=1200.00:
    novo_salario = salario * 1.10
    reajuste = salario * 0.10
    print("seu reajuste é de: ", reajuste)
    print("seu salário é de: ", novo_salario)
elif salario >=1200.01 and salario >=2000.00:
    novo_salario = salario * 1.7
    reajuste = salario * 0.07
    print("seu reajuste é de: ", reajuste)
    print("seu salário é de: ", novo_salario)
else:
    novo_salario = salario * 1.4
    reajuste = salario * 0.04
    print("seu reajuste é de: ", reajuste)
    print("seu salário é de: ", novo_salario)