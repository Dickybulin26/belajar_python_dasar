from . import Operasi

DB_NAME = "data.txt"

TEMPLATE = {
    "pk"      : "XXXXXX",
    'date_add': "yyy-mm-dd",
    'judul'   : 255*' ',
    'penulis' : 255*' ',
    "tahun"   : 'yyyy'
}


def init_console():
    try:
        with open('data.txt', 'r') as file:
            print("database tersedia, init done!")
    except:
        print('Database tidak ditemukan, silahkan membuat databse baru!')
        Operasi.create_first_data()
        # with open('data.txt', 'w', encoding='utf-8') as file:
        #     penulis = input('Penulis: ')
        #     judul = input('Judul: ')
        #     tahun = input('Tahun: ')
            # data_str = f'{penulis},{judul},{tahun}'
            # file.write(data_str)
