amount = int(input())
product = 0
for i in range(amount):
    product += int(input())

i = product
n = 0
while i > 100000:
    n += 1
    i -= 100000

ongkir = n * 10000
total = product
if product >= 2000000:
    ongkir *= 0.5
    total = total * 0.5 + ongkir
elif product >= 100000:
    total += ongkir - 15000

print(ongkir)
print(total)