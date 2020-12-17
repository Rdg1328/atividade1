lista_produtos = []
lista_precos = []
lista_quantidades = []


def inserirProdutos():
    nome = str(input('Produto: ')).upper()
    return lista_produtos.append(nome)


def inserirPreco():
    preco = float(input('Preço: '))
    return lista_precos.append(preco)


def inserirQuantidade():
    qtde = int(input('Quantidade: '))
    return lista_quantidades.append(qtde)


def relatorioProdutos():
    for ind, produto in enumerate(lista_produtos):
        print(produto)


def cadastrarProduto():
    inserirProdutos()
    inserirPreco()
    inserirQuantidade()


def listarProdutos():
    print("Lista de produtos:")
    print(" Produto                       preço            quantidade")

    for i, produto in enumerate(lista_produtos):
        print("{0} {1} {2}"
            .format(
            str(produto).ljust(25),
            str(lista_precos[i]).center(13),
            str(lista_quantidades[i]).center(23)))



def excluirProduto():
    relatorioProdutos()
    produto = str(input('Selecione o produto: ')).upper()
    if produto in lista_produtos:
        i = lista_produtos.index(produto)
        lista_produtos.pop(i)
        lista_precos.pop(i)
        lista_quantidades.pop(i)
        input('Produto excluido. [Enter]')
    else:
        input('Produto inexistente. [Enter]')



menu = '''
Menu
0- Finalizar
1- Cadastrar Produto
2- Listar Produtos
3- Excluir Produto

Escolha: '''


escolha = 0
while True:
    escolha = input(menu)
    if escolha == '0':
        break
    elif escolha == '1':
        cadastrarProduto()
    elif escolha == '2':
        listarProdutos()
    elif escolha == '3':
        excluirProduto()
    else:
        input('Opção inválida! [Enter]')
