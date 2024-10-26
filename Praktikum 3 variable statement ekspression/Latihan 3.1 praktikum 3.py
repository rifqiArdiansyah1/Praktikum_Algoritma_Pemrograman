#input variable
bilangan1 = 710;
bilangan2 = 50;
bilangan3 = 600;
mean = bilangan1 + bilangan2 + bilangan3 / 3;

#condition statements
if bilangan1 > bilangan2 and bilangan1 > bilangan3 :
    print("%d adalah bilangan terbesar \n dengan mean (nilai rata-rata) = %.1f" % (bilangan1, mean));
elif bilangan2 > bilangan1 and bilangan2 > bilangan3 :
    print("%d adalah bilangan terbesar \n dengan mean (nilai rata-rata) = %.1f" % (bilangan2, mean));
else :
    print("%d adalah bilangan terbesar \n dengan mean (nilai rata-rata) = %.1f" % (bilangan3, mean));
