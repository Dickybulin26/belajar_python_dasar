'''*args'''

# memasukan data/argument

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("ucup",170,50)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
    
fungsi(["otong",150,55])

# kenalan dengan *args

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("dudung",155,60)

# studi kasus

def tambah(*data):
    # data tipenya adalah tuple, dia bisa di literasi
    output = 0
    for angka in data:
        output += angka

    return output

hasil = tambah(10,5,15)
print(f"hasil = {hasil}")