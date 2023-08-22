def pegaPalavras(nome):    
    with open(nome, 'r') as arquivo:
        linha = arquivo.readlines()
    for c in range(len(linha) - 1):
        linha[c] = linha[c].replace('\n', '',-1)
    return linha.copy()


def escolhaPalavra(lista):
    from random import choice
    if lista:
        escolhida = choice(lista)
        lista.remove(escolhida)
        return escolhida
    else:
        print("Acabou as palvra")


def limparTerminal():
    from os import system
    system('cls')


def menu():
    while True:
        try:
            print("""## Jogo da forca ##
[1] - Play
[2] - Ranking
[3] - Sair""")
            resposta = int(input("Digite uma opção: "))
        except:
            limparTerminal()
            print("\033[91m" + "# Digite uma opção valida #", "\033[0m") #\033[91m faz a corno terminal ficar vermelha e o [0m coloca na cor padrão
        else:
            limparTerminal()
            return resposta


def cadastroJogador():
    print("-- Cadastro Jogador --")
    resposta = str(input("Qual seu nome: "))
    return resposta


def ranking():
    return 0




limparTerminal()
palavras = pegaPalavras('m:\\Meus projetos\\Estruturas-de-dados\\Atividades\\atv002\\palavras.txt')
opcaoEscolhida =  menu()
