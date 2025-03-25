preco = float(input("Digite o preço do produto:"))
# Verifica o desconto recebido e realiza e multiplicação do 0,07
desconto = 7 / 100 * preco
# Verifica o preço recebido e multiplica ele por 0,055
aumento = 0.055 * preco

# Printa os resultados solicitados (desconto e aumento)
print(f'Preço com desconto = R$ {preco - desconto:.2f}')
print(f'Preço com aumento = R$ {preco + aumento:.2f}')