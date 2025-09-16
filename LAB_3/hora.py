hora_inicial = int(input("Digite a hora inicial: "))
minuto_inicial = int(input("Digite o minuto inicial: "))
hora_final = int(input("Digite a hora final: "))
minuto_final = int(input("Digite o minuto final: "))

# Converter tudo para minutos
total_minutos_inicial = hora_inicial * 60 + minuto_inicial
total_minutos_final = hora_final * 60 + minuto_final
    
    # Calcular a diferença em minutos
if total_minutos_final > total_minutos_inicial:
    duracao_minutos = total_minutos_final - total_minutos_inicial
else:
        # Se o jogo termina no dia seguinte
    duracao_minutos = (24 * 60 - total_minutos_inicial) + total_minutos_final
    
    # Garantir duração mínima de 1 minuto
if duracao_minutos == 0:
    duracao_minutos = 24 * 60  # 24 horas em minutos
    
    # Converter de volta para horas e minutos
duracao_horas = duracao_minutos // 60
duracao_minutos_resto = duracao_minutos % 60
    
    # Exibir o resultado
print(f"O jogo durou {duracao_horas} hora(s) e {duracao_minutos_resto} minutos(s)")
