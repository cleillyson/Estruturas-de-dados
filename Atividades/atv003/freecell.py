from tkinter import *
from PIL import Image, ImageTk
from os.path import abspath, basename
caminho = abspath(__file__).replace(basename(__file__), "")
# --------- Janela Principal
root = Tk()
root.title("Freecell - DCC")
largura = 1100
altura = 700
posX = int(root.winfo_screenwidth() / 2 - largura / 2)
posY = int(root.winfo_screenheight() / 2 - altura / 2 - altura / 100)
root.geometry(f"{largura}x{altura}+{posX}+{posY}")
root.resizable(False, False)
root.iconbitmap(caminho + "imagens/imgs/python.ico")
root.configure(background="green")

# --------- Classes

class card():
    def __init__(self, path, name, root) -> None:
        self.caminho = path + name + ".png"
        self.nome = name
        self.naipe = self.nome.split("_")[2]
        self.numero = self.nome.split("_")[0]
        self.cor = "vermelho" if (self.naipe in ["ouros", "copas"]) else "preto"
        self.imagem = ImageTk.PhotoImage(Image.open(self.caminho)) #Define a imagem da carta
        self.botao = Button(root, image=self.imagem, borderwidth=0)

    def coloca(self, positionX, positionY) -> None:
        self.botao.lift()
        self.botao.place(x=positionX, y=positionY)

class dack():
    def __init__(self) -> None:
        self.monte = []
        
    def inserir(self, card):
        self.monte.append(card)

    def embaralhar(self):
        from random import shuffle
        shuffle(self.monte)

    def pegaCartas(self, inicio, fim):
        return self.monte[inicio:fim]

# --------- Funções
def cardClicked(card):
    pass

def criarColunas(baralho, colunas):
    for c in range(2):
        for l in range(4):
            suporte = 7*l + 28*c - l*c
            colunas[c * 4 + l] = baralho.pegaCartas(suporte, suporte + 7 - c)
    
    colunasX = 30
    colunasY = 200
    colunasEspacamentoX = 125
    colunasEspacamentoY = 40

    for x in range(len(colunas)):
        for y in range(len(colunas[x])):
            colunas[x][y].coloca(colunasX + colunasEspacamentoX * x, colunasY + colunasEspacamentoY * y)

def embaralharJogo(baralho):
    global colunas
    baralho.embaralhar()
    criarColunas(baralho, colunas)

# --------- Ciando baralho
naipes = ["copas", "ouros", "paus", "espadas"]
baralho = dack()
for nai in naipes:
    for num in range(1, 14):
        baralho.inserir(card(caminho + "imagens\\cards\\",f"{num}_of_{nai}", root))
baralho.embaralhar()

# --------- Criando colunas
colunas =[[] for c in range(8)]
criarColunas(baralho, colunas)

# --------- Codigo
botao = Button(root, text="Embaralhar", command=lambda :embaralharJogo(baralho))
botao.place(x=0, y=0)
root.mainloop()