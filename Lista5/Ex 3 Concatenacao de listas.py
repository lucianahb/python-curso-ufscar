#Faça um programa que receba 5 valores para um lista A e 5 valores para um lista B, depois construa
#uma lista C que intercala valores de A e B. Por exemplo
#A = [5, 1, 7, 6, 12] e B = [4, 3, 9, 10, 0]
#C = [5, (1o valor de A), 4 (1o valor de B), 1(2o valor de A), 3 (2o valor de B), ...]

listaA = []
listaB = []
numEntradas = 5

for i in range(0, numEntradas):
    valoresA = int(input("Digite números que integrarão a PRIMEIRA lista: "))
    listaA.append(valoresA)

for i in range(0, numEntradas):
    valoresB = int(input("Digite números que integrarão a SEGUNDA lista: "))
    listaB.append(valoresB)

listaC = [listaA[0], listaB[0], listaA[1], listaB[1], listaA[2], listaB[2], listaA[3], listaB[3], listaA[4], listaB[4]]


print(listaA)
print(listaB)
print(listaC)

