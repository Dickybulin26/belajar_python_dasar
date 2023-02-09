"""latihan fungsi"""

from email import message
import os
    # program menghitung luas dan keliling persegi panjang 
# while True:
#     # membuat header program
#     os.system("cls")
#     print(f'{"PROGRAM MENGHITUNG LUAS":^40}')
#     print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
#     print(f"{'-'*40:^40}")

#     # mengambil input user
#     LEBAR =  int(input("masukan nilai lebar: "))
#     PANJANG = int(input("masukan nilai panjang: "))

#     # program menghitung luas
#     LUAS = PANJANG*LEBAR
#     KELILING = 2*(PANJANG+LEBAR)

#     # tampilkan hasil
#     print(f"hasil perhitungan luas = {LUAS}")
#     print(f"hasil perhitungan keliling = {KELILING}")

def header():
    '''fungsi Header'''
    # membuat header program
    os.system("cls")
    print(f'{"PROGRAM MENGHITUNG LUAS":^40}')
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    '''fungsi input user'''
    # mengambil input user
    LEBAR =  int(input("masukan nilai lebar: "))
    PANJANG = int(input("masukan nilai panjang: "))

    return LEBAR,PANJANG

def hitung_luas(LEBAR,PANJANG):
    '''fungsi luas'''
    return LEBAR*PANJANG

def hitung_keliling(LEBAR,PANJANG):
    '''fungis keliling'''
    return 2*(LEBAR+PANJANG)

def display(message,value):
    '''fungsi display'''
    print(f"hasil perhitungan {message} = {value}")

# program utama
while True:
    header()
    print("opsi perhitungan:")
    print("1.menghitung keliling")
    print("2.menghitung luas")

    opsi = input("pilih menu no: ")
    if opsi == "1":
        LEBAR,PANJANG = input_user()
        KELILING = hitung_keliling(LEBAR,PANJANG)
        display("keliling",KELILING)

    elif opsi == "2":
        LEBAR,PANJANG = input_user()
        LUAS = hitung_luas(LEBAR,PANJANG)
        display("luas",LUAS)

    isContinue = input("apakah lanjut (Y/N)")
    if isContinue == "N":
        break

print("program selesai, terima kasih")