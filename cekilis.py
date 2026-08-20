import random
import time
kisiler = list()

def ekle(x):
    print("-"*30)
    kisi = input("Kullanıcı adını giriniz: ")
    kisiler.append(kisi)
    print(f"{kisi}, adlı kullanıcı eklendi.")
    input("Devam etmek için herhangi bir tuşa basınız.")

def listele(x):
    say=1
    print("-"*30)
    print("Kişi listesi getiriliyor...")
    time.sleep(2)
    for i in x:
        print(str(say)+"-",i)
        say+=1
    input("Devam etmek için herhangi bir tuşa basınız.")

def sec(x):
    say=1
    print("-"*30)
    kisi_sayi = int(input("Kaç kişi seçilsin: "))
    rastgele_sec = random.sample(x,kisi_sayi)
    print("Çekiliş başlıyor...")
    time.sleep(2)

    for i in rastgele_sec:
        print(f"{say}. kişi seçiliyor...")
        time.sleep(4)
        print(str(say)+"-",i,"kullanıcısı çekilişi kazandı.")
        time.sleep(1)
        say+=1
    input("Devam etmek için herhangi bir tuşa basınız.")

def karistir(x):
    say=1
    print("-"*30)
    random.shuffle(x)
    print("Kişi listesi karıştılıyor...")
    time.sleep(2)
    for i in x:
        print(str(say)+"-",i)
        say+=1
    input("Devam etmek için herhangi bir tuşa basınız.")

while True:
    print("Çekiliş Uygulamasına Hoşgeldiniz")
    print("-"*30)
    print("1-Kullanıcı Ekle\n2-Kullanıcıları Listele\n3-Çekiliş Yap\n4-Listeyi Karıştır")
    secim = int(input("Lütfen bir seçim yapınız: "))

    if secim==1:
        ekle(kisiler)
    elif secim==2:
        listele(kisiler)
    elif secim==3:
        sec(kisiler)
    elif secim==4:
        karistir(kisiler)
    else:
        print("Lütfen uygun bir seçim yapınız.")
    print("-"*30)
