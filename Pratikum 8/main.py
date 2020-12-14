import MyLib

def main():
    # input
    x = int(input("Masukkan angka pertama untuk aritmatika:"))
    y = int(input("Masukkan angka kedua untuk aritmatika:"))
    s = float(input("Masukkan sisi persegi (float):"))
    a,t = map(float,input("Masukkan a & t segitiga (float)(float):").split())

    #output dengan memanggil fungsi pada aritmatika untuk masukan int
    print("Hasil Penjumlahan:", MyLib.Tambah(x, y))
    print("Hasil Pengurangan:", MyLib.Kurang(x, y))
    #berikut ini contoh men-assign hasil fungsi ke variable
    hasilkali = MyLib.Kali(x, y) 
    print("Hasil Perkalian:", hasilkali)
    print("Hasil Pembagian:", MyLib.Bagi(x, y))
    
    #Luas
    print("Luas persegi:", MyLib.LuasPersegi(s))
    print("Luas segitiga:", MyLib.LuasSegitiga(a, t))

main()