kalimat = "saya adalah mahasiswa teknik informatika"
kataSplit = kalimat.split()
kataPendek = ""
kataPanjang = ""

for kata in kataSplit:
    if len(kata) < len(kataPendek) or kataPendek == "":
        kataPendek = kata
    if len(kata) > len(kataPanjang) or kataPanjang == "":
        kataPanjang = kata

print("Kata terpendek:", kataPendek)
print("Kata terpanjang:", kataPanjang)