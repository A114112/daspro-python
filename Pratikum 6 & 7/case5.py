t = int(input())
if t > 1:
    for i in range(2, t):
        if t % i == 0:
            print('Bukan Bilangan Prima')
            break
    else:
        print('Bilangan Prima')
else:
    print('Bukan Bilangan Prima')