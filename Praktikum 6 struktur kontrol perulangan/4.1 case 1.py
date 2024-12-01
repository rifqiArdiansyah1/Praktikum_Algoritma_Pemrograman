jmlh_pisang_goreng = int(input("Banyak pisang goreng yang ingin dihitung: \n"))
harga_Satuan = int(input("Harga perbiji: \n"))
print("Daftar harga pisang goreng:")

count = 1
while count <= jmlh_pisang_goreng :
    print(f"{count} Pisang goreng: {harga_Satuan * count}")
    count += 1

# for i in range(1, jmlh_pisang_goreng + 1, 1):
#     print(f"{i} Pisang goreng: {harga_Satuan * i}")