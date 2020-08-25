def inicializaLista():
    global nomes


def adicionaNome():
    global nomes


def removeNome():
    global nomes


def buscaNome():
    global nomes


def printaLista():
    global nomes



nomes = []

while True:
    print("Opções:",
          "[0] Sair",
          "[1] Inicializar a lista",
          "[2] Adicionar nome a lista",
          "[3] Retirar nome da lista",
          "[4] Buscar nome na lista",
          "[5] Printar a lista")

    opcao = int(input("Sua opção? "))

    if opcao == 0:
        break
    if opcao == 1:
        inicializaLista()
    elif opcao == 2:
        adicionaNome()
    elif opcao == 3:
        removeNome()
    elif opcao == 4:
        if buscaNome():
            print("O nome buscado está na lista!")
        else:
            print("O nome buscado não está na lista!")
    elif opcao == 5:
        printaLista()
    else:
        print("Opção inválida!")
