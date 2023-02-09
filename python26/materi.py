#  Latihan perulangan membuat segitiga

sisi = int(input("masukan angka = "))

# 1.menggunakan for

# dummy variabel
print("awal dari for")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

print("akhir dari for")

# 2. menggunakan While

print("awal While")
count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

print("akhir while")

# 3. hanya ganjil saja

print("awal While")
count = 1
while True:
    # akan kembali ke atas jika ganjil
    if (count % 2):
        print("*"*count)
        count += 1

    # akan print jika GENAP
    else:
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break

print("akhir while")

# 4. hanya ganjil saja

print("awal While")
count = 1
spasi = int(sisi/2)
while True:
    # akan kembali ke atas jika ganjil
    if (count % 2):
        print(" "*spasi, "+"*count)
        spasi -= 1
        count += 1

    # akan print jika GENAP
    else:
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break

print("akhir while")




















