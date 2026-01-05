# 1
soz = input("So'z kiriting: ")

if soz == soz[::-1]:
    print("Bu so'z palindrom")
else:
    print("Bu so'z palindrom emas")

# 2
n = int(input("N ni kirit: "))

a = 0
b = 1

if n == 1:
    print(a)
else:
    print(a, b, end=" ")
    for i in range(n - 2):
        c = a + b
        print(c, end=" ")
        a = b
        b = c

# 3
n = int(input("N ni kirit: "))

for son in range(2, n + 1):
    tub = True
    for i in range(2, son):
        if son % i == 0:
            tub = False
            break
    if tub:
        print(son, end=" ")

# 4
raqamlar = input("Raqamlarni bo'sh joy bilan kiriting: ").split()

raqamlar = [int(x) for x in raqamlar]

raqamlar.sort()

print("Saralangan ro'yxat:", raqamlar)

# 5
raqamlar = [1, 2, 2, 3, 3, 3, 4]

eng_kop = raqamlar[0]
maks_soni = raqamlar.count(raqamlar[0])

for son in raqamlar:
    if raqamlar.count(son) > maks_soni:
        maks_soni = raqamlar.count(son)
        eng_kop = son

print("Eng ko'p uchraydigan element:", eng_kop)
