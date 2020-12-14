def toList(val):
    return [val[i:i+3] for i in range(0, len(val), 3)]

def percentageDna(x, y):
    x = toList(x)
    y = toList(y)
    l = len(x) if len(x) <= len(y) else len(y)
    
    t = 0
    for i in range(l):
        if x[i] == y[i]:
            t += 1
    
    return t / l * 100

def main():
    x = input('DNA Ayah: ')
    y = input('DNA Anak: ')
    
    p = percentageDna(x, y)
    print(p)
    
    if p >= 75:
        print('dia ayahku')
    else:
        print('dia bukan ayahku')

if __name__ == "__main__":
    main()