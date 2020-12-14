x = input('DNA Ayah: ')
y = input('DNA Anak: ')
p = sum(x[i:i+3] == y[i:i+3] for i in range(0, len(x), 3)) / (len(x) // 3) * 100
print(p)
if p >= 75:
    print('dia ayahku')
else:
    print('dia bukan ayahku')