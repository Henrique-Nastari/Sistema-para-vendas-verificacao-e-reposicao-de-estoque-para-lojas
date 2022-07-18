
def vender_produtos(produtos):

    data = input("Digite a data da compra: ")

    nome = input("Digite o produto a ser vendido: ")

    quantidade = int(input("Digite a quantia de produtos a serem adquiridos: "))

    for produto in produtos:
        if nome == produto[0]:
            print("Produto vendido no dia ",data,"com valor igual a " , produto[1] * quantidade)
            produto[2] = produto[2] - quantidade
            return produtos, [data,nome,quantidade,produto[1] * quantidade]

    print("Produto não encontrado!")
    return produtos, False

