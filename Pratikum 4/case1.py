number = int(input('Masukkan Nomor: '))

if number == 0:
    print('0: Tidak Valid')
    exit()

if number % 2 == 0:
    print('Type A')
else:
    print('Type B')