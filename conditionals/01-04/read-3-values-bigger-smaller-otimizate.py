valor1 = int(input("Digite o primeiro valor inteiro: "))
valor2 = int(input("Digite o segundo valor inteiro: "))
valor3 = int(input("Digite o terceiro valor inteiro: "))

# Encontrar o maior valor
maior = valor1
if valor2 > maior:
    maior = valor2
if valor3 > maior:
    maior = valor3

# Encontrar o menor valor
menor = valor1
if valor2 < menor:
    menor = valor2
if valor3 < menor:
    menor = valor3

print(f"O menor valor é: {menor}")
print(f"O maior valor é: {maior}")