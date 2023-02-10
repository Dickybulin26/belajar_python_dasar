# looping dari list

# for loop
print("For loop\n")
kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["asep","jamal",'udin','supri','malik']

for nama in peserta:
    print(f'nama = {nama}')

# for loop dan range
print("\nFor loop dan range\n")

kumpulan_angka = [10,5,4,2,6,5]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

# while loop
print("\nWhile loop\n")

kumpulan_angka = [10,5,4,2,6,5]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka = {kumpulan_angka}")
    i += 1

# list comperehension
print("\nList comprehension\n")

data = ["udin",1,2,3,"asep"]

[print(f"data = {i}") for i in data]

angka = [10,5,4,2,6,5]

angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# enumerate
print("\nenumerate\n")
data_list = ["udin",1,2,3,"asep"]

for index,data in enumerate(data_list):
    print(f"index = {index},data = {data}")