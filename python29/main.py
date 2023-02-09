data_angka = [1,3,4,5,6,63,45,346,643,34,56,4,3]

print(f"data angka = \n{data_angka}")

# count data

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 4 = {jumlah_data_3}")

# ambil posisi data (index)

data = ["udin","jamal","asep","malik"]
print(f"data = {data}")

index_asep = data.index("asep")
index_malik = data.index("malik")
print(f"index si asep = {index_asep}")
print(f"index si malik = {index_malik}")

# mnegurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sesudah sort = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# balik list
data_angka.reverse()
data.reverse()
print(f"data di reverse = \n{data_angka} \n{data}")

