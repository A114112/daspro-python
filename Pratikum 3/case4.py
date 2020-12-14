length = float(input('Panjang: '))
width = float(input('Lebar: '))
approval = input('Persetujuan [Setuju/Tidak Setuju]: ')

result = length * width

if approval.lower() == 'setuju':
    output = result / 2
elif approval.lower() == 'tidak setuju':
    output = float(0)
else:
    print('Format persetujuan tidak dikenal')
    exit()

print(result)
print(output)