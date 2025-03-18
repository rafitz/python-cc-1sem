segundos_totais = int(input("Digite a quantidade de segundos: "))

dias = segundos_totais // 86400
horas = (segundos_totais % 86400) // 3600
minutos = (segundos_totais % 3600) // 60
segundos = segundos_totais % 60

print(f"{segundos_totais} segundos resulta em {dias} dia(s), {horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s).")