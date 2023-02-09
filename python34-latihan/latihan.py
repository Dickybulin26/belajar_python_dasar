# program list buku

list_buku = []
while True:
    print('masulan data buku')
    judul = input("masukan judul buku\t: ")
    penulis = input("masukan nama penulsi\t: ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

    print("\n\n",'='*10,'Data buku',"="*10)
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]} ")

    print("\n\n",'='*20)
    islanjut = input("Apakah dilanjutkan?(yes/no) ")

    if islanjut == 'no':
        break

print("PROGRAM SELESAI")