# OPERASI KOMPERASI

# setiap hasil operasi komperasi adalah boolean

# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# lebih besar dari (>)
print("======== lebih besar dari (>)")
hasil = a > 3
print(a,">",3,"=",hasil)

hasil = b > 3
print(a,">",3,"=",hasil)

hasil = b >2
print(a,">",2,"=",hasil)

# lebih kecil dari (<)
print("======== lebih kecil dari (<)")

hasil = a < 3
print(a,"<",3,"=",hasil)

hasil = b < 3
print(a,"<",3,"=",hasil)

hasil = b <2
print(a,"<",2,"=",hasil)

# lebih besar dari (>=)
print("======== lebih dari sama dengan (>=)")
hasil = a >= 3
print(a,">=",3,"=",hasil)

hasil = b >= 3
print(a,">=",3,"=",hasil)

hasil = b >=2
print(a,">=",2,"=",hasil)

# lebih besar dari (<=)
print("======== kurang dari sama dengan (<=)")
hasil = a <= 3
print(a,"<=",3,"=",hasil)

hasil = b <= 3
print(a,"<=",3,"=",hasil)

hasil = b <=2
print(a,"<=",2,"=",hasil)

# samadengan (==)
print("======== kurang dari sama dengan (==)")
hasil = a == 4
print(a,"==",4,"=",hasil)

hasil = b == 4
print(b,"==",4,"=",hasil)

# samadengan (!=)
print("======== kurang dari sama dengan (!=)")
hasil = a != 4
print(a,"!=",4,"=",hasil)

hasil = b != 4
print(b,"!=",4,"=",hasil)

# 'is' sebagai komparasi objekct indentity
print("======== object identity (is)")
# x = 5 ini adalah assignment membuat object 
x = 5
y = 5
print('nilai x =',x,'id = ',hex(id(x)))
print('nilai y =',y,'id = ',hex(id(y)))
hasil = x is y
print('x is y = ',hasil)

x = 5
y = 6
print('nilai x =',x,'id = ',hex(id(x)))
print('nilai y =',y,'id = ',hex(id(y)))
hasil = x is y
print('x is y = ',hasil)

# 'is not' sebagai komparasi objekct indentity
print("======== object identity (is not)")
# x = 5 ini adalah assignment membuat object 
x = 5
y = 5
print('nilai x =',x,'id = ',hex(id(x)))
print('nilai y =',y,'id = ',hex(id(y)))
hasil = x is not y
print('x is not y =',hasil)

x = 5
y = 6
print('nilai x =',x,'id = ',hex(id(x)))
print('nilai y =',y,'id = ',hex(id(y)))
hasil = x is not y
print('x is not y =',hasil)
