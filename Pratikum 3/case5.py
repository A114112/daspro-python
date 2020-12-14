total = int(input('Total belanja: '))

if(total >= 1000000):
    total -= total * 0.1
elif(total >= 500000):
    total -= total * 0.05

print(int(total))