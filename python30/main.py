## teknik meduplikat list

a = ["udin","otong","dudung"]
print(f"a = {a}")

b = a #pass by reference
print(f"b = {b}")

# kita akan merubah member dari a 

#  ini akan merubah kedua list
a[1] = "malik"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list
print(f'adress a = {hex(id(a))}')
print(f'adress b = {hex(id(b))}')

# menduplikat list dengan copy

print("membuat list c dengan a.copy")
c = a.copy() # full suplikat / data baru

print(f'adress a = {hex(id(a))}')
print(f'adress b = {hex(id(b))}')
print(f'adress c = {hex(id(c))}')

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 0")

c[0] = "asep"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 1")

c[1] = "dudung"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")







