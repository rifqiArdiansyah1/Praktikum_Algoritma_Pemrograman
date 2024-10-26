input_bulan = input("Masukkan bulan berapa (1-12) : ")
input_tahun = input("Masukkan tahun berapa (4 digit) : ")

try :
    bulan = int(input_bulan)
    tahun = int(input_tahun)
    if bulan < 1 or bulan > 12 :    #Menggunakan if else nested / nested decisions 
        print("Masukkan bulan harus antara (1-12)!")
    else :
        if bulan in (4,6,9,11) :
            hari = 30
        elif bulan == 2 :
            if tahun % 4 == 0:  #cek tahun kabisat (29 hari)
                hari = 29
            else :              #jika tidak tahun kabisat (28 hari)
                hari = 28
        else :
            hari = 31
        print("Hari = %d\nBulan Ke = %d\nTahun = %d " % (hari ,bulan, tahun))
except :
    print("Masukkan angka bulan dan tahun dengan benar!")