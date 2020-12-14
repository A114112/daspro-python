balance = int(input('Saldo awal: '))

while balance > 0:
    kredit = int(input('Pengeluaran soni hari ini (isikan -1 untuk keluar):'))

    if kredit == -1:
        print('sisa saldo', balance)
        exit()
    
    balance -= kredit

print('saldo tidak cukup')
print('sisa saldo', balance + kredit)