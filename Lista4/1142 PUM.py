n = int(input("Digite um valor inteiro: "))
x = 1

for i in range(1, n + 1):
    print('{} {} {} PUM'.format(x, x+1, x+2))
    x = x + 4