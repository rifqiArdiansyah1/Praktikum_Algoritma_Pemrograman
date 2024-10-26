#input bilangan bulat
input_bil = input("Masukkan suatu bilangan : ")

#try except untuk penanganan kesalahan input (agar tidak terjadi error)
try :
    bilangan = int(input_bil) #type casting integer
    #if else statements (cek apakah bilangan tersebut positif, negatif, nol)
    if int(input_bil) > 0 :
        print("Positif") 
    elif int(input_bil) < 0 :
        print("Negatif")
    else :
        print("Nol")
except :
    print("Anda salah memasukkan input bilangan")