from lib import *

def main():
    n = int(input())
    data = [float] * n
    for i in range(n):
        data[i] = float(input())

    fts(total(data))
    fts(mean(data))
    fts(median(data))
    fts(minimum(data))
    fts(maximum(data))
    
if __name__ == "__main__":
    main()