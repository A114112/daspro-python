money = int(input('Masukkan jumlah uang anda: '))
remains = money - 1200000

# Concert Price
regular = 500000
vip = 1000000

# Action
if remains < 0:
    print('Inputan tidak valid')
elif remains < regular:
    print('Soni tidak bisa menonton konser karena uang kurang')
elif remains >= regular and remains < vip:
    print('Soni jadi menonton konser dengan tempat duduk biasa')
else:
    print('Soni jadi menonton konser dengan tempat duduk VIP')