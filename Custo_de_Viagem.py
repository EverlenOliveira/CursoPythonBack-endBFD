print("----------CALCULADORA DE CUSTO DE VIAGEM----------")

distancia = float(input("Qual a distância da viagem em km?: "))
consumo = float(input("Qual o consumo do carro ou moto em Km/l?: "))
combustivel = float(input("Qual o valor do combustível em R$?: "))

custo_total = (distancia / consumo) * combustivel

print(f"O custo total da viagem será de R$: {custo_total:.2f}")