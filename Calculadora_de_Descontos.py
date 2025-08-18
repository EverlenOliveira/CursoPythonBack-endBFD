print("----------CALCULADORA DE DESCONTOS----------")
preco = float(input("Qual o preço do produto?: "))
porcentagem = float(input("Qual a porcentagem de desconto?: "))

valor_desconto = (preco * porcentagem)/100
preco_final = preco - valor_desconto

print("O valor de desconto é: ")
print(f"O preço final do produto é: {preco_final:.2f}")