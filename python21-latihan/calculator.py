# latihan 
# kalkulator sederhana

print(20*"=")
print("kalkulator sederhana")
print(20*"=" + "\n")

angka_1 = float(input("masukana angka 1 = "))
operator = input("operator (+,-,*,/) : ")
angka_2 = float(input("masukan angka 2 = "))

# percabangan

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")
    
elif operator == "*" or operator == "x":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")

elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")

else:
    print("masukan yang bener dong!, aku pusing nih")

print("akhir dari program,terima kasih")
