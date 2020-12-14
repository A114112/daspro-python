import statistics

amount = 0
data = []
for i in range(int(input())):
    x = int(input('Nilai mahasiswa'))
    data.append(x)

print('Jumlah nilai:', sum(data))
print('Rata-rata nilai:', statistics.mean(data))
print('Nilai Max:', max(data))
print('Nilai Min:', min(data))