x = input('DNA Ayah: ')
y = input('DNA Anak: ')
p = sum(x[i:i+3] == y[i:i+3] for i in range(0, len(x), 3)) / (len(x) // 3) * 100
print(p)
print('dia ayahku') if p >= 75 else print('dia bukan ayahku')