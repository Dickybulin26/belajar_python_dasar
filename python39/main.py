import datetime

mahasiswa1 =  {
    'nama': 'ucup surucup',
    'nis': '13265510',
    'sks_lulus': 130,
    'beasiswa': False,
    'lahir':datetime.datetime(2007,2,26)
}

mahasiswa2 =  {
    'nama': 'Otong Surotong',
    'nis': '54641684',
    'sks_lulus': 140,
    'beasiswa': True,
    'lahir':datetime.datetime(2008,2,6)
}

mahasiswa3 =  {
    'nama': 'Asep Surasep',
    'nis': '15416161',
    'sks_lulus': 266,
    'beasiswa': False,
    'lahir':datetime.datetime(2005,5,7)
}

data_mahasiswa = {
    'MAH001': mahasiswa1,
    'MAH002': mahasiswa2,
    'MAH003': mahasiswa3,
}

print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIS = data_mahasiswa[KEY]['nis']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")
