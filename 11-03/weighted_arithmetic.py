n1 = float(input("Digite a nota 1:"))
p1 = int(input("Digite o peso da nota 1:"))
n2 = float(input("Digite a nota 2:"))
p2 = int(input("Digite o peso da nota 2:"))

mp = (n1 * p1 + n2 * p2) / (p1 + p2)

print(f'Media Ponderada = {mp:.1f}')