#URI Online Judge | 1065 Pares entre Cinco Números

#cont = cont + 1 === cont +=1

cont = 0

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
d = int(input("Digite o valor de D: "))
e = int(input("Digite o valor de E: "))

if a % 2 == 0:
    cont +=1

if b % 2 == 0:
    cont +=1

if c % 2 == 0:
    cont +=1

if d % 2 == 0:
    cont +=1

if e % 2 == 0:
    cont +=1

print (cont, "valor(es) par(es)")