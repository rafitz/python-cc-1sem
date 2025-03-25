from math import sqrt
ca = float(input('Entre com o valor do cateto oposto: '))
cb = float(input('Entre com o valor do cateto adjacente: '))

h = sqrt(ca ** 2 + cb ** 2)

print(f"A hipotenusa do triânguo retângulo é {h}")