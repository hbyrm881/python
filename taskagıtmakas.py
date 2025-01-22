import random

def pc_secim_uret():
    n = random.randint(1,3)
    if n == 1:
        return "taş"
    elif n == 2:
        return "kağıt"
    elif n == 3:
       return "makas"

print("Çıkmak için 'çıkış' yazın.")
while True:
    secim = input("Taş Kağıt Makas ? ")
    pc_secim = pc_secim_uret ()
    if secim == "çıkış":
        print("Çıkış yapıldı..")
        break

    print("Bilgisayar secimi : ", pc_secim)

    if secim == "taş" and pc_secim == "makas" :
        print("Kullanıcı kazandı")
    elif secim == "taş" and pc_secim == "kağıt":
        print("Bilgisayar kazandı")
    elif secim == "taş" and pc_secim == "taş":
        print("Berabere")
    elif secim == "kağıt" and pc_secim == "taş":
        print("kullanıcı kazandı")
    elif secim == "kağıt" and pc_secim == "makas":
        print("bilgisayar kazandı")
    elif secim == "kağıt" and pc_secim == "kağıt":
        print("berabere")
    elif secim == "makas" and pc_secim == "kağıt":
        print("kullanıcı kazandı")
    elif secim == "makas" and pc_secim == "taş":
        print("bilgisayar kazandı")
    elif secim == "makas" and pc_secim == "makas":
        print("kullanıcı kazandı")
    else:
        print("Hata!- taş kağıt makas girdiğinizden emin olun")
