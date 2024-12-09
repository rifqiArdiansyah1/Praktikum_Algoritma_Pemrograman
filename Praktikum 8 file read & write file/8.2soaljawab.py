fileName = input("nama file: ")
try:
    fhand = open(fileName)

    file = fhand.read().split()
    
    fhand.close()

    pertanyaan1 = input(f"{file[0]}\nJawab: ")
    print("Jawaban Benar✅") if pertanyaan1.lower() == file[3].lower() else print("Jawaban Salah❌")
    
    pertanyaan2 =  input(f"{" ".join(file[4:7])}\nJawab: ")
    print("Jawaban Benar✅") if pertanyaan2.lower() == file[8].lower() else print("Jawaban Salah❌")
    
    pertanyaan3 =  input(f"{" ".join(file[9:13])}\nJawab: ")
    print("Jawaban Benar✅") if pertanyaan3.lower() == file[14].lower() else print("Jawaban Salah❌")
    
    pertanyaan4 =  input(f"{" ".join(file[15:20])}\nJawab: ")
    print("Jawaban Benar✅") if pertanyaan4.lower() == file[21].lower() else print("Jawaban Salah❌")
    
    pertanyaan5 =  input(f"{" ".join(file[21:25 ])}\nJawab: ")
    print("Jawaban Benar✅") if pertanyaan5.lower() == file[26].lower() else print("Jawaban Salah❌")
    
    print("Selamat, Anda berhasil menjawab semua pertanyaan!")
        
except:
    print('File tidak ditemukan')