def cadastrar_produto():
    
    
    nome = input('Digite o produto a ser cadastradado: ')
    
    preco = float(input("Digite o preço do produto: "))
    
    quantidade = float(input("Digite a quantidade do produto: "))
    
    return [nome, preco, quantidade]
    
    