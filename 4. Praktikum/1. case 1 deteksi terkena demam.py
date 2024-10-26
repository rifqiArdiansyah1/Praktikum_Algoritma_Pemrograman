#input bilangan bulat
input_suhu = input("Masukkan suhu tubuh: ")

#try except untuk penanganan kesalahan input (agar tidak terjadi error)
try :
    # cek apakah suhu badan tersebut termasuk kategori demam atau tidak
    suhu = int(input_suhu)
    if suhu >= 38:
        print("Anda demam")
    else:
        print("Anda tidak demam")
except :
    print("Anda memasukkan input yang salah")
