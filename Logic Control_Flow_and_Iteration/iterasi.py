# ITERASI / LOOPING
# Loop atau Iterasi adalah cara untuk berulang kali mengeksekusi beberapa kode. Ini sebuah contoh:
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # print all on same line

"""
Ketika kita menggunakan loop, ada beberapa hal yang perlu diperhatikan :
    1. Kita perlu memberikan nama variable yang akan digunakan (dalam contoh di atas adalah planet)
    2. Serentetan nilai yang ingin kita looping untuk melakukan operasi kepada setiap elemennya ( dalam contoh di atas adalah planets ).

range(), range() adalah suatu fungsi yang menghasilkan suatu baris nilai. Lebih jauhnya lagi, 
kita bisa menggunakan fungsi help yang telah kita pelajari sebelumnya untuk lebih faham berbagai macam 
cara untuk menggunakannya. Berikut merupakan satu contoh sederhana :
"""

for i in range(5):
    print("Doing important work. i =", i)

"""
Di python ada sebuah fungsi bawaan yang bernama enumerate(). Enumerate() memungkinkan kita 
untuk melakukan loop terhadap suatu object semacam list disertai dengan pengambilan index dari 
setiap elemennya. Contohnya seperti berikut :
"""
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index,area in enumerate(areas) :
    print("room"+str(index)+": "+str(area))

# Jenis loop lain dalam python adalah while loop, yang terus menerus melakukan looping sampai memenuhi 
# suatu kondisi yang membuat dia harus berhenti, berikut contohnya :
i = 0
while i < 10:
    print(i, end=' ')
    i += 1

"""Argumen dari while loop dievaluasi setiap looping, dan loop dijalankan sampai hasil evaluasi dari conditional operator bernilai False.
Di dalam looping terdapat beberapa statement yang dapat digunakan ketika memenuhi suatu kondisi, seperti break, continue dan pass statement.
Break statement digunakan untuk mengakhiri suatu looping jika telah memenuhi kondisi tertentu. sebagai contoh:"""
while True:
    a = input('input string: ')
    if a == 'quit':
        break
    print('length of a is {}'.format(len(a)))

# Continue statement digunakan untuk menskip atau mengakhiri iterasi yang sedang berjalan dan 
# melanjutkan iterasi selanjutnya. sebagai contoh:
fruits = ['apple', 'banana', 'orange', 'grape', 'pineapple']
for fruit in fruits:
    if fruit == 'orange':
        continue
    print('my fruit is {}'.format(i))
# Pada program di atas, iterasi akan berhenti ketika memenuhi kondisi ‘orange’ dan melanjutkan ke iterasi selanjutnya.

"""
Pass statement merupakan null statement. Pass digunakan ketika kita membuat suatu stament tetapi tidak 
ingin menambahkan suatu kode. Saat statement Pass dieksekusi, maka tidak akan terjadi apa-apa tetapi kita bisa menghindari error.
"""
# Exception Handling
"""Ketika ada suatu error di sebuah kode, Python biasanya akan berhenti mengeksekusi 
kode selanjutnya dan menampilkan error. Exception handling merupakan statement yang mengatur error dalam sebuah kode.
    - Try : suatu statement yang mengetes kode error
    - Except : suatu statement yang menghandle apabila ada error
    - Finally : suatu statement yang mengeksekusi suatu kode
"""
a = int(input())
b = int(input())

try:
    c = a/b
except Exception as e:
    print('raising error in:', e)
finally:
    print('Finish')
