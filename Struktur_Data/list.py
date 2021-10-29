# LIST
# List adalah salah satu tipe data untuk mengoleksikan data di python
# Sifat List: 
""" 1. List berisi koleksi nilai/data.
    2. List bisa berisi tipe data apapun dan tidak harus semua data berisi tipe data yang sama.
    3. List bisa berubah
"""
# Contoh
nilai1 = 90
nilai2 = 78
nilai3 = 88
# simpan dalam List
nilai_ipa = [nilai1, nilai2, nilai3]
print(nilai_ipa) # [90, 78, 88]

# Membuat List
suhu_kota = ['Banyumas', 30, 'Cilacap', 32, 'Kebumen', 29]
print(suhu_kota)

nama_buah = ['apel', 'jeruk', 'manggis']

# membuat list dalam list
campur_list = [suhu_kota, nama_buah]
print(campur_list) # [['Banyumas', 30, 'Cilacap', 32, 'Kebumen', 29], ['apel', 'jeruk', 'manggis']]

"""
Setelah kita bisa membuat data sederhana dengan list. Sekarang kita akan belajar bagaimana caranya mengakses data dalam list. 
Untuk mengakses data dalam list, python menggunakan sesuatu yang bernama index. Index menunjukan posisi suatu data di dalam list, 
dan python memulai index dari 0. Perlu diketahui sebelumnya bahwa ada 2 teknik untuk mengakses data di dalam list. Pertama dengan 
subsetting list, kedua dengan slicing list. Mari kita lihat contohnya :
"""
no_rumah = [
    20,
    12,
    33,
    3,
    11,
    89
]

# kita akan mencetak nomor rumah 33 (berada di index ke 2)
print(no_rumah[2])
print(no_rumah[-1])


# Slicinglist
# Mengambil data dengan index 0, 1, 2, 3
print(no_rumah[:4]) 

# Mengambil data dengan index 2, 3, 4
print(no_rumah[2:5])

# MANIPULASI LIST
# mengubah value
no_rumah[2] = 100
print(no_rumah)

# list baru
nama_hewan = ["sapi", "kerbau", "semut", "kodok", "ular", "buaya"]
# ubah value pd index ke 3 & 4
nama_hewan[3:5] = ["macan", "singa"]
print(nama_hewan)

# menambah value list dengan tanda "+"
nama_hewan = nama_hewan + ["gajah"]
print(nama_hewan)

# menambahkan elemen dlm List dg fungsi append() dan insert()
wayang = ["arjuna", "kresna", "rama"]
wayang.append("bima") #akan berada di index paling akhir (list yg baru)
wayang.insert(3, "shinta")

# hapus
del(wayang[0])
print(wayang)

# Some Function in List (len -> panjang elemen list)
print(len(wayang))
print(sorted(wayang))

angka = [1,3,2,4,2]
print(sum(angka))

# copy
laptop = ["acer","lenovo","asus"]
laptop2 = laptop.copy()
print(laptop2)