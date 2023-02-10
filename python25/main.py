# Break

angka = 0

while True:
    angka += 1
    print(f"angka sekarang -> {angka}")

    if angka == 3:
        print("nice!!")
        break

    print("wassupp!!")

print("end")

data_int = int(input("hitung sampai = "))


angka = 0

while True:
    angka += 1
    # print(f"angka sekarang -> {angka}")
    print(f"count = {angka}")

    if angka == data_int:
        print("nice!!")
        break

    print("wassupp!!")

print("end")