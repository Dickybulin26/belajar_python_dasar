# episode latihan logika dan komparasi
# membuat gabungan area rentang dari angka

# ++++++3-------10++++++

inputUser = float(input('masukan angka yang bernilai\n kurang dari 3 \natau \nlebih besar dari 10\n : '))

# +++++++3---------------
# memriksa angka kurang dari 3
iskurangdari = (inputUser < 3)
print("kurang dari 3 = ",iskurangdari)

# -----------------10++++++
# memriksa angka lebih dari 10
islebihdari = (inputUser > 10)
print("lebih dari 10 = ",islebihdari)

# ++++++3-------10++++++

iscorrect = iskurangdari or islebihdari
print("angka yang anda masukan: ",iscorrect)

# -------3++++++10------
# kasus irisan

inputUser = float(input('masukan angka yang bernilai\n lebih dari 3 \ndan \nkurang dari 10\n : '))

# -------3++++++++++
# lebih dari 3
print("\n",10*'=',"\n")
islebihdari = inputUser > 3
print('lebih dari 3 = ',islebihdari)

# ++++++++++10______
# memriksa angka lebih dari 10
iskurangdari = (inputUser < 10)
print('kurang dari 10 = ',iskurangdari)

# -------3++++++10------
iscorrect = iskurangdari and islebihdari
print("angka yang anda masukan: ",iscorrect)

