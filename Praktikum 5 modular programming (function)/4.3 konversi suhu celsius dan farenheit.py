celcius = 5
farenheit = 10

celcius_to_farenheit = lambda celcius: (celcius * 9/5) + 32
farenheit_to_celcius = lambda farenheit: (farenheit - 32) * 5/9

print(celcius,"Celcius =", celcius_to_farenheit(celcius), "Farenheit")
print(farenheit,"Farenheit =", farenheit_to_celcius(farenheit), "Celcius")


#   STUDI KASUS
# Kamu sedang mengembangkan aplikasi cuaca untuk smartphone. Salah satu fitur yang
# dibutuhkan adalah konversi suhu antara Celsius dan Fahrenheit. Buatlah dua fungsi lambda
# di Python untuk melakukan konversi ini. Fungsi-fungsi tersebut akan menjadi dasar dari modul
# konversi suhu dalam aplikasimu.