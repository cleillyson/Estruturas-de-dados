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
        return escolhida.upper()
    else:
        print("Acabou as palvra")


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
            limparTerminal()
        except:
            limparTerminal()
            coresNoTerminal("# Digite uma opção valida #", "vermelho")
        else:
            if 1 <= resposta <= 3:
                return resposta
            coresNoTerminal("# Digite uma opção valida #", "vermelho")


def escolha(escolha,  podio, listaPalavras):
    match escolha:
        case 1:
            jogador = cadastroJogador()
            pontos = forca(jogador, listaPalavras)
            podio[jogador] = pontos
            return True
        case 2:
            podio = dict(sorted(podio.items()))
            ranking(podio)  
            return True 
        case 3:
            coresNoTerminal("Espero que tenha gostado :)", "azul")
            return(False)


def cadastroJogador():
    print("-- Cadastro Jogador --")
    resposta = str(input("Qual seu nome: "))
    return resposta


def forca(nome, palavras):
    erros = 0
    acertos = []
    palavraEscolhida = escolhaPalavra(palavras)
    partesCorpo = ['' for c in range(6)]
    limparTerminal()
    while erros < 6:
        cont = 0
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
        print("Adivinha: ", end='')
        for c in palavraEscolhida:
            if c in acertos:
                cont += 1
                print(c, end=" ")
            else:
                print("_", end=" ")
        if cont == len(palavraEscolhida):
            print()
            break
        print("\n")
        chute = str(input("Letra: ")).upper()
        if (chute in palavraEscolhida) and (not (chute in acertos)): 
            acertos.append(chute)
        elif not (chute in palavraEscolhida): erros += 1
        limparTerminal()
    return (6 - erros) * 100



def ranking(podio):
    coresNoTerminal("## Ranking ##", "verde")
    for k in podio:
        print(f"{k} ficou com {podio[k]}")
    


palavras = pegaPalavras('m:\\Meus projetos\\Estruturas-de-dados\\Atividades\\atv002\\palavras.txt')
continuar = True
podio = {}
while continuar:
    continuar = escolha(menu(), podio, palavras)


