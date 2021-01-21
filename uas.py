# Kamus Global
# Keadaan Awal: dataNama merupakan variabel global untuk list nama
# dataBatasDaya merupakan variabel global untuk list daya kwH saat ini
# dataPulsa merupakan variabel global untuk list pulsa yang ingin dibeli

dataNama = []
dataBatasDaya = []
dataPulsa = []


def SimpanNama(nama):
    # Merupakan prosedur untuk menyimpan setiap nama kedalam list dataNama
    global dataNama
    dataNama.append(nama)

def SimpanBatasDaya(daya):
    # Merupakan prosedur untuk menyimpan setiap daya kedalam list dataBatasDaya
    # Isi dibawah ini 2 baris, dengan nilai 5
    global dataBatasDaya
    dataBatasDaya.append(daya)

def SimpanPembelianPulsa(pulsa):
    # Merupakan prosedur untuk menyimpan setiap pulsa kedalam list dataPulsa
    # Isi dibawah ini 2 baris, dengan nilai 5
    global dataPulsa
    dataPulsa.append(pulsa)

def CekPenerimaBantuanListrik(daya, pulsa):
    # Merupakan fungsi untuk mengecek apakah mendapatkan bantuan atau tidak
    # Keadaan awal: daya dan pulsa setiap orang
    # Keadaan akhir: fungsi ini akan mengembalikan boolean True atau False
    # Fungsi ini akan mengembalikan nilai True jika syarat memenuhi
    # dan false jika tidak memenuhi
    # Cek deskripsi soal untuk syarat Penerima bantuan listrik
    # Isi dibawah ini, Bisa 4 sampai 8 baris kode, nilai 20
    if daya >= 450 and daya <= 900 and pulsa >= 10000 and pulsa <= 50000:
        return True
    elif daya > 900 and pulsa >= 10000 and pulsa <= 50000:
        return True
    else:
        return False

def HitungTotalPembayaran(daya,pulsa):
    # Keadaan awal: daya dan pulsa
    # Keadaan akhir: fungsi ini mengembalikan total biaya yang harus dibayar oleh setiap orang
    # Pertama cek bantuan apakah daya dan pulsanya memenuhi kriteria
    # Jika memenuhi atau pulsa yang dibeli minimal 10000 maka total bayar menjadi gratis
    # Jika tidak, total bayar terdiri dari pulsa ditambah 3000
    # Isi dibawah ini, Bisa 5 sampai 10 baris kode, nilai 20
    if CekPenerimaBantuanListrik(daya, pulsa) == False:
        if daya > 0 and pulsa > 0:
            return pulsa + 3000
        else:
            return 0
    else:
        return 0

def DisplayPembayaran():
    # Berikut ada prosedur untuk menampilkan Nama, Batas daya dan total Bayar
    # Ambil global variabel dan panggil fungsi HitungTotalPembayaran untuk setiap orang
    global dataNama 
    global dataBatasDaya
    global dataPulsa

    for i in range(len(dataNama)):
        print("Nama: ",dataNama[i],"Batas Daya: ",dataBatasDaya[i], "Total Bayar: ",HitungTotalPembayaran(dataBatasDaya[i],dataPulsa[i]))

def main():
    # Buat inputan oleh user sebanyak n orang yang akan membayar
    n = int(input())
    i = 0

    # Isikan data nama, daya, dan pulsa yang dibeli dan simpan pada variabel global
    while i<n:
        nama = input()
        daya = int(input())
        pulsa = int(input())

        SimpanNama(nama)
        SimpanBatasDaya(daya)
        SimpanPembelianPulsa(pulsa)

        i=i+1
    # Tampilkan data semua orang dengan detil pembayaran yang ada
    DisplayPembayaran()    

if __name__ == "__main__":
    main()