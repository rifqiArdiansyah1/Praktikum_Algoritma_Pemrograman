kalimat = "saya belajar      python   di  Malang"

#menghilangkan spasi ganda menggunakan function sendiri
def hapus_spasi_ganda(kalimat):
    kalimat_baru = ""
    for i in range(len(kalimat)):
        if kalimat[i] != " " or kalimat[i - 1] != " ":
            kalimat_baru += kalimat[i]
    return kalimat_baru

kalimat_baru = hapus_spasi_ganda(kalimat)
print(kalimat_baru)

#menghilangkan spasi ganda menggunakan built-in function
kalimat_baru = " ".join(kalimat.split())
print(kalimat_baru)