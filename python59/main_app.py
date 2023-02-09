## Tutorial membaca file eksternal

from importlib.resources import contents


print(3*"=", "membaca file txt ", 3*"=")
file = open("data.txt",mode="r")

print(f"status read : {file.readable()}")
print(f"status read : {file.writable()}")

## baca seluruh file
print(file.read())

## baca per baris
# print(file.readline(), end="") # baca baris pertama
# print(file.readline(), end="") # baca baris berikutnya

## baca semua baris sebagai list
# print(file.readlines())

print(f"apakah file sudah di close : {file.closed}")
file.close()
print(f"apakah file sudah di close : {file.closed}")

## salah satu teknik membuka file di python 

print("\n",3*"=", "membaca file txt dengan with", 3*"=","\n")

with open("data.txt", mode="r") as file:
    content = file.readline()
    print(content,end="")
    
print(f"apakah file sudah di close : {file.closed}")