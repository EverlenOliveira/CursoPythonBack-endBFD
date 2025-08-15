#calculadora de índice de massa corporal
peso = float(input("Qual o seu peso (kg)?: "))
altura = float(input("Qual a sua altura(m)?: "))

imc = peso/(altura**2)

print(f"Seu IMC é: {imc:.2f}")
