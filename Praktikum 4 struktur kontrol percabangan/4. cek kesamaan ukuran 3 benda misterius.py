# input besar ukuran benda
input_benda1 = input("Masukkan ukuran benda 1 = ")
input_benda2 = input("Masukkan ukuran benda 2 = ")
input_benda3 = input("Masukkan ukuran benda 3 = ")

#penanganan kesalahan jika pengguna memasukkan input yang tidak valid
try :
    benda1 = int(input_benda1)  #type casting ke integer
    benda2 = int(input_benda2)
    benda3 = int(input_benda3)

    # percabangan kondisi / if else (mencari ukuran yang sama atau tidak terhadap 3 benda)
    if benda1 == benda2 and benda2 == benda3 :
        print("3 benda sama")
    elif benda1 == benda2 or benda1 == benda3 or benda2 == benda3 :
        print("2 benda sama")
    else :
        print("Tidak ada yang sama")

except : 
    print("Masukkan angka ukuran benda dengan benar! ")