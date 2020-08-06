n = int(input("Digite um número inteiro entre 0 e 10, será o número de testes: "))

for i in range(0, n):
    num = int(input("Digite um número para verificar se é primo: "))
    a = 0
    b = 1
    while b <= num:
        if num % b == 0:
            a = a + 1
        b = b + 1
    if a > 2:
        print('{}: primo'.format(num))
    else:
        print('{}: não é primo'.format(num))