a=int(input("Введите число:"))
b=int(input("Введите число:"))
if a%2==0:
    print(sum(range(a, b+1, 2)))
else:
    print(sum(range(a+1, b+1, 2)))