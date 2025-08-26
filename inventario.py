print("----------CONTROLE DE INVENTÁRIO DE SUPERMERCADO----------")

inventario = []

while True:
    print('''Suas opções:
          [1]Adicionar Item
          [2]Remover Item
          [3]Listar Itens
          [0]Sair''')
    
    opcao = input("Escolha a opção que deseja realizar: ")
    
    if not opcao.isdigit():
        print("Entrada inválida! Digite apenas números de acordo com os disponíveis(0, 1, 2, 3)")
        continue
    
    if opcao == "1":
        nome = input("Qual o nome do item?: ")
        quantidade = int(input("Quantos itens deseja adicionar?: "))
        item = {"nome": nome, "quantidade": quantidade}
        inventario.append(item)
        print(f"{quantidade} unidade(s) de {nome} adicionada(s).")
        
    elif opcao == "2":
        nome = input("Qual o item que deseja remover?: ")
        encontrado = False
        for item in inventario:
            if item["nome"].lower() == nome.lower():
                encontrado = True
                print(f"O produto {item['nome']} tem {item['quantidade']} unidade(s).")
                qdt_remover = int(input("Quantas unidades deseja remover?: "))
                if qdt_remover >= item ["quantidade"]:
                    inventario.remove(item)
                    print(f"Todas as unidades de {nome} foram removidas!")
                else:
                    item["quantidade"] -= qdt_remover
                    print(f"O {qdt_remover} unidade(s) de {nome} removida(s) do iventário! Restam {item['quantidade']}.")
                break
        if not encontrado:
            print("Produto não encontrado.")      
    
    elif opcao == "3":
        if len(inventario) == 0:
            print("Inventáro vazio.")
        else:
            print("\n--- Itens no Inventário ---")
            for item in inventario:
                print(f"{item['nome']} - {item['quantidade']} unidade(s).")        
        
    elif opcao == "0":
        print("Fechando Inventário...")
        break
    else: 
        print("Opção inválida!Tente novamente.")