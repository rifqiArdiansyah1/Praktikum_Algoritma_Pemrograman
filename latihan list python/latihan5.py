inputListAngka = input("Masukkan list angka: ")
listAngka = inputListAngka.split(",")
listAngkaGenap = []
for angka in listAngka:
    if int(angka) % 2 == 0:
        listAngkaGenap.append(angka.strip())

print(listAngkaGenap)