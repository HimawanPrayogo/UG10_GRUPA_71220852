print("===== Selamat datang di Toko Andi Tersenyum, selamat belanja! =====")
a=int(input("Total belanja:Rp. "))

b=a-(a*2/100)

c=a-(a*5/100)

d=a-(a*10/100)

if a<100000:
    print("Tidak ada diskon! maka yang anda bayarkan: Rp.",a)
    
elif a>=100000:
    print("Biaya yang harus dibayar setelah diskon 2% adalah: Rp.",b)

elif a>=500000:
    print("Biaya yang harus dibayar setelah diskon 5% adalah: Rp.",c)

elif a>=1000000:
    print("Biaya yang harus dibayar setelah diskon 10% adalah: Rp.",d)
    
else:
    print("salah")






            
