import subprocess
import optparse
import re

def kullanici_girdisini_al():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="arayuz", help="Değiştirilecek ağ arayüzü")
    parse_object.add_option("-m", "--mac", dest="mac_adresi", help="Yeni MAC adresi")
    return parse_object.parse_args()

def mac_adresini_degistir(arayuz, yeni_mac):
    subprocess.call(["ifconfig", arayuz, "down"])
    subprocess.call(["ifconfig", arayuz, "hw", "ether", yeni_mac])
    subprocess.call(["ifconfig", arayuz, "up"])

def yeni_mac_kontrol(arayuz):
    ifconfig = subprocess.check_output(["ifconfig", arayuz])
    yeni_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
    if yeni_mac:
        return yeni_mac.group(0)
    else:
        return None

def kullanim_klavuzu():
    print("""
╔════════════════════════════════════╗
║       MAC Adresi Değiştirici       ║
╠════════════════════════════════════╣
║ 1 - MAC Adresini Değiştir          ║
║ 2 - Kullanım Kılavuzunu Göster     ║
║ 3 - Ana Menüye Dön                 ║
╚════════════════════════════════════╝

Kullanım:
sudo python3 script_adi.py -i <arayüz> -m <yeni_mac_adresi>

Örnek:
sudo python3 macchanger.py -i wlan0 -m 00:11:22:33:44:55

Açıklamalar:
- '-i' : MAC adresini değiştireceğiniz ağ arayüzünü girin (örneğin wlan0).
- '-m' : Yeni vermek istediğiniz MAC adresini girin.
Not: Bu işlem için root yetkisi gerekir.
""")
    input("Devam etmek için ENTER tuşuna basın...")

def menu():
    while True:
        print("\n--- MAC Adresi Değiştirici ---")
        print("1 - MAC Adresini Değiştir")
        print("2 - Kullanım Kılavuzunu Göster")
        print("3 - Ana Menüye Dön")
        secim = input("Seçiminiz: ")

        if secim == "1":
            (kullanici_girdisi, _) = kullanici_girdisini_al()
            if not kullanici_girdisi.arayuz or not kullanici_girdisi.mac_adresi:
                print("Lütfen hem arayüz (-i) hem de MAC adresi (-m) belirtin!")
                continue

            mac_adresini_degistir(kullanici_girdisi.arayuz, kullanici_girdisi.mac_adresi)
            son_mac = yeni_mac_kontrol(str(kullanici_girdisi.arayuz))

            if son_mac == kullanici_girdisi.mac_adresi:
                print(f"✅ Başarılı! Yeni MAC adresi: {son_mac}")
            else:
                print("❌ Hata! MAC adresi değiştirilemedi.")
        elif secim == "2":
            kullanim_klavuzu()
        elif secim == "3":
            print("Ana menüye dönülüyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")
