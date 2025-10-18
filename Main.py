from termcolor import colored
import pyfiglet
import bilgiler  # bilgiler.py dosyasını içe aktarır
from soru_cevap import SoruCevap
import macchanger
import ag_tarayici
import ag_arp_saldiri
import sniffer
import kraken
# Başlık ASCII sanatı
ascii_yazi = pyfiglet.figlet_format("Türkçe Siber Güvenlik Eğitimi Programına")
renkli_yazi = colored(ascii_yazi, color="green")

def ana_menu():
    return ("1 - Bilgi Listesini Görüntüle\n"
            "2 - Soru-Cevap Modu\n"
            "3 - MAC Adresi Değiştirici\n"
            "4 - Ağ Tarayıcı\n"
            "5 - Ortadaki Adam Saldırısı\n"
            "6 - Paket Dinleyici (Sniffer)\n"
            "7 - Kraken\n"
            "8 - Çıkış")

def baslik_goster():
    print(renkli_yazi)


def bilgiler_menusu():
    while True:
        bilgiler.liste()
        secim = input("Lütfen bilgi numarasını girin (Ana menüye dönmek için 99): ")

        if secim == "99":
            break
        elif secim.isdigit() and 1 <= int(secim) <= 30:
            print("\n" + bilgiler.bilgi_getir(secim) + "\n")
            input("Bilgi görüntülendi. Devam etmek için ENTER tuşuna basın...")
        else:
            print("\nGeçersiz giriş. Lütfen tekrar deneyin.\n")
            input("Bilgi görüntülenemedi. Devam etmek için ENTER tuşuna basın...")


# Program başlasın
baslik_goster()
print("**** Programa Hoş Geldiniz ****\n")
print(ana_menu())  # Program başlarken ana menüyü göster

while True:
    secim = input("Seçiminizi girin: ")

    if secim == "1":
        bilgiler_menusu()
        print(ana_menu())
    elif secim == "2":
        sc = SoruCevap()
        sc.baslat()
        print(ana_menu())
    elif secim == "3":
        macchanger.menu()
        print(ana_menu())
    elif secim == "4":
        ag_tarayici.menu()  # Ağ tarayıcı menüsünü çalıştır
        print(ana_menu())
    elif secim == "5":
        ag_arp_saldiri.menu()
        print(ana_menu())
    elif secim == "6":
        sniffer.mainfunc()
        print(ana_menu())
    elif secim == "7":
        kraken.execkraken()
        print(ana_menu())
    elif secim == "8":
        print("Programdan çıkılıyor. İyi günler dileriz.")
        break
    else:
        print("Geçersiz giriş yaptınız. Lütfen tekrar deneyin.\n")
        print(ana_menu())



