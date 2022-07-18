def verificar_quantidade(produtos):

    nome = input('Qual o nome do produto que você quer encontrar? ')

    encontrou = False
    for produto in produtos:
        if nome == produto[0]:
            print("Produto:", nome, "Encontrado. Quantidade = ", produto[2])
            encontrou = True
            break
    if encontrou == False:
        print("Produto não encontrado")

