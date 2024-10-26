#input
upah_per_jam = int(input("Masukkan berapa upah per jam = "));
jam_per_minggu = int(input("Masukkan berapa jam per minggu = "));

#1.total cuan sebelum kena pajak
total_cuan_sebelum_kena_pajak = upah_per_jam * jam_per_minggu * 5;

#2.sisa cuan setelah bayar pajak
total_cuan_setelah_bayar_pajak = total_cuan_sebelum_kena_pajak - 0.14 * total_cuan_sebelum_kena_pajak;

#3.rincian belanja: fashion, perlengkapan belajar, csr pribadi, anak yatim dan fakir-miskin.
fashion = 0.10 * total_cuan_setelah_bayar_pajak;
perlengkapan_belajar = 0.01 * total_cuan_setelah_bayar_pajak;
csr = 0.25 * total_cuan_setelah_bayar_pajak;
anak_yatim = 0.30 * total_cuan_setelah_bayar_pajak;
fakir_miskin = total_cuan_setelah_bayar_pajak - fashion - perlengkapan_belajar - csr - anak_yatim;

#output
print("-------------------------------------------------------------------------------------------")
print("Total cuan Wawan sebelum kena pajak = %d" % (total_cuan_sebelum_kena_pajak))
print("Sisa cuan Wawan setelah bayar pajak = %d" % (total_cuan_setelah_bayar_pajak))
print("Rincian belanja: \n fashion = %d \n perlengkapan belajar %d \n csr pribadi = %d \n anak yatim = %d \n fakir miskin = %d" % 
(fashion, perlengkapan_belajar, csr, anak_yatim, fakir_miskin))
