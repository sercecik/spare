import scapy.all as scapy
import optparse
import sys

def kullanici_girdisi_al():
    parse_objesi = optparse.OptionParser()
    parse_objesi.add_option("-i", "--ipadres", dest="ip_adresi", help="Tarama yapılacak IP adresi veya aralığı")

    (kullanici_girdisi, args) = parse_objesi.parse_args()

    if not kullanici_girdisi.ip_adresi:
        print("Lütfen bir IP adresi veya aralığı girin! Örnek: 192.168.1.1/24")
        sys.exit()

    return kullanici_girdisi

def agi_tara(ip):
    print(f"{ip} adresi için tarama başlatılıyor...")
    arp_istegi = scapy.ARP(pdst=ip)
    yayin_paketi = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    birlestirilmis_paket = yayin_paketi / arp_istegi

    cevaplar, cevaplanmayanlar = scapy.srp(birlestirilmis_paket, timeout=2, verbose=False)

    print("Ağda bulunan aktif cihazlar:")
    print("IP Adresi\t\tMAC Adresi")
    print("-" * 40)
    for gonderilen, alinan in cevaplar:
        print(f"{alinan.psrc}\t\t{alinan.hwsrc}")

def kullanim_klavuzu():
    print("""
╔════════════════════════════════════╗
║        Ağ Tarayıcı Kullanımı       ║
╠════════════════════════════════════╣
║ -i veya --ipadres parametresi ile  ║
║   tarama yapılacak IP veya aralık  ║
║   belirtilmelidir.                 ║
║ Örnek:                             ║
║ sudo python3 ag_tarayici.py -i     ║
║ 192.168.1.1/24                     ║
╠════════════════════════════════════╣
║ Not: Bu komut root (sudo) olarak   ║
║ çalıştırılmalıdır.                 ║
╚════════════════════════════════════╝
""")
    input("Devam etmek için ENTER tuşuna basın...")

def menu():
    while True:
        print("\n--- Ağ Tarayıcı ---")
        print("1 - Ağ taraması yap")
        print("2 - Kullanım kılavuzunu göster")
        print("3 - Çıkış")
        secim = input("Seçiminiz: ")

        if secim == "1":
            (kullanici_girdisi, _) = kullanici_girdisi_al()
            agi_tara(kullanici_girdisi.ip_adresi)
        elif secim == "2":
            kullanim_klavuzu()
        elif secim == "3":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    menu()
