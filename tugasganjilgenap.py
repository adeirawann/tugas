# Nama: Mohammad Ade Irawan
# Nim: 222410102081

x = ("Genap")
y = ("Ganjil")
o = ("Kecil")
p = ("Sedang")
q = ("Besar")

bil = int(input("Masukkan Angka: "))
bilnew = bil % 2

if bilnew == 0 : 
    if bil < 10 :
        print("Bilangan", bil, "Merupakan Bilangan", x, "Dan Tergolong Bilangan", o)
    elif 10 <= bil <= 50 :
        print("Bilangan", bil, "Merupakan Bilangan", x, "Dan Tergolong Bilangan", p)
    else :
        print("Bilangan", bil, "Merupakan Bilangan", x, "Dan Tergolong Bilangan", q)

elif bilnew == 1 :
    if bil < 10 :
        print("Bilangan", bil, "Merupakan Bilangan", y, "Dan Tergolong Bilangan", o)
    elif 10 <= bil <= 50 :
        print("Bilangan", bil, "Merupakan Bilangan", y, "Dan Tergolong Bilangan", p)
    else :
        print("Bilangan", bil, "Merupakan Bilangan", y, "Dan Tergolong Bilangan", q)

