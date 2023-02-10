# operasi dan manipulasi string

# 1. menyambung string (konkatenasi)
from pstats import Stats

nama_pertama = "ucup"
nama_tengah = "bin"
nama_akhir = "mailik"

nama_lengkap = nama_pertama + " " +nama_tengah + "'" + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. operator untuk string

# mengecek apakah ada komponen char / string di string

d = "a"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

D = "A"
status = D in nama_lengkap
print(D + " ada di " + nama_lengkap + " = " + str(status))

d = "a"
status = d not in nama_lengkap
print(d + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)
print(15*"wk")

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-6 : " + nama_lengkap[6])
print("index ke-(-1): " + nama_lengkap[-1]) 
print("index ke-(-2): " + nama_lengkap[-2]) 
print("index ke-[0:3]: " + nama_lengkap[0:4])
print("index ke-[3:7]: " + nama_lengkap[3:8])
print("index ke-[0:2,4,6,8,10]: " + nama_lengkap[0:11:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))

# item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord("'")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# 4.operator dalam bentuk method

data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada data " + data + " = " + str(jumlah))
