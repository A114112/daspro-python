def main():
    result = []
    while True:
        put = int(input())
        if put == 0:
            break
        result.append(put)
    print(result)

if __name__ == "__main__":
    main()