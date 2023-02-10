'''Type hints untuk fungsi'''

# bentuk standar fungsi yang sudah kita pelajari
'''
studi kasus
def fungsi(parameter):
    hasil  = parameter**2
    print(hasil)

fungsi(1)
fungsi("ucup")
fungsi(True)
'''

# penggunaan type hints

import string

def sepuluh_pangkat(argument:int) -> int:
    output = 10**argument
    return output

HASIL = sepuluh_pangkat(4)
print(HASIL)

def display(argument:string):
    print(argument)

display("ucup")

