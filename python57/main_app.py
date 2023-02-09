import numpy as np

list_a = [1,2,3,4]
vector_a = np.array([1, 2, 3, 4])

print(f"list_a = {list_a}")
# print(list_a**2) <- ini akan gagal
print(vector_a**2)
print(f"a pangkat 2 = {vector_a}")
print(f"a kali 5 = {vector_a*5}")

matrix_b = np.array([(1,2),(3,4)])
print(f"matrix_b = \n{matrix_b}")
print(f"matrix_b b^2 = \n{matrix_b**2}")

zeros_c = np.zeros((2,2))
print(f"zeros_c nol = \n{zeros_c}")

ones_d = np.ones((2,2))
print(f"zeros_c satu = \n{ones_d}")

jumlah = matrix_b + matrix_b**2 + ones_d
print(f"hasil penjumlahan matrik = \n{jumlah}")
