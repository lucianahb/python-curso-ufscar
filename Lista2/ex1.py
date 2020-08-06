print("Digite o valor de A")
a = input()
print("Digite o valor de B")
b = input()
print("Digite o valor de C")
c = input()
print("Digite o valor de D")
d = input()

a = int(a)
b = int(b)
c = int(c)
d = int(d)

if(d > c and d > a) and ((c+d) > (a + b)) and (c > 0) and (d > 0) and (a % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
