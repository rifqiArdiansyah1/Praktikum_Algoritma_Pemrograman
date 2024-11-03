def cocokkan_produk (bilangan1, bilangan2, bilangan3) :
    if bilangan1 % 10 == bilangan2 % 10 or bilangan1 % 10 == bilangan3 % 10 or bilangan2 % 10 == bilangan3 % 10:
        return True
    else :
        return False
print(cocokkan_produk(286, 896, 234))   #true
print(cocokkan_produk(286, 8932, 2346)) #true
print(cocokkan_produk(2863, 896, 234))  #false



#   STUDI KASUS
# Kamu sedang membuat program untuk sebuah toko online yang ingin mengelompokkan
# produk berdasarkan digit terakhir dari kode produknya. Buatlah fungsi Python
# cocokkan_produk yang akan memeriksa apakah minimal dua dari tiga kode produk yang
# diberikan memiliki digit terakhir yang sama. Gunakan fungsi tersebut untuk mengecek
# beberapa test-case berikut ini:
# Input = 900, 10, 38. Output yang diharapkan = True
# Input = 276, 6, 75. Output yang diharapkan = True
# Input = 63, 391, 108. Output yang diharapkan = False
# Input = 654, 24, 74. Output yang diharapkan = True
# Fungsi ini akan membantu toko untuk membuat promosi khusus untuk produk-produk dengan
# digit terakhir yang sama.