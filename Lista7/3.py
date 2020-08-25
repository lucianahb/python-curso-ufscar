def collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


n = int(input("Digite o primeiro número da sequência: "))
print(n)

while n != 1:
    n = collatz(n)
    print(int(n))
