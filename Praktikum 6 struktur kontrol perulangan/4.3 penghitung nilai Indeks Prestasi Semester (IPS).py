jumlahMatakuliah = int(input("Masukkan jumlah mata kuliah: "))
sksResult = 0
nilaiA = 4
nilaiB = 3
niaiC = 2
nilaiD = 1
nilaiIPS = 0

for i in range(1,jumlahMatakuliah + 1,1):
    nilaiMatkul = input(f"Masukkan nilai matakuliah ke-{i} (A, B, C, D):")
    sks = int(input(f"Masukkan jumlah SKS mata kuliah ke-{i}:"))
    sksResult += sks
    
    if nilaiMatkul == "A":
        nilaiIPS += (nilaiA * sks)
    elif nilaiMatkul == "B":
        nilaiIPS += (nilaiB * sks)
    elif nilaiMatkul == "C":
        nilaiIPS += (nilaiC * sks)
    elif nilaiMatkul == "D":
        nilaiIPS += (nilaiC * sks)
    
    if i == jumlahMatakuliah:
        nilaiIPS /= sksResult

print(f"Nilai IPS anda adalah: {nilaiIPS}")