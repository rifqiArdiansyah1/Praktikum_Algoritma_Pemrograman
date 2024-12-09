input_file1 = input("Masukkan nama file pertama: ")
input_file2 = input("Masukkan nama file kedua: ")
try:
    file1 = open(input_file1, "r")
    file2 = open(input_file2, "r")
    data1 = file1.read()
    data2 = file2.read()
    ukuranFile1 = len(data1) / 1000
    ukuranFile2 = len(data2) / 1000
    selisihUkuranFile = ukuranFile1 - ukuranFile2 if ukuranFile1 > ukuranFile2 else ukuranFile2 - ukuranFile1
    
    file1.seek(0)
    file2.seek(0)
    
    barisFile1 = len(file1.readlines())
    barisFile2 = len(file2.readlines())
    selisihBarisFile = barisFile1 - barisFile2 if barisFile1 > barisFile2 else barisFile2 - barisFile1
    
    print("\nPerbedaan Ukuran File:")
    print(f"Ukuran file 1 : {ukuranFile1:.2f} KB")
    print(f"Ukuran file 2 : {ukuranFile2:.2f} KB")
    print(f"Selisih ukuran file 1 dan 2 : {selisihUkuranFile} KB")
    
    print("\nPerbedaan Baris File:")
    print(f"Baris File 1 : {barisFile1}")
    print(f"Baris File 2 : {barisFile2}")
    print(f"Selisih baris file 1 dan 2 : {selisihBarisFile}")
    
    file1.close()
    file2.close()
    
except FileNotFoundError:
    print("Salah satu atau kedua file tidak ditemukan")
except IOError:
    print("Terjadi kesalahan saat membaca file")