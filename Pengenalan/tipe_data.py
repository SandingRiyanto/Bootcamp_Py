# macam-macam tipe data (python)
# 1. Integer
x = 10
print(x)
print(type(x))

# 2. Float / double
y = 9.7
print(y)
print(type(y))

# 3. String, value diapit oleh tanda petik satu atau petik dua (sama saja)
s = "Sanding Riyanto"
print(s)
print(type(s))

# modifikasi String dengan salah satu fungsi, yg bernama: capitalize() -> merubah huruf depan jadi Kapital/Besar
kata = "aku suka wayang kulit"
new_kata = kata.capitalize()
print(new_kata)

# 4. Boolean (T/F)
a = True
b = False
print(a)
print(type(a))

#Printing
# Dalam Python, ada beberapa cara yang bisa digunakan untuk mencetak sebuah string, sebagai contoh:
salam = "Assalamualaikum"
objek = "Riyan"
ucapan = salam + " " + objek
print(ucapan)

# contoh lain:
nama = "Vita"
umur = 21
print("Hai, namaku " + nama + ". Umurku " + str(umur) + "tahun")
# str() berfungsi merubah tipe data Int ke Str

# Old Style
print('Hello i am %s i am %d years old' % (nama, umur))

# 'New Style' string formatting
print('Hello i am {0} i am {1} years old'.format(nama, umur))

# String interpolation
print(f'Hello i am {nama} i am {umur} years old')

# Operasi Aritmatika
A = 10
B = 2
C = A + B
D = A / B
print(C,D)
print(type(D)) #tipe data hasil pembagian (D) jenisnya Float, krn default hasil pembagian pd Python spt itu, utk merubahnya bisa menggunakan:

D1 = int(A/B)

# merubah integer menjadi string
number = 100000
number = str(number)
print(number)
print(type(number))