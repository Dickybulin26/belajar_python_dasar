data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. menggunakan double quote "..."
'''

data ='menggunakan single quote'
print(data)

data ="menggunakan double quote"
print(data)

print('"halo, apa kabar?"')
print("'halo, apa kabar?'")
print("ini adalah hari jum`at")

# 2. menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backlash
print("C:\\user\\Udin")

# tab
print("jamal\t\t\tudin, semakin jauhan")

# backspace
print("jamal  \budin, semakin dekat")

# newline
# LF -> line feed = unix,macos,linux
print("baris pertama.\nbaris kedua.") 
# CR -> carriage return = commodore,acorn,lisp
print("baris pertama.\rbaris kedua") 
# CRLF -> line feed carriage return = windows
print("baris pertama.\r\nbaris kedua") 

# 3. sring literal / raw

# hati-hati
# akan salah pathnya
print('C:\\new folder')

# menggunakan raw strings
print(r'C:\new folder')

# multiline literal string
print('''
Nama : Udin
Kelas : 9 SMP
''')

# multiline literal string dan raw
print(r"""
Nama : Udin
Kelas : 9 SMP\new normal
Webtsite : www.udin.com/home
""")