lista_a = []
lista_b = []
soma = 0
op = -1

num_entradas_a = int(input("nº inteiro entre 0 e 5, será o número de entradas da lista A: "))
for i in range(0, num_entradas_a):
    valores_a = int(input("nº que integrarão a lista A: "))
    lista_a.append(valores_a)

num_entradas_b = int(input("nº inteiro entre 0 e 5, será o número de entradas da lista B: "))
for i in range(0, num_entradas_b):
    valores_b = int(input("nº que integrarão a lista B: "))
    lista_b.append(valores_b)

def set_vetor():
    vetor_escolhido = ""
    input_vetor = int(input("Qual lista você quer, 0 para A ou 1 para B: "))

    if input_vetor == 0:
        vetor_escolhido = lista_a
    if input_vetor == 1:
        vetor_escolhido = lista_b

    return vetor_escolhido

while op != 0:
    if op == 1:
        vetor_esc = set_vetor()
        soma = sum(vetor_esc)
        print(soma)
        op = -1

    if op == 2:
        junta_lista = (lista_a + lista_b)
        soma_geral = sum(junta_lista)
        print(soma_geral)
        op = -1

    if op == 3:
        vetor_esc = set_vetor()
        soma = sum(vetor_esc)
        media = soma / len(vetor_esc)
        print(media)
        op = -1

    if op == 4:
        junta_lista = (lista_a + lista_b)
        soma_geral = sum(junta_lista)
        media_geral = soma_geral / len(junta_lista)
        print(media_geral)
        op = -1

    if op == 5:
        vetor_esc = set_vetor()
        maior = max(int(maior) for maior in vetor_esc)
        print(maior)
        op = -1

    if op == 6:
        junta_lista = (lista_a + lista_b)
        maior = max(int(maior) for maior in junta_lista)
        print(maior)
        op = -1

    if op == 7:
        vetor_esc = set_vetor()
        maior = min(int(maior) for maior in vetor_esc)
        print(maior)
        op = -1

    if op == 8:
        junta_lista = (lista_a + lista_b)
        maior = min(int(maior) for maior in junta_lista)
        print(maior)
        op = -1

    if op == 9:
        vetor_esc = set_vetor()
        print(vetor_esc)
        op = -1

    if op == 10:
        vetor_esc = set_vetor()
        vetor_esc.reverse()
        print(vetor_esc)
        op = -1

    if op == 11:
        vetor_esc = set_vetor()
        lista_c = []
        for num in vetor_esc:
            if num % 2 == 0:
                lista_c.append(num)
        print(lista_c)
        op = -1

    if op == 12:
        vetor_esc = set_vetor()
        lista_c = []
        for num in vetor_esc:
            if num % 2 != 0:
                lista_c.append(num)
        print(lista_c)
        op = -1

    if op == 13:
        vetor_esc = set_vetor()
        lista_c = []
        for num in vetor_esc:
            if num % 2 == 1:
                lista_c.append(num)
        print(lista_c)
        op = -1


    if op == -1:
        print("Escolha qual operação quer:")
        print("0: Sair do programa")
        print("1: Exibir a soma dos valores de A ou B")
        print("2: Exibir a soma geral dos dois vetores")
        print("3: Exibir a média dos valores de A ou B")
        print("4: Exibir a média geral")
        print("5: Exibe o maior valor de A ou B")
        print("6: Exibe o maior valor geral")
        print("7: Exibe o menor valor de A ou B")
        print("8: Exibe o menor valor geral")
        print("9: Exibe todos os valores de A ou B")
        print("10: Exibe todos os valores de A ou B em ordem inversa")
        print("11: Exibe todos os valores pares de A ou B")
        print("12: Exibe todos os valores ímpares de A ou B")
        print("13: Exibe todos os valores primos de A ou B")

        op = int(input("Digite um nº inteiro de 0 a 13: "))