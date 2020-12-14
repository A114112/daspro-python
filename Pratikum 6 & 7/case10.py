import random

balance = int(input('Masukkan saldo awal: '))
birth_date = int(input('Kapan tanggal lahir Mama: '))

if birth_date != 12:
    print('Ini penipu!')
else:
    kredit = int(input('Masukkan jumlah pulsa yang diinginkan Mama: '))

    if balance < kredit:
        print('saldo tidak cukup')
    else:
        signal = 0
        amount = 0
        while signal < 0.5:
            print('Mohon tunggu....')
            
            amount += 1
            if amount > 2:
                print('Transaksi gagal!')
                exit()

            signal = random.random()
    
        print('Transaksi', kredit, 'berhasil!')