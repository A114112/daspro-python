year = int(input('Masukkan nomor tahun motor anda: '))

if year >= 2020:
    print('Motor sudah tahun 2020')
else:
    cost = (2020 - year) * 2000000
    print(cost)