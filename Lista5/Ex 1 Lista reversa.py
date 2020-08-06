#Faça um programa que receba inicialmente um número n que determina o número de entradas dele.
#Após receber estas n entradas, printe eles na ordem reversa em que foram inseridas, todas na mesma
#linha.

#lista = [1, 2, 3, 4, 6]
#lista.reverse()
#print(lista)

# https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/

lista = []
i = 0

numEntradas = int(input("Digite um número inteiro entre 0 e 5, será o número de entradas: "))

for i in range(0, numEntradas):
    num = int(input("Digite números que integrarão a lista: "))
    lista.append(num)
    lista.reverse()

print(lista, end=" ")


