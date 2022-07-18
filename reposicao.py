def reposicao_produtos(produtos):
    nome = input("Digite o nome do produto a repor: ")
    quantidade = int(input("Quantidade de produtos: "))
    achou = False
    for produto in produtos:
        if nome == produto[0]:
            produto[2] = quantidade + produto[2]
            print("Resposição feita!")
            achou = True
            break
    if achou == False:
        print("Produto não encontrado")
