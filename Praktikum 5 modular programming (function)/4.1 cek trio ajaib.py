def cek_trio_ajaib (angka1, angka2, angka3) :
    if angka1 != angka2 and angka1 != angka3 and angka2 != angka3 :
        if angka1 + angka2 == angka3 :
            return True
        else :
            return False
    else :
        return False
print(cek_trio_ajaib(1,1,2))   #False
print(cek_trio_ajaib(1,2,1))   #False
print(cek_trio_ajaib(15,5,12)) #True


#   STUDI KASUS
# Kamu sedang membuat program untuk sebuah permainan matematika. Salah satu levelnya
# mengharuskan pemain menemukan tiga angka yang berbeda dan memiliki hubungan khusus:
# jika dua angka dijumlahkan, hasilnya adalah angka ketiga. Buatlah fungsi Python
# cek_trio_ajaib yang akan mengecek apakah tiga angka yang diberikan pemain memenuhi
# kriteria tersebut. Fungsi akan mengembalikan True jika angka-angka tersebut membentuk
# "trio ajaib", dan False jika tidak.