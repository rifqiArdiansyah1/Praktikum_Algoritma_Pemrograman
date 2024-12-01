kata1 = input("Masukkan kata-kata Pertama: ")
kata2 = input("Masukkan kata-kata Kedua: ")

kata1Processed = sorted(kata1.lower().replace(" ", ""))
kata2Processed = sorted(kata2.lower().replace(" ", ""))

if kata1Processed == kata2Processed:
    print("Anagram")
else:
    print("Bukan Anagram")

