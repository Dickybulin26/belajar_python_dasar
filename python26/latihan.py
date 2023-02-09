# latihan looping membuat ketupat

# bagian atas
for i in range(0, 5):
    print(" " * (5 - i), end = "")
    for x in range(i):
        print("+ ", end = "")

    print()

# bagian bawah
for i in range(5, 0, -1):
    print(" "*(5-i), end='')
    for x in range(i):
        print("+ ", end='')
    print()