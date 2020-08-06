#input de x notas, quando digitar uma nota fora do while,
# (negativa ou maior que 10), ele calcula a média

numNotas = 0
somaNotas = 0
nota = float(input("Digite a nota: "))


while nota >= 0 and nota <= 10:
    somaNotas += nota
    numNotas += 1
    nota = float(input("Digite a nota: "))

print("Sua média é:", somaNotas/numNotas)
