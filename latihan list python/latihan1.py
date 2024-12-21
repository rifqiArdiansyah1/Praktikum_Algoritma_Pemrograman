buah = ['apel', 'jeruk', 'mangga', 'anggur', 'pisang']
print(buah)

#menambahkan data list
buah.append('pepaya')
buah.append('semangka')
buah.append('melon')
print(buah)
#menghapus data list
buah.remove('apel')

#mengubha data list
buah[len(buah)-1] = 'durian'

print(buah)