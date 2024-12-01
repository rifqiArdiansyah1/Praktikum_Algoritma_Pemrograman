kalimat = "dirumah saya gempa bumi gempa bumi di malang gempa bumi di surabaya"

kataKunci = "gempa bumi"
kataKunciCount = kalimat.count(kataKunci) #menggunakan Built-in Function

#menggunakan function sendiri 
def keyword(kalimat, kata_kunci):
    total = 0
    index = 0
    while index < len(kalimat):
        if kalimat[index:index + len(kata_kunci)] == kata_kunci:
            total += 1
            index += len(kata_kunci)
        else:
            index += 1
            
    return total

total = keyword(kalimat, kataKunci)
print("Kata ditemukan sebanyak", total, "kali")
print("Kata ditemukan sebanyak", kataKunciCount, "kali")
