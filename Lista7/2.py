def ehPar(n):
    if n % 2 == 0:
        return True
    else:
        return False


numero = int(input("Digite sua opção: "))

if ehPar(numero):
    print(numero, "é par!")
else:
    print(numero, "é ímpar!")