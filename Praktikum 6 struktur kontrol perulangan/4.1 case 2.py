print("Selamat datang di kalkulator deret pintar")
jumlahBilangan = int(input("Masukkan banyaknya bilangan, kemudian ENTER: \n"))
totalBilangan = 0
totalRerata = 0
count = 1

print("Deret bilangan: ", end="")

while count <= jumlahBilangan:
    if count == jumlahBilangan:
        print(f"{count}", end="")
    else:
        print(f"{count}", end="")
    totalBilangan += count
    count += 1

# for i in range(1,jumlahBilangan+1, 1) :
#     if i == jumlahBilangan:
#         print(f"{i}", end="")
#     else:
#         print(f"{i}", end=",")
#     totalBilangan += i

print(f"  Total seluruh bilangan jika dijumlahkan: {totalBilangan}")
totalRerata = totalBilangan / jumlahBilangan
print("Total rerata: %.1f" % totalRerata)