import smtplib
import getpass
import time
from email.message import EmailMessage

# 1. Ayarlar
SENDER_EMAIL = input("Gönderici (Sizin) Gmail Adresiniz: ").strip()
SENDER_PASSWORD = getpass.getpass("Gmail Uygulama Şifreniz (Ekranda görünmez, yazıp Enter'a basın): ").strip()
SUBJECT = "İsveç'te Vergi ve Hukuk Süreçlerinizde Türkçe Destek 🇸🇪"

# Hedef E-Posta Listesi
# Test için öncelikle sadece kendi mailinizi koyun!
TARGET_EMAILS = [
    "furhoff77@gmail.com", "ilkerdagdeviren@yahoo.com", "baroktay@hotmail.com", "cihan.ertas@live.se",
    "senay.sen@hotmail.com", "nasreenshareef72@gmail.com", "pulatserpil@hotmail.com", "sevvalgs44@icloud.com",
    "serensumer91@gmail.com", "hontug@hotmail.com", "cigdem.parlayan@hotmail.se", "ronjagum@outlook.com",
    "aysegulozcan888912@gmail.com", "filiz_tok@hotmail.com", "karason_87@hotmail.com", "mustafaaltinok6302@hotmail.com",
    "jamesdean222@hotmail.com", "ayselkaratass@hotmail.com", "randgha@yahoo.com", "zero-bmw@hotmail.com",
    "19470235s.c@gmail.com", "custovic_almir@hotmail.com", "comboyluk@gmail.com", "nazalarmshne@gmail.com",
    "meryemkurt79@hotmail.com", "wahidyaren2012@gmail.com", "ozlemkocsm@gmail.com", "zonechu@gmail.com",
    "serin7588@gmail.com", "ye20021@hotmail.com", "semralkurnaz@icloud.com", "yagmureva4@gmail.com",
    "senemcandemir2017@gmail.com", "nejathamed73@gmail.com", "ulash141@gmail.com", "akalin86@live.se",
    "zeynepgumul97@hotmail.com", "sira700@gmail.com", "pappa.falt@gmail.com", "bayraklie085@gmail.com",
    "rozgarshakir86@gmail.com", "mukhtarzadeturqay@gmail.com", "Loringunes_@outlook.com", "serpilpolat1985@hotmail.com",
    "songulkurtulus@hotmail.se", "dilekbsky@hotmail.com", "tyuler@hotmail.com", "antkas37@hotmail.com",
    "denizpehriz@gmail.com", "erhannadirler@hotmail.com", "asiyebeydogan@hotmail.com", "erenmelihaltun71@gmail.com",
    "tijengul2906@gmail.com", "medinem_1980@hotmail.de", "asiya.alp89@gmail.com", "charleskonakci@gmail.com",
    "hlkglryz@gmail.com", "nesrin.altuntas@hotmail.com", "ozberrakoz@gmail.com", "enginemekli@gmail.com",
    "nuriyucel3@gmail.com", "feganlatife@gmail.com", "hsnyk27@gmail.com", "ozkan.turan@hotmail.com",
    "savasf16@msn.com", "nevin.peker1993@outlook.com", "aysegulkoyuncu1@gmail.com", "sarvinazmuhidinova@gmail.com",
    "Senol_guzel@hotmail.com", "ayse_ferhan1961@hotmail.com", "awikstentolli@hotmail.com", "melisa.kulbay@gmail.com",
    "sule86k@gmail.com", "pakizekoc13@gmail.com", "profsuchitra@gmail.com", "kaciras_00@hotmail.com",
    "info@sivo.se", "evrim26@hotmail.com", "arafe84@hotmail.com", "merihonal977@gmail.com",
    "ekincirabia20@gmail.com", "selma-kocak@hotmail.com", "polat@live.se", "atanberrin@gmail.com",
    "forsenruth01@gmail.com"
]

# 2. HTML Şablonunu Oku
try:
    with open('email_template.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
except FileNotFoundError:
    print("HATA: email_template.html dosyası bulunamadı. Lütfen scripti mail-gonderim-paneli klasöründe çalıştırın.")
    exit(1)

# Test Modu Sorusu
print("\n--- ÇALIŞMA MODU ---")
print("1: TEST Modu (Sadece size 1 adet mail gönderir)")
print("2: CANLI Mod (Tüm listeye gönderir)")
mode = input("Seçiminiz (1/2): ").strip()

if mode == "1":
    test_email = input("Test mailinin gönderileceği adres (örn: kendi adresiniz): ").strip()
    emails_to_send = [test_email]
    print(f"\nTest modu aktif. Sadece {test_email} adresine gönderilecek.")
elif mode == "2":
    emails_to_send = TARGET_EMAILS
    print(f"\nCANLI mod aktif. Toplam {len(emails_to_send)} kişiye gönderilecek.")
    confirm = input("Emin misiniz? (E/H): ").strip().lower()
    if confirm != "e":
        print("İptal edildi.")
        exit(0)
else:
    print("Geçersiz seçim. İptal ediliyor.")
    exit(1)

# 3. SMTP Bağlantısı ve Gönderim
print("\nSunucuya bağlanılıyor...")
try:
    # Gmail SMTP sunucusu ayarlari
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls() # Güvenli baglanti
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    print("✅ Başarıyla giriş yapıldı.\n")

    success_count = 0
    fail_count = 0

    for idx, target_email in enumerate(emails_to_send, 1):
        msg = EmailMessage()
        msg['Subject'] = SUBJECT
        msg['From'] = f"İsveç'e Nasıl Gelinir <{SENDER_EMAIL}>"
        msg['To'] = target_email
        
        # Sadece HTML versiyonu
        msg.set_content(html_content, subtype='html')

        try:
            print(f"[{idx}/{len(emails_to_send)}] Gönderiliyor: {target_email} ...", end=" ")
            server.send_message(msg)
            print("BAŞARILI")
            success_count += 1
            
            # Anti-Spam Bekleme Süresi (Sadece canlı modda)
            if mode == "2" and idx < len(emails_to_send):
                time.sleep(15) # Her mail arası 15 saniye bekle
        except Exception as e:
            print(f"HATA: {e}")
            fail_count += 1

    server.quit()
    print(f"\n🎉 İşlem tamamlandı! Başarılı: {success_count}, Başarısız: {fail_count}")

except smtplib.SMTPAuthenticationError:
    print("\nHATA: Şifre veya E-posta yanlış!")
    print("Lütfen Gmail hesabınız için oluşturduğunuz 'Uygulama Şifresini' (App Password) kullandığınızdan emin olun.")
except Exception as e:
    print(f"\nBeklenmeyen bir hata oluştu: {e}")
