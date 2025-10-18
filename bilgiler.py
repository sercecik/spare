def bilgi_getir(numara):
    bilgiler = {
        "1": "Antivirüs Yazılımı: Zararlı yazılımları tespit edip temizlemek için kullanılan güvenlik yazılımıdır.",
        "2": "Casus Yazılım (Spyware): Kullanıcının haberi olmadan bilgi toplayan zararlı yazılımdır.",
        "3": "Dağıtık Hizmet Engelleme Saldırısı (DDoS): Sistemi aşırı istekle çökertme saldırısıdır.",
        "4": "Fidye Yazılımı (Ransomware): Dosyaları şifreleyip açmak için fidye isteyen zararlı yazılımdır.",
        "5": "Güvenlik Duvarı (Firewall): Gelen ve giden ağ trafiğini kontrol eden güvenlik sistemidir.",
        "6": "Kabakuvvet Saldırısı (Brute Force): Şifreleri sistemli denemelerle kırma yöntemidir.",
        "7": "Kali: Linux tabanlı ve açık kaynaklı bir sızma testi işletim sistemidir.",
        "8": "Ortadaki Adam Saldırısı (MITM): İki taraf arasındaki iletişime gizlice girerek verileri izleyen, değiştiren ya da yönlendiren bir siber saldırı türüdür.",
        "9": "Oltalama (Phishing): Sahte sitelerle kullanıcıdan bilgi çalmaya çalışan saldırı türüdür.",
        "10": "Sanal Özel Ağ (VPN): İnternette şifreli ve güvenli şekilde gezinmeyi sağlayan ağ yapısıdır.",
        "11": "Saldırı Önleme Sistemi (IPS): Şüpheli aktiviteleri engelleyen güvenlik sistemidir.",
        "12": "Saldırı Tespit Sistemi (IDS): Ağda şüpheli hareketleri algılayan güvenlik sistemidir.",
        "13": "Saldırı Ekibi (Red Team): Sistemdeki açıkları bulan ve saldırı simülasyonları yapan ekiptir.",
        "14": "Savunma Ekibi (Blue Team): Sistemi savunan ve saldırılara karşı önlem alan ekiptir.",
        "15": "SQL Enjeksiyonu: Web uygulamalarında veri tabanına zararlı SQL komutları enjekte etme saldırısıdır.",
        "16": "Sosyal Mühendislik: İnsanları manipüle ederek gizli bilgi edinme yöntemidir.",
        "17": "Sıfır Gün Açığı (Zero-Day): Henüz bilinmeyen ve yaması olmayan güvenlik açığıdır.",
        "18": "Sızma Testi (Penetration Test): Güvenlik açıklarını bulmak için sistemin test edilmesidir.",
        "19": "Sistem Gizleyici Yazılım (Rootkit): Sisteme gizlice yerleşip iz bırakmadan çalışan zararlı yazılımdır.",
        "20": "Truva Atı (Trojan): Zararsız gibi görünüp arka planda zarar veren yazılımdır.",
        "21": "Tuş Kaydedici (Keylogger): Kullanıcının yazdığı tuşları kaydeden casus yazılımdır.",
        "22": "Yama (Patch): Yazılım açıklarını kapatmak için yapılan güncellemelerdir.",
        "23": "Zararlı Yazılım (Malware): Cihaza zarar veren tüm kötü amaçlı yazılımların genel adıdır.",
        "24": "Şifreleme (Encryption): Veriyi güvenli hale getirmek için dönüştürme işlemidir.",
        "25": "Güvenlik Açığı (Vulnerability): Sistemde kötü niyetli kişilerin kullanabileceği zayıf noktadır.",
        "26": "Parola Yönetimi: Güçlü ve güvenli parolaların oluşturulması ve saklanmasıdır.",
        "27": "Siber Tehdit İstihbaratı: Siber saldırıları önceden tespit etmek için bilgi toplama sürecidir.",
        "28": "Sosyal Medya Güvenliği: Sosyal medya platformlarında kişisel bilgilerin korunmasıdır.",
        "29": "Wi-Fi Güvenliği: Kablosuz ağların saldırılardan korunması için alınan önlemler.",
        "30": "Yedekleme (Backup): Veri kaybına karşı bilgilerin kopyalanması işlemidir."
    }
    return bilgiler.get(numara, "Geçerli bir bilgi numarası giriniz.")


def liste():
    print("\n--- Bilgi Listesi (Alfabetik) ---")
    print("1  - Antivirüs Yazılımı")
    print("2  - Casus Yazılım")
    print("3  - Dağıtık Hizmet Engelleme Saldırısı (DDoS)")
    print("4  - Fidye Yazılımı")
    print("5  - Güvenlik Duvarı")
    print("6  - Kabakuvvet Saldırısı")
    print("7  - Kali")
    print("8  - Ortadaki Adam (MITM) Saldırısı")
    print("9  - Oltalama (Phishing)")
    print("10 - Sanal Özel Ağ (VPN)")
    print("11 - Saldırı Önleme Sistemi (IPS)")
    print("12 - Saldırı Tespit Sistemi (IDS)")
    print("13 - Saldırı Ekibi (Red Team)")
    print("14 - Savunma Ekibi (Blue Team)")
    print("15 - SQL Enjeksiyonu")
    print("16 - Sosyal Mühendislik")
    print("17 - Sıfır Gün Açığı")
    print("18 - Sızma Testi")
    print("19 - Sistem Gizleyici Yazılım (Rootkit)")
    print("20 - Truva Atı")
    print("21 - Tuş Kaydedici")
    print("22 - Yama (Patch)")
    print("23 - Zararlı Yazılım")
    print("24 - Şifreleme")
    print("25 - Güvenlik Açığı")
    print("26 - Parola Yönetimi")
    print("27 - Siber Tehdit İstihbaratı")
    print("28 - Sosyal Medya Güvenliği")
    print("29 - Wi-Fi Güvenliği")
    print("30 - Yedekleme")
    print("99 - Ana Menüye Dön\n")
