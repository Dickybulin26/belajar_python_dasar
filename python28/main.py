## Operasi

# index 0(-3)    1(-2)    2(-1) 
data = ["udin", "jamal", "asep"]

# mengambil data dari list ini
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[2]
print(f"data terakhir (index 0) = {data_terakhir}")

data_udin = data[2]
print(f"data udin = {data_terakhir}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"data data = {panjang_data}")

## manipulasi data list

#menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

data.insert(1,"mulyadi")
print(f"data sesudah ditambah = \n{data}")

# menambah di akhir list
data.append("jajang")
print(f"data ditambah lagi = \n{data}")

# menambahkan list dengan list
data_baru = ["ujang","ucup","dadang"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# merubah data
# kita rubah data 2 menjadi malik
data[2] = "malik"
print(f"data rubah = \n{data}")

# meremove data
data.remove("ujang")
print(f"data remove = \n{data}")
# data.remove("gilang") akan error jika tidak ada di list

# meremove data paling belakang
data_akhir = data.pop()
print(f"data terakhir = \n{data}")

print(data_akhir)







