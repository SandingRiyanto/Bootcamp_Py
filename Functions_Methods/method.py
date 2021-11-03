# METHOD
"""Method adalah salah satu hal yang sangat penting dalam python. memahami method akan membuat kita 
semakin pro dalam menggunakan bahasa python.
Sederhananya, method adalah suatu fungsi yang dimiliki oleh suatu object.
Apa itu object? Segala yang ada di python adalah object. Contohnya kita membuat variabel bertipe 
string, bertipe list, bertipe numeric dan lain sebagainya, itu semua adalah object, dan setiap object 
memiki fungsi yang hanya bisa digunakan oleh object tersebut. Sebagai contoh, object string memiliki 
method uppercase, dimana method upper ini tidak bisa digunakan oleh object lain seperti list. Tapi 
list juga memiliki fungsi seperti index, yang dimana fungsi index ini tidak bisa digunakan oleh data 
dengan tipe objek lain seperti string contohnya. Jadi intinya, fungsi yang dimiliki oleh suatu object 
dinamakan method. Berikut adalah contohnya :
"""
# membuat object string
huruf_kecil = 'huruf kecil'
print(huruf_kecil.upper())

# mendifinisikan object list
keluarga_ucup = ['mamah', 'papah', 'ucup', 'adek ucup', 'kaka ucup']
# memanggil method yang dimiliki oleh list
print(keluarga_ucup.index('ucup'))

## jika kita menggunakan method upper ketika object list, maka akan error
## karena method tersebut bukan dimiliki object list
# print(keluarga_ucup.upper())
#AttributeError: 'list' object has no attribute 'upper'

# Menggunakan External Library
"""Untuk menggunakan external library di kode python kita, kita terlebih dahulu memanggil library 
tersebut menggunakan suatu keyword yaitu ‘import’. Berikut adalah contoh memanggil dan menggunakan external library di python :"""
r = 0.43
import math
phi = math.pi
keliling = 2*phi*r
luas = phi*r*r
print("Keliling dan Luasnya adalah: ", keliling, luas)
