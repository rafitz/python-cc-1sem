entrada = input("Digite o número: ")

if entrada.isdigit():
    x = int(entrada)
    print(type(x))
    print("Você digitou um número inteiro válido!")
else:
    print("Erro: O valor digitado não é um número inteiro!")