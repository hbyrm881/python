print("hesap makinası = h \nsaat = s")
bs = input("ne yapmak istiyorsun ")

#hesap makinası
if bs == "h":
    print("Toplama +\nÇıkarma -\nBölme /\nÇarpma *\nHangi işlemi yapmak istiyorsun?")
    i = input("işlem: ")
    s1 = int(input("sayı giriniz: "))
    s2 = int(input("sayı giriniz: "))
    if i == "+" :
        s = s1 + s2
        print(s)
        input("çıkmak için herhangi bir tuşa basın: ")
    if i == "-":
        s = s1 - s2
        print(s)
        input("çıkmak için herhangi bir tuşa basın: ")
    if i == "/":
        s = s1 / s2
        print(s)
        input("çıkmak için herhangi bir tuşa basın: ")
    if i == "*":
        s = s1 * s2
        print(s)
        input("çıkmak için herhangi bir tuşa basın: ")

    else :
        print("hatalı işlem")

#saat
if bs == "s":
    import time
    import tkinter as tk


    def güncelle_saat():
        """Saat etiketini günceller."""
        şimdiki_zaman = time.strftime("%H:%M:%S")
        saat_etiket.config(text=şimdiki_zaman)
        saat_etiket.after(1000, güncelle_saat)  # 1 saniye sonra tekrar çağır


    pencere = tk.Tk()
    pencere.title("Dijital Saat")

    saat_etiket = tk.Label(pencere, font=("Arial", 48), bg="black", fg="white")
    saat_etiket.pack(pady=20)

    güncelle_saat()  # İlk kez saati güncelle

    pencere.mainloop()