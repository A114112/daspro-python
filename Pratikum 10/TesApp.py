def panjangString(s):
    return len(s)

def cariKarakter(s,c):
    print('ada') if s in c else print('tidak ada')

def frekuensiKarakter(s,c):
    return sum(s == i for i in c)

def cekPalindrom(s):
    return s == s[::-1]

def main():
    data = "balonku ada lima, rupa-rupa warnanya"
    c1 = input()
    c2 = input()
    p = input()
    print(panjangString(data))
    cariKarakter(c1,data)
    print(frekuensiKarakter(c2,data))
    if cekPalindrom(p):
        print("palindrom")
    else:
        print("bukan palindrom")  
    print(frekuensiKarakter("aku sayang kamu","a"))

if __name__ == "__main__":
    main()
