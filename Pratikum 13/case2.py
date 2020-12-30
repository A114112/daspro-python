val = input().split()
total = 0
for i in val:
    total += 1
    if i == 'E':
        print('TIDAK LULUS')
        exit()
print('TIDAK LULUS') if total < 5 else print('LULUS')