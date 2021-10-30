"""
Dictionary adalah suatu topik yang sangat penting dalam python dan data science. Karena dictionary seperti penyusun 
untuk suatu objek yang lebih kompleks seperti pandas dataframe yang akan kita pelajari nanti.

Jadi, dictionary ini adalah salah satu jenis tipe data di python yang memetakan antara key dan value dari suatu data. Berikut contohnya:
"""

numbers = {'one':1, 'two':2, 'three':3}
print(numbers['one'])

# ubah nilai dalam dict
numbers['one'] = 'satu'
print(numbers)

# Loop pd Dict
for k in numbers:
    print("{} = {}".format(k, numbers[k]))
print("")
# Jika kita ingin melakukan iterasi terhadap valuenya saja, maka kita bisa gunakan:
for de in numbers.values():
    print("{}".format(de))

# Object dictionary mempunyai suatu method yang bernama items(), dimana dengan fungsi ini 
# kita dapat melakukan loop terhadap suatu dictionary beserta dengan key dan value nya:
for key, value in numbers.items():
    print("{} = {}".format(key, value))

# Dalam dictionary, untuk mengecek apakah suatu key tertentu ada dalam dictionary tersebut 
# bisa gunakan ‘in’ yang akan menghasilkan nilai Boolean True atau False, seperti berikut:
print('one' in numbers)

# Untuk menambahkan item dalam dictionary, bisa menggunakan syntaks seperti berikut:
numbers = {'one':1, 'two':2, 'three':3}
numbers['four'] = 10
print(numbers)

numbers1 = {'two':5}
numbers.update(numbers1)
print(numbers)

"""
Dalam dictionary, kita bisa melakukan removing data dengan menggunakan method pop, clear dan del. 
pop akan menghapus suatu item dalam dictionary berdasarkan key-nya. clear akan menghapus keseluruhan 
item dalam dictionary. del akan menghapus berdasarkan key, tetapi jika tidak memasukkan key maka fungsi 
del akan menghapus keseluruhan dictionary. Seperti contoh berikut:
"""
numbers = {'four': 10, 'one': 1, 'three': 3, 'two': 5}
numbers.pop('one')
print(numbers)

numbers.clear()
print(numbers)

numbers = {'four': 10, 'three': 3, 'two': 5}
del numbers['four']
print(numbers)

del numbers
print(numbers)

# NameError: name 'numbers' is not defined

"""
Method ->	Description
clear()	-> Removes all items from the dictionary.
copy()	-> Returns a shallow copy of the dictionary.
fromkeys(seq[, v]) ->	Returns a new dictionary with keys from seq and value equal to v (defaults to None).
get(key[,d]) -> Returns the value of the key. If the key does not exist, returns d (defaults to None).
items()	-> Return a new object of the dictionary's items in (key, value) format.
keys()	-> Returns a new object of the dictionary's keys.
pop(key[,d]) -> Removes the item with the key and returns its value or d if key is not found. If d is not provided and the key is not found, it raises KeyError.
popitem() -> Removes and returns an arbitrary item (key, value). Raises KeyError if the dictionary is empty.
setdefault(key[,d]) ->	Returns the corresponding value if the key is in the dictionary. If not, inserts the key with a value of d and returns d (defaults to None).
update([other])	-> Updates the dictionary with the key/value pairs from other, overwriting existing keys.
values() -> Returns a new object of the dictionary's values
"""

# selesai