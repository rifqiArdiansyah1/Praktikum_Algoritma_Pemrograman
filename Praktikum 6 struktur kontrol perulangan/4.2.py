hargaTinggi = 0
hargaRendah = None
try:
    while True:
        jawab = input("Masukkan harga (ketik 'stop' untuk berhenti): ")
        
        if jawab == "stop":
            break
        
        harga = int(jawab)
        
        if hargaRendah == None:
            hargaTinggi = harga
            hargaRendah = harga
        else:
            if harga > hargaTinggi:
                hargaTinggi = harga
            if harga < hargaRendah:
                hargaRendah = harga

except:
    print("Input tidak valid. Masukkan harga atau 'stop'")

if hargaRendah != None:
    print(f"Harga Ter-tinggi: Rp.{hargaTinggi}")
    print(f"Harga Ter-rendah: RP.{hargaRendah}")
else:
    print(f"Tidak harga yang dimasukkan!")