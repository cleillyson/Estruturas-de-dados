def pegaPalavras(nome):    
    with open(nome, 'r') as arquivo:
        linha = arquivo.readlines()
    for c in range(len(linha) - 1):
        linha[c] = linha[c].replace('\n', '',-1)
    return linha.copy()

def coresNoTerminal(frase, cor, retorno=0):
    cores = {
        'reset': '\033[0m',
        'vermelho': '\033[91m',
        'verde': '\033[92m',
        'amarelo': '\033[93m',
        'azul': '\033[94m',
        'roxo': '\033[95m',
    }
    if retorno == 0:
        print(cores[cor] + frase + cores['reset'])
    else:
        return (cores[cor] + frase + cores['reset'])

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
    limparTerminal()
    while True:
        try:
            print("""## Jogo da forca ##
[1] - Play
[2] - Ranking
[3] - Sair""")
            resposta = int(input("Digite uma opção: "))
            limparTerminal()
        except:
            limparTerminal()
            coresNoTerminal("# Digite uma opção valida #", "vermelho")
        else:
            if 1 <= resposta <= 3:
                break
            coresNoTerminal("# Digite uma opção valida #", "vermelho")
    limparTerminal()
    match resposta:
        case 1:
            forca(cadastroJogador())
            return True
        case 2:
            ranking()  
            return True 
        case 3:
            coresNoTerminal("Espero que tenha gostado :)", "azul")
            return(False)


def cadastroJogador():
    print("-- Cadastro Jogador --")
    resposta = str(input("Qual seu nome: "))
    return resposta


def forca(nome):
    erros = 0
    partesCorpo = ['' for c in range(6)]
    limparTerminal()
    while erros <= 6:
        match erros:
            case 1:
                partesCorpo[0] = coresNoTerminal("O", "vermelho", 1)
            case 2:
                partesCorpo[1] = coresNoTerminal(" |", "vermelho", 1)
            case 3:
                partesCorpo[2] = coresNoTerminal("-", "vermelho", 1)
            case 4:
                partesCorpo[1] = coresNoTerminal("|", "vermelho", 1)
                partesCorpo[3] = coresNoTerminal("-", "vermelho", 1)
            case 5:
                partesCorpo[4] = coresNoTerminal("/ ", "vermelho", 1)
            case 6:
                partesCorpo[5] = coresNoTerminal("\\", "vermelho", 1)
        print(f"""### JOGO DA FORCA ###
---------
|       |            
|       | 
|       {partesCorpo[0]}
|      {partesCorpo[3]}{partesCorpo[1]}{partesCorpo[2]}
|      {partesCorpo[4]}{partesCorpo[5]}
|
-                                                                                     
""")
    coresNoTerminal(f"## Jogador: {nome} ##", "roxo")



def ranking():
    coresNoTerminal("## Top 10 ##", "verde")

              

palavras = pegaPalavras('m:\\Meus projetos\\Estruturas-de-dados\\Atividades\\atv002\\palavras.txt')
continuar = True
while continuar:
    continuar = menu()


