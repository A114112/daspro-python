# daspro-05102020

## Soal No. 1
Deskripsi: Mawar adalah seorang Programmer level newbie. Dia masih penasaran dengan kode program berikut ini:

```python
# Initialisasi Variabel dan Tipe Data
a = 0
b = 4.5
c = 'kata'

# Contoh Output Program
print('Latihan 1 \n')

print (type(a)) # tipe data integer
print ("Nilai bilangan bulat a adalah", a,"\n")

print (type(b)) # tipe data float
print ("Nilai bilangan decimal b adalah", b,"\n")

print (type(c)) # tipe data string
print ("Kata dari c adalah ", c,"\n")
```

<b>Pertanyaan</b>: Bantu Mawar untuk melihat output dari kode program tersebut!

<b>Catatan</b>:
Mohon untuk tidak melakukan copy paste. Copy paste hanya akan merusak cita rasa dari memprogram. Anda tidak perlu takut error. Percaya dirilah dalam mengerjakan!
Meskipun ini soal “mengetik ulang”, anda perlu memahaminya dan mungkin mendiskusikannya dengan teman atau dosen.

Penjelasan Input: -
Penjelasan Output: -

Contoh Output:
```bash
Latihan 1

<class 'int'>
Nilai bilangan bulat a adalah 0

<class 'float'>
Nilai bilangan decimal b adalah 4.5

<class 'str'>
Kata dari c adalah  kata
```

## Soal No. 2
Deskripsi: Mawar adalah seorang Programmer level newbie. Dia masih penasaran dengan kode program berikut ini:

```python
# Initialisasi Variabel dan Tipe Data
umur = 18
beratbadan = 48.3

# Contoh Output Program dengan variasi print
print("umur saya",umur,"tahun")
print("umur saya",umur)
print("umur saya"+str(umur)+"tahun")
print("umur saya %d" % (umur))
print("berat badan saya %f" % (beratbadan))
print("berat badan saya {} kilogram".format(beratbadan))
```

<b>Pertanyaan</b>: Bantu Mawar untuk melihat output dari kode program tersebut!

<b>Catatan</b>:
Mohon untuk tidak melakukan copy paste. Copy paste hanya akan merusak cita rasa dari memprogram. Anda tidak perlu takut error. Percaya dirilah dalam mengerjakan!
Meskipun ini soal “mengetik ulang”, anda perlu memahaminya dan mungkin mendiskusikannya dengan teman atau dosen.

Penjelasan Input: -
Penjelasan Output: -

Contoh Output:
```bash
umur saya 18 tahun
umur saya 18
umur saya 18 tahun
umur saya 18
berat badan saya 48.300000
berat badan saya 48.3 kilogram
```

## Soal No. 3
Deskripsi: Diberikan program python berikut:

```python
# Kamus
a = 1
b = 4

# Algoritma
print("Hasil a yang pertama:",a)
print("Hasil b yang pertama: "+str(b))

b = a  1
a -= b #ini ekuivalen dengan a = a - b

print("Hasil a yang kedua: "+str(a))
print("Hasil b yang kedua:",b)

a = b + 2
b = a * b

print("Hasil a yang ketiga: {}".format(a))
print("Hasil b yang ketiga: %f" % (b)

# berikut adalah cara menukar nilai pada dua variabel dengan assignment
c = a
a = 
b = c

print("Hasil a yang keempat: {}".format(a))
print("Hasil b yang keempat: {}".format(b))
```

Pastikan program diatas tidak ada error dan pamahi nilai-nilai yang di outputkan harus sama persis (misal nilai 2 tidak boleh 2.0).

Penjelasan Input: -
Penjelasan Output: -

Contoh Output :
```bash
Hasil a yang pertama: 1
Hasil b yang pertama: 4
Hasil a yang kedua: -1
Hasil b yang kedua: 2
Hasil a yang ketiga: 4
Hasil b yang ketiga: 8.000000
Hasil a yang keempat: 8
Hasil b yang keempat: 4
```

## Soal No. 4

<b>Deskripsi</b>: Mawar ingin mendaftarkan beasiswa. Salah satu syarat pendaftaran beasiswa tersebut adalah mengetahui nama orang tua (ayah atau ibu). Mawar lupa dengan nama orang tuanya.

<b>Pertanyaan</b>: Bantu mawar untuk menuliskan nama orang tuanya!

Nb. Tampung nama ayah atau ibu mawar pada suatu variabel dengan mekanisme input kemudian outputkan dengan print.

contoh: 
```python
a = input()
```

Penjelasan Input: Nama ayah atau ibu mawar bertipe string
Penjelasan Output: Nama ayah atau ibu mawar.

Contoh Output #1:
```bash
Eko
```

Contoh Output #2:
```bash
Joni
```
