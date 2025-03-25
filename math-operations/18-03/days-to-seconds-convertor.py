d = int(input("Digite quantidade de dias: "))
h = int(input("Digite quantidade de horas: "))
m = int(input("Digite quantidade de minutos: "))
s = int(input("Digite quantidade de segundos: "))

ds = d * 24 * 60 * 60
hs = h * 60 * 60
ms = m * 60 + s

print(ds + hs + ms)