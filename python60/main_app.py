# 1. mode write

# dia akan membuat file baru jika tidak ada,
# lalu akan menimpa / overwrite isinya

with open("data_1.txt","w",encoding="utf-8") as file:
    file.write("ucup surucup")

with open("data_1.txt","w",encoding="utf-8") as file:
    file.write("ucup surucup")

with open("data_1.txt","w",encoding="utf-8") as file:
    file.write("ucup surucup")

# 2. mode append

with open("data_2.txt","a",encoding="utf-8") as file:
    file.write("jon si jhonny\n")

with open("data_2.txt","a",encoding="utf-8") as file:
    file.write("ucup surucup\n")

with open("data_2.txt","a",encoding="utf-8") as file:
    file.write("tambah lagi dengan append\n")