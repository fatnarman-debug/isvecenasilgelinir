# Session Management Skill (Oturum Yönetimi Yeteneği)

Bu yetenek, kullanıcının çalışma seanslarını yönetmesini sağlar. "kapatiyoruz" denildiğinde mevcut durumu kaydeder, "nerde kalmıştık" denildiğinde ise kaldığı yerden devam eder.

## Kurallar ve Komutlar

### 1. "kapatiyoruz" (Seansı Kapat)
Kullanıcı "kapatiyoruz" dediğinde şu adımlar izlenmelidir:
1. **Çalışma Özeti:** O seansta yapılan tüm işlerin (yazılan kodlar, oluşturulan bloglar, düzeltilen hatalar) detaylı bir listesini çıkar.
2. **Aktif Görevler:** Henüz tamamlanmamış veya bir sonraki seansta yapılması planlanan işleri belirle.
3. **Bellek Güncelleme:** `skill/session-memory.md` dosyasını oluştur veya güncelle.
4. **Kapanış Mesajı:** Kullanıcıya yapılan işlerin özetini sun ve "İyi çalışmalar, bir sonraki seansta görüşmek üzere!" şeklinde veda et.

### 2. "nerde kalmıştık" (Seansa Devam Et)
Kullanıcı "nerde kalmıştık" dediğinde şu adımlar izlenmelidir:
1. **Bellek Okuma:** `skill/session-memory.md` dosyasını oku.
2. **Durum Analizi:** En son hangi görevde kalındığını, hangi dosyaların açık olduğunu ve sıradaki adımın ne olduğunu belirle.
3. **Restorasyon:** Kullanıcıya "En son [X] işini yapıyorduk, [Y] dosyaları üzerinde çalışıyorduk. Şimdi [Z] adımından devam edebiliriz." şeklinde bilgi ver.
4. **Hazırlık:** Gerekli dosyaları tekrar aç ve çalışmaya başla.

## Bellek Dosyası Yapısı (skill/session-memory.md)

```markdown
# Session Memory (Oturum Belleği)

## Son Güncelleme: [Tarih/Saat]

## Tamamlanan İşler (Son Seans)
- [Örn: İsveç boşanma rehberi oluşturuldu]
- [Örn: SEO optimizasyonları yapıldı]

## Yarım Kalan / Bekleyen İşler
- [Örn: Watchdog gerçek veriye bağlanacak]
- [Örn: Sitemap güncellenecek]

## Aktif Dosyalar
- [Örn: agents/sentinel.py]
- [Örn: index.html]

## Sıradaki Adım
- [Örn: Sentinel.py içerisindeki scan fonksiyonunun güncellenmesi]
```
