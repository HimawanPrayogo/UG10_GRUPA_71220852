no1=int(input("Masukkan nilai soal 1:"))
no2=int(input("Masukkan nilai soal 2:"))
no3=int(input("Masukkan nilai soal 3:"))
umur=int(input("Masukkan umur anda:"))

poin1=no1*(50/100)
poin2=no2*(30/100)
poin3=no3*(20/100)

rata2=poin1+poin2+poin3
print("Rata- rata nilai anda:",rata2)

if (umur<=25)and(rata2>=80):
    print("Selamat Anda Lulus!")
    
elif (umur>25)and(rata2>=90):
    print("Selamat Anda Lulus!")
else:
    print("Coba Lagi Tahun Depan!")
    
