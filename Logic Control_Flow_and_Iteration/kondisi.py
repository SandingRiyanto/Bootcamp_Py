# KONDISIONAL
"""
Percabangan digunakan untuk membuat sebuah kode yang cara berjalannya kode ditentukan oleh 
pengetesan pernyataan bersyarat. Sama seperti fungsi pengecekan pada bolean, pada percabangan 
ini juga dilakukan dengan memanfaatkan operator pembanding. Ada tiga jenis pernyataan yang akan 
kita pelajari pada kesempatan kali ini, yaitu pernyataan if, pernyataan if - else, dan pernyataan if - elif - else.

Satu hal yang harus diingat dalam pelaksanaan percabangan adalah pentingnya indentasi.Python memiliki
sebuah tipe data bernama boolean, yang hanya memiliki 2 nilai, yaitu True atau False.
"""
# Pernyataan If
"""Pernyataan if digunakan jika kita hanya ingin menguji satu pernyataan sebagai syarat jika kode kita ingin dijalankan.
Persamaan umum dari pernyataan if adalah"""
nilai = 9
if nilai >= 8 :
    print('lulus')

nilai = 7
if nilai >= 8 :
    print('lulus')
# tidak akan muncul apa-apa

# Pernyataan If - Else
nilai = 6
if nilai >= 8:
  print('lulus')
else:
  print('tidak lulus')

# Pernyataan If - Elif - Else
"""Pernyataan if-elif-else digunakan jika kita hanya memiliki banyak syarat yang ingin diuji 
secara berurutan. Jadi jika syarat pertama tidak terpenuhi dia akan menguji syarat kedua, dan 
begitu seterusnya hingga bertemu dengan else."""
#contoh1
usia = 6
if usia < 14:
  print('anak-anak')
elif nilai < 20:
  print('remaja')
else:
  print('dewasa')

#contoh2
usia = 17
if usia < 14:
  print('anak-anak')
elif nilai < 20:
  print('remaja')
else:
  print('dewasa')

