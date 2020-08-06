i = 0
cont = 0
qtde = int(input("Digite quantas vezes quer analisar se os números são pares: "))

while i < qtde:
    num = int(input("Digite um número para ver se é par: "))
    if num % 2 == 0:
        cont = cont + 1

    i += 1

print(cont, "valor(es) par(es)")