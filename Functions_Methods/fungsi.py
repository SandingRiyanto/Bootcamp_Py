# Getting Help
"""Jika kita ingin menghitung jumlah item suatu objek, kita bisa menggunakan fungsi ‘len’. 
Tetapi bagaimana jika kita lupa kegunaan fungsi tersebut? Maka kita bisa gunakan fungsi help."""
print(help(len))

# Mendefinisikan fungsi 
"""
def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

- Dari contoh di atas, kita membuat fungsi yang bernama least_difference, dimana fungsi ini memiliki tiga argument, yaitu a, b, c
- Fungsi dimulai dengan kata kunci ‘def’. Blok kode yang menjorok setelah tanda ‘:’ dijalankan ketika fungsi dipanggil.
- ‘return’ adalah kata kunci lain juga yang berkaitan dengan fungsi. Kata kunci ‘return’ adalah untuk menentukan apa yang akan 
di hasilkan dari fungsi tersebut.
"""

# Parameter or Arguments
# Default Parameter
def greet():
    print('Hello, Colion')

def greet(who="Colin"):
    print("Hello,", who)


""" Dari contoh di atas, kita mendefinisikan fungsi yang memiliki arguments ‘who’. Di dalam fungsi tersebut 
kita mengassign nilai “Colin” terhadap argumen ‘who’. Ini menunjukan, jika kita tidak memberikan nilai ‘who’ 
ketika kita memanggil fungsi tersebut.,maka fungsi tersebut akan memiliki nilai argument ‘who’ sebagai “Colion”. 
Berikut contohnya : """

# memanggil fungsi tanpa memberikan nilai untuk argumentt who
print(greet())  # memanggil fungsi dengan memiliki argument who 
print(greet())  # memanggil fungsi dengan memberikan argument untuk nilai who 
print(greet("Fauzan"))

# Keyword Parameter
# Keyword parameter, merupakan saat kita memanggil fungsi tersebut dengan keyword yang sudah ditentukan, hampir mirip seperti pada default.
def fungsi_04(nama):
  print(nama)

fungsi_04(nama = 'rudi')

# Arbitary Parameter
# Arbitary adalah saat kita tidak mengetahui berapa parameter yang ingin kita masukkan saat melakukan 
# pembuatan fungsi. Ada dua jenis arbitrary parameter pada fungsi,
""" 
    1. Args parameter, menggunakan satu tanda asterisk sebelum parameter. Parameter berbentuk tuple.
    2. Kwargs parameter, menggunakan dua tanda asterisk sebelum parameter. Parameter berbentuk dictionary. 
"""
#contoh fungsi args
def fungsi_05 (*nama):
  for item in nama:
    print(item)

fungsi_05('rudi','santi','mirna')

#contoh fungsi kwargs
def fungsi_06 (**nama):
  for key, value in nama.items():
    print(key, value)

fungsi_06(nama = 'rudi', umur = 18)

# Fungsi Lambda
""" Fungsi Lambda dikenal sebagai fungsi anonim, dimana fungsi ini tidak terdefinisi artinya 
kita bisa melakukan operasi menggunakan fungsi lambda tanpa mendefinisikan terlebih dahulu fungsinya.
Dalam fungsi lambda, ia bisa memiliki beberapa argumen tetapi hanya memiliki 1 ekspresi.
"""
# Persamaan umum dari fungsi lambda adalah.
# lambda argument: kode/pernyataan

kali_2 = lambda x: x * 2

print(kali_2(2))

"""Contoh di atas merupakan contoh yang kurang baik dalam penggunaan lambda, karena tujuan fungsi lambda 
adalah fungsi sementara yang tidak disimpan di dalam memori. Untuk memenuhi tujuan ini, biasanya fungsi 
lambda selain digunakan secara langsung juga digunakan dengan memanfaatkan tiga fungsi lain, yaitu Map, Filter, dan Reduce."""

"""Map
Fungsi map adalah fungsi yang digunakan untuk mengaplikasikan suatu fungsi pada semua 
anggota array atau struktur data. Terdapat dua paramater masukkan pada fungsi Map, yang pertama berisi 
fungsinya dan yang kedua berisi array/struktur datanya."""

# Contoh dari fungsi map adalah.

data = [1,2,3,4]

def kali_3(nilai):
  return nilai*3

hasil = list(map(kali_3,data))

print(hasil)

# Sekarang akan kita coba aplikasikan fungsi lambda pada fungsi map.

data = [1,2,3,4]

hasil = list(map(lambda x:x*3,data))

print(hasil)

"""Filter
Fungsi filter adalah fungsi yang digunakan untuk mengaplikasikan suatu fungsi pada 
list untuk mendapatkan nilai yang sesuai syarat. Terdapat dua paramater masukkan pada 
fungsi Filter, yang pertama berisi fungsinya dan yang kedua berisi array/struktur datanya."""

# Contoh dari fungsi filter adalah.

data = [1,2,3,4]

def cek_genap(nilai):
   if nilai % 2 == 0:
      return True
   return False
hasil = list(filter(cek_genap,data)) 
print(hasil)

# Sekarang akan kita coba aplikasikan fungsi lambda bersama dengan fungsi filter.

data = [1,2,3,4]

hasil = list(filter(lambda x:x%2 == 0,data))

print(hasil)

# Reduce

# Fungsi reduce adalah fungsi yang digunakan untuk mengaplikasikan suatu fungsi pada semua 
# anggota array atau struktur data untuk mendapatkan satu nilai di akhir.
"""Misalkan kita memiliki fungsi f(a,b) = Y yang akan diaplikasikan pada list [1,2,3,4]
Reduce akan mengambil dua nilai paling awal untuk dimasukkan pada fungsi, menjadi f(1,2) = Y
lalu nilai Y akan dimasukkan pada list menggantikan 2 nilai lama, menjadi [Y,3,4]
setelah itu diambil kembali dua nilai paling awal untuk dimasukkan pada fungsi, menjadi f(Y,3) = Y
Begitu seterusnya hingga semua nilai ter-reduce menjadi satu nilai.
Terdapat dua paramater masukkan pada fungsi reduce, yang pertama berisi fungsinya dan yang 
kedua berisi array/struktur datanya. Mulai pada python 3.xx reduce dimasukkan pada modul functools 
sehingga untuk memakainya kita perlu import modulnya terlebih dahulu
"""


from functools import reduce
data = [3,6,2,8,6,9,3]

def cek_maks(a,b):
  if a > b:
    return a
  else:
    return b

hasil  = reduce(cek_maks,data)
print(hasil)

# Sekarang akan kita coba aplikasikan fungsi lambda bersama dengan fungsi reduce.

from functools import reduce

data = [3,6,2,8,6,9,3]

hasil = reduce(lambda a,b: a if a > b else b,data)

print(hasil)