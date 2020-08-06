#Faça um programa que receba um número n inicialmente que determina o
# número de entradas dele.
#Após receber estas n entradas seu programa deve receber um caractere
# que determina uma de três operações, que são:
#M = Media dos números inseridos
#P = quantidade de números pares
#I = quantidade de números ímpares
#Por exemplo, para um execução que insere os seguintes 5 números:
#[3, 7, 8, 5, 12]
#A opção M deve printar na tela sua média, no caso 7
#A opção P deve printar a quantidade de números pares, no caso 2
#A opção I deve printar a quantidade de números ímpares, no caso 3.

lista = []
i = 0
soma = 0

numEntradas = int(input("Digite quantos números quer na lista: "))

for i in range(0, numEntradas):
    num = int(input("Digite números que integrarão a lista: "))
    lista.append(num)

operacao = str(input("Digite M para saber a média, P para saber os pares, ou I para os impares: "))

if operacao == "M":
    for i in lista:
        soma += num
        media = (soma / len(lista))
    print(media)

#elif operacao == "P":
#   for i in range(0, num):
#      if lista[i] % 2 !== 0:

#    print(impar)

