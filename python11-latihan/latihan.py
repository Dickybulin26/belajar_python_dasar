# latihan komparasi dan logika

# soal

# 1.----------0++++++5--------8+++++++11--------
#      false  | true |  false | true   | false

# 2.+++++++++0-------5+++++++++8-------11+++++++
#     true   | false |   true  |  false | true   

print('jawaban no 1')
Angka1 = float(input("Masukkan angka : "))
nol = (Angka1 > 0)
lima = (Angka1 < 5)
delapan = (Angka1 > 8)
sebelas = (Angka1 < 11)
Jawaban = (nol and lima) or (delapan and sebelas)
print("Angka anda :",Jawaban)

print('jawaban no 2')
Angka2 = float(input("Masukkan angka : "))
nol = (Angka2 < 0)
lima = (Angka2 > 5)
delapan = (Angka2 < 8)
sebelas = (Angka2 > 11)
Jawaban = (nol or lima) and (delapan or sebelas)
print("Angka anda :",Jawaban)

