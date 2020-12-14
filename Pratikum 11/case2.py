def average(val):
    s = sum(val)
    if s % 2 == 0:
        r = sum(val) / len(val)
    else:
        r = sum(val) // len(val)
    return r

def median(val):
    items = len(val) 
    val.sort() 
    if items % 2 == 0: 
        x = val[items // 2] 
        y = val[items // 2 - 1] 
        median = (x + y) / 2
    else: 
        median = val[items // 2] 
    return median

def main():
    val = list(map(int, input().split(' ')))
    #list
    print(val)
    # Jumlah
    print(sum(val))
    # Rata - rata
    print(average(val))
    # Median
    print(median(val))
    # Min
    print(min(val))
    #Max
    print(max(val))

if __name__ == "__main__":
    main()