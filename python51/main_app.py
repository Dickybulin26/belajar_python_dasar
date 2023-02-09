# import

# fungsinya adalah untuk mengambil 
# program dari file external .py

# 1.menyambung program dari external

import program_print
import program_ucup

# 2.import dengan data
import variabel
import udin

# data ada di namespace variabel
print(variabel.data)
print(udin.data)

# 3.import dengan fungsi

import matematika

hasil = matematika.tambah(4,5)
print(hasil)