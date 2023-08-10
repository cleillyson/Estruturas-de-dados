def buscaSequencial(lista, item): #Uma busca simples
    resultado = []  
    for c in range(len(lista)):
        if item == lista[c]:
            resultado.append(c)
    return resultado.copy()



def buscaBinaria(lista, item):
    resultado = []
    inicio = 0
    fim = len(lista) - 1
    while (inicio <= fim):
        meio = (fim + inicio) // 2
        if (lista[meio] == item):
            resultado.append(meio)
            auxiliar = 1 #Auxiliar que vai ser incrementado de 1 em 1
            while True: #Usado para ver se tem multiplos valores
                caso1 = lista[meio + auxiliar] == item #verifica se o proximo item da lista tambem é igual ao item procurado
                caso2 = lista[meio - auxiliar] == item #verifica se o item anterior da lista tambem é igual ao item procurado
                if (caso1 or caso2):
                    if (caso1):
                        resultado.append(meio + auxiliar) #caso seja igual adiciona o index no fim da lista
                    if (caso2):
                        resultado.insert(0, meio - auxiliar) #caso seja diferente adicioa o index no inicio da lista
                else:
                    return resultado.copy() #retorna uma copia da lista
                auxiliar += 1 #incremento do auxiliar
        elif (lista[meio] < item):
            inicio = meio + 1
        elif (lista[meio] > item):
            fim = meio - 1
    return resultado.copy()



if (__name__ == '__main__'):#testes
    lista_num = [
    [2, 2, 5, 8, 23, 24, 32, 44, 56, 99], #2 número que vai ser procurado
    [2, 2, 5, 8, 23, 24, 32, 44, 56, 99], #7 número que vai ser procurado
    [4, 14, 15, 19, 21, 23, 45, 78, 81, 81, 90], #81 número que vai ser procurado
    [1, 13, 21, 21, 21, 25, 36, 74] #21 número que vai ser procurado
    ]
    nume = [2, 7, 81, 21]
    for c in range(4):
        print(buscaSequencial(lista_num[c], nume[c]))
        print(buscaBinaria(lista_num[c], nume[c]))

