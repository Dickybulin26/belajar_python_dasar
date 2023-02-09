## -- list --

# kumpulan data numbers
import re


data_angka = [1,2,3]
print(data_angka)

# kumpulan data string
data_str = ["udin","jamal", "siti"]
print(data_str)

# kumbulan boolean 
data_bool = [True, False, True, False]
print(data_bool)

# kumpulan campuran 
data_campuran = [1,"ayam goreng",2,"sapi",True,"burung",False]
print(data_campuran)

## cara alternatif membuat list
data_range = range(0,10,2)# range (start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comperehension
data_list_pake_for =  [i**10 for i in range(0, 10)]
print(data_list_pake_for)

# membuat list pake for pake if
list_pake_for_if = [i for i in range(0, 10) if i != 5]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0, 10) if i%2 == 0]
print(list_pake_for_if)

list_pake_for_if = [i**2 for i in range(0, 10) if i%2 != 0]
print(list_pake_for_if)

