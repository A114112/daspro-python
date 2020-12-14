price_list = [int(input(f'Harga barang ke-{i+1}: ')) for i in range(int(input('Jumlah harga barang yang akan dinput: ')))]
voucher = int(input('Jenis Voucher: '))

total = sum(price_list)
shipping = total * 0.05

if voucher == 1:
    if total >= 100000 and total < 200000:
        shipping = 0
    elif total >= 200000:
        shipping = total * 0.02
elif voucher == 2:
    if total >= 150000 and total <= 1000000:
        total -= total * 0.2
    elif total > 1000000:
        total -= total * 0.05

print('Total ongkir', int(shipping))
print('Total yang dibayar', int(total + shipping))