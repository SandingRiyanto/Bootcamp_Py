# TUPLE
"""
Sama seperti list, tuple juga merupakan struktur data yang digunakan untuk menyimpan satu atau 
lebih data di dalamnya. Perbedaanya terletak pada kemampuan untuk melakukan perubahan anggota. 
Anggota pada tuple tidak dapat diubah sebagian, akan tetapi dapat diubah keseluruhan dengan memanfaatkan 
melakukan inisiasi variabel dengan nilai yang baru. Inisiasi variabel tuple dilakukan dengan menggunakan 
tanda kurung '()'.
"""
tuple_01 = (1,2,3,4)
tuple_02 = ('sanding',)
print(type(tuple_02))

# duplikasi tuple
tuple_03 = tuple_01[0:2]

# Menginisiasi Multi-Variabel Menggunakan Tuple
"""Walau kita tidak dapat melakukan perubahan pada tuple, tapi kita bisa menginisiasikan anggota tuple 
ke dalam variabel-variabel. Hanya saja variabel yang diinisiasikan harus berjumlah sama dengan anggota tuple tersebut."""
#sekarang akan kita masukkan kedalam 4 variabel dikarenakan tuple tersebut memiliki 4 anggota
a, b, c, d = tuple_01

print(a, b, c, d)
print(type(a), type(b), type(c), type(d))

# Metode pada Tuple
"""Pada tuple hanya terdapat dua metode yang dapat digunakan, count() dan index(). 
count() digunakan untuk menghitung jumlah anggota dari nilai tertentu dan index() untuk 
mengetahui lokasi anggota tersebut pertama ditemukan."""

tuple_05 = (1, 2, 2, 3, 4)

print(tuple_05.count(2))
print(tuple_05.index(2))

# Kenapa Menggunakan Tuple?
"""Dengan semua keterbatasan yang dimiliki mungkin akan timbul pertanyaan, kenapa harus tuple 
dibandingkan list. Ada tiga poin utama yang bisa dijelaskan,

1. Karena strukturnya lebih sederhana, struktur data tuple memakan memori lebih sedikit dibandingkan dengan list. 
Untuk data yang berukuran besar ini akan sangat menguntungkan.
2. Memori yang lebih sedikit juga mempengaruhi waktu proses dari tuple. Tuple memiliki waktu proses yang relatif lebih 
singkat daripada list.
3. Anggota yang tidak dapat diubah membuat tuple menjadi pilihan saat kita ingin menggunakannya untuk menyimpan suatu 
parameter yang tidak boleh berubah nilainya."""