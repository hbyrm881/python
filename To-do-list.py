"""To Do List"""

to_do_list = []

def gorevEkle(todolist):
    gorev = input("Yapılacak görev : ")
    to_do_list.append(gorev)
    print("Ekleme başarılı")
def gorevleriGoster(todolist):
    print("Yapılacak görevler :")
    siraSayisi = 0
    for i in to_do_list:
        siraSayisi += 1
        print(siraSayisi,"- " + i)
def gorevSil(todolist):
    gorev = input("silinecek görevi giriniz : ")
    if gorev in to_do_list:
        to_do_list.remove(gorev)
        print("Silme İşlemi Başaralılı")
    else:
        print("Görev Bulunamadı")

while True:
    print("\n To Do List Uygulaması ")
    print("\n Lütfen yapmak istediğiniz işlemi seçiniz :"
          "\n 1 - Görev Ekle"
          "\n 2 - Görevleri Göster"
          "\n 3 - Görev Sil"
          "\n 4 - Çıkış")
    secim = int(input("Lütfen secimi giriniz : 1/2/3/4 : "))

    if secim == 1 :
        gorevEkle(to_do_list)
    elif secim == 2:
        gorevleriGoster(to_do_list)
    elif secim == 3:
        gorevSil(to_do_list)
    elif secim == 4:
        print("Çıkış yapılıyor...")
        break
    else:
        print("Hatalı tuşlama yaptınız...")






