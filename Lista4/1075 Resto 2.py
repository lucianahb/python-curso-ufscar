num = int(input("Digite um número: "))

for i in range(1, 10001):
    if i % num == 2:
        print(i)