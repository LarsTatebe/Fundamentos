valor_compra = float(input("Digite o valor da compra: "))
num_parcelas = int(input("Digite a quantidade de parcelas: "))

desconto_parcela = 0
desconto_valor = 0

if num_parcelas == 1:
    desconto_parcela = 10
elif 2 <= num_parcelas <= 3:
    desconto_parcela = 5
else:
    desconto_parcela = 0

if valor_compra > 5000:
    desconto_valor = 5

desconto_total = desconto_parcela + desconto_valor

valor_desconto = valor_compra * (desconto_total / 100)

valor_final = valor_compra - valor_desconto

if num_parcelas > 0:
    valor_parcela = valor_final / num_parcelas
else:
    valor_parcela = valor_final

print(f"Desconto total: {valor_desconto:.2f}")
print(f"Valor final da compra com desconto: {valor_final:.2f}")

if num_parcelas > 1:
    print(f"Cada parcela será de: {valor_parcela:.2f}")
else:
    print(f"Cada parcela será de: {valor_final:.2f}")
