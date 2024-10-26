hours = 45
rate = 10 
pay = 0

if hours > 40 :
    #gaji = kerja 40 jam * gaji + jam lembur (diatas 40 jam) * rate * 1.5 (gaji dilipatkan 1.5)
    pay = 40 * rate + (hours - 40) * (rate * 1.5)
else :
    pay = hours * rate

print(pay)