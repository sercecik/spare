import random


class SoruCevap:
    def __init__(self):
        self.sorular = {
            "Antivirüs yazılımı ne işe yarar?": "zararlı yazılımları tespit edip temizlemek",
            "Casus yazılım (spyware) nedir?": "kullanıcının haberi olmadan bilgi toplayan zararlı yazılım",
            "Dağıtık Hizmet Engelleme Saldırısı (DDoS) nedir?": "sistemi aşırı istekle çökertme saldırısı",
            "Fidye yazılımı (ransomware) ne yapar?": "dosyaları şifreleyip açmak için fidye ister",
            "Güvenlik duvarı (firewall) ne işe yarar?": "gelen ve giden ağ trafiğini kontrol eder",
            "Brute force (kaba kuvvet) saldırısı nedir?": "şifreleri deneme yanılma ile kırma yöntemi",
            "Kali nedir?": "linux tabanlı açık kaynaklı sızma testi işletim sistemi",
            "Ortadaki adam (MITM) saldırısı ne demektir?": "iki taraf arasındaki iletişime gizlice girme",
            "Oltalama (phishing) nedir?": "sahte sitelerle kullanıcıdan bilgi çalma saldırısı",
            "Sanal özel ağ (VPN) ne işe yarar?": "internette şifreli güvenli bağlantı sağlar",
            "Saldırı önleme sistemi (IPS) nedir?": "şüpheli aktiviteleri engelleyen güvenlik sistemi",
            "Saldırı tespit sistemi (IDS) ne yapar?": "ağdaki şüpheli hareketleri algılar",
            "Red team (saldırı ekibi) kimdir?": "sistemde açıkları bulan saldırı simülatörleri",
            "Blue team (savunma ekibi) ne yapar?": "sistemi savunan güvenlik ekibi",
            "SQL enjeksiyonu nedir?": "veritabanına zararlı SQL komutları ekleme saldırısı",
            "Sosyal mühendislik ne anlama gelir?": "insanları manipüle ederek bilgi edinme yöntemi",
            "Sıfır gün açığı (zero-day) nedir?": "henüz bilinmeyen ve yamalanmamış güvenlik açığı",
            "Sızma testi (penetrasyon testi) ne amaçlar?": "güvenlik açıklarını bulmak için sistemi test etmek",
            "Rootkit (sistem gizleyici yazılım) ne demektir?": "gizlice sistemde çalışan zararlı yazılım",
            "Truva atı (trojan) nedir?": "zararsız görünür ama zarar veren yazılım",
            "Keylogger (tuş kaydedici) ne yapar?": "kullanıcının yazdığı tuşları kaydeder",
            "Yama (patch) nedir?": "yazılım açıklarını kapatan güncelleme",
            "Malware (zararlı yazılım) nedir?": "cihaza zarar veren kötü amaçlı yazılımlar"
        }
        self.dogru_cevaplar = []
        self.yanlis_cevaplar = []

    def secenek_uret(self, dogru_cevap):
        tum_cevaplar = list(self.sorular.values())
        yanlis_cevaplar = random.sample([c for c in tum_cevaplar if c != dogru_cevap], 2)
        secenekler = yanlis_cevaplar + [dogru_cevap]
        random.shuffle(secenekler)
        return secenekler

    def baslat(self):
        print("\n--- Soru-Cevap Modu ---")
        print("Çıkmak için 'q' tuşuna basın.\n")

        yanlis_sayisi = 0

        while True:
            soru, dogru_cevap = random.choice(list(self.sorular.items()))
            secenekler = self.secenek_uret(dogru_cevap)
            harfler = ['a', 'b', 'c']
            cevap_harfleri = dict(zip(harfler, secenekler))
            print(f"Soru: {soru}")
            for harf in harfler:
                print(f"  {harf}) {cevap_harfleri[harf]}")
            kullanici_cevap = input("Cevabınız (a/b/c veya q): ").lower()

            if kullanici_cevap == 'q':
                print("Soru-cevap modundan çıkılıyor.\n")
                break

            if kullanici_cevap in cevap_harfleri:
                secilen = cevap_harfleri[kullanici_cevap]
                if secilen == dogru_cevap:
                    print("Doğru! 🎉\n")
                    self.dogru_cevaplar.append(soru)
                else:
                    print(f"Yanlış! Doğru cevap: {dogru_cevap}\n")
                    self.yanlis_cevaplar.append(soru)
                    yanlis_sayisi += 1
                    if yanlis_sayisi == 3:
                        print("3 yanlış yaptınız. Moddan çıkılıyor.\n")
                        break
            else:
                print("Geçersiz seçim. a, b, c veya q girin.\n")

        input("Sonuçları görmek için bir tuşa basın...")
        self.ozet_goster()

    def ozet_goster(self):
        print("\n--- Doğru Cevapladığınız Sorular ---")
        if self.dogru_cevaplar:
            for soru in self.dogru_cevaplar:
                print("✔️", soru)
        else:
            print("Hiç doğru cevap verilmedi.")

        print("\n--- Yanlış Cevapladığınız Sorular ---")
        if self.yanlis_cevaplar:
            for soru in self.yanlis_cevaplar:
                print("❌", soru)
        else:
            print("Hiç yanlış cevap verilmedi.")
        print()




