import cadastro_produtos
import verificar_quant
import listar_produtos
import vender_produtos
import reposicao
import historico_vendas

def escolher_operacao():
    
    print("*********************************")
    print("******* Sistema de Vendas *******")
    print("*********************************")

    produtos = []
    vendas = []

    while (True):
        print("(1) Cadastrar Produtos, (2) Verificar Quantidade, (3) Listar Produtos, (4) Vender Produtos, (5) Reposição, (6) Histórico de Vendas, (7) Listar Produtos, (0) Sair -->>")

        operacao = int(input("Qual operação deseja realizar? "))

        if  (operacao == 1):
            print("\n\nCADASTRO DE PRODUTOS:\n\n")
            produto = cadastro_produtos.cadastrar_produto()
            produtos.append(produto)
        elif(operacao == 2):
            print("\n\nVERIFICAR QUANTIDADE:\n\n")
            verificar_quant.verificar_quantidade(produtos)
        elif(operacao == 3):
            print("\n\nLISTAR PRODUTOS:\n\n")
            listar_produtos.listar_produtos(produtos)
        elif(operacao == 4):
            print("\n\nVENDER PRODUTOS:\n\n")
            produtos, retorno = vender_produtos.vender_produtos(produtos)
            if retorno:
                vendas.append(retorno)
                print(vendas)
        elif(operacao == 5):
            print("\n\nREPOSICAO DE PRODUTOS:\n\n")
            reposicao.reposicao_produtos(produtos)
        elif(operacao == 6):
            print("\n\nHISTÓRICO DE VENDAS:\n\n")
            historico_vendas.historico_vendas(produtos)
        elif(operacao == 7):
            print("\n\nLISTAR PRODUTOS:\n\n")
            print(produtos)
        else:
            break


if(__name__ == "__main__"):
    escolher_operacao()
