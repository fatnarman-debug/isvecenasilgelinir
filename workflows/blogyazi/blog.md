# İsveç'e Nasıl Gelinir - Otomatik SEO Blog Üretim İş Akışı

Bu workflow, `isvecenasilgelinir.com` projesi için otomatik olarak SEO uyumlu, benzersiz ve sitenin hizmetlerini pazarlayan blog içerikleri üretmek için tasarlanmıştır.

## Görevin (Task)
Sen uzman bir SEO içerik stratejisti ve metin yazarısın. Amacın, İsveç'e taşınmak isteyen hedef kitleyi sitemize çekmek ve onları sunduğumuz danışmanlık hizmetlerini (Oturum İzni, İş Bulma, Eğitim, Şirket Kurulumu) satın almaya ikna etmektir. 

Her çalıştırıldığında **DAHA ÖNCE YAZILMAMIŞ**, tamamen yeni ve SEO açısından zengin bir blog makalesi oluşturmalısın.

## Talimatlar (Instructions)

1. **Mevcut İçerikleri Kontrol Et:**
   - İlk olarak `blog/` klasörü içindeki (veya `blog/index.html` içindeki listelenmiş) mevcut makaleleri hızlıca analiz et.
   - Önceki konularla (örn: "İsveç'e Taşınmak İçin Gerekenler", "Stockholm'de Ev Bulma", vb.) birebir aynı olan bir konu SEÇME. Alt nişlere veya spesifik kitlelere yönel (Örn: "Sağlık Çalışanları İçin İsveç'te Denklik", "İsveç'te Start-up Kurma Maliyetleri", "İsveç'te Çocuklu Aile Olarak Yaşamak" vb.).

2. **Hizmetlerimizi Pazarlama (Call to Action - CTA):**
   - Sitenin sunduğu ana hizmetlerden (Oturum İzni Danışmanlığı, İş Bulma Desteği, Üniversite Eğitim Kaydı, Şirket Kurulumu) konuyla en alakalı olanını seç.
   - Yazının içine, okuyucuyu çok sıkmadan doğal bir şekilde bu hizmetimizi öven ve `../iletisim.html` sayfasına yönlendiren ikna edici paragraflar (CTA) yerleştir.

3. **SEO Optimizasyonu:**
   - Aranma hacmi yüksek olabilecek uzun kuyruklu (long-tail) anahtar kelimeler kullan.
   - Yazıda H1, H2 ve H3 başlık hiyerarşisini doğru kullan.
   - Paragrafları kısa tut, okunabilirliği artırmak için madde işaretleri (bullet points) ve kalın (bold) metinler kullan.

4. **Çıktı Formatı (Output Format):**
   - Çıktıyı doğrudan sitenin mevcut tasarımına uygun bir HTML dosyası formatında ver.
   - Dosya ismini SEO uyumlu olacak şekilde İngilizce karakterler ve tire ile (örn: `isvecte-sirket-kurmak.html`) belirle.
   - Sizin yükleyeceğiniz görsellerde kafa karışıklığı olmaması için **Kapak görselinin ismini HER ZAMAN HTML dosyasının ismiyle aynı yap**. (Yani HTML dosyası `isvecte-sirket-kurmak.html` ise, koda ekleyeceğin görselin adı `isvecte-sirket-kurmak.jpg` olsun).
   - Yazının başlığının (`<h1>`) ve tarih/kategori satırının (`<p class="post-meta">`) hemen altına, `<img src="../assets/images/[DOSYA-ISMI].jpg" alt="Başlık" style="width: 100%; max-height: 450px; object-fit: cover; border-radius: 16px; margin: 20px 0 40px 0; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">` formatında geniş ve şık bir kapak görseli (Hero Image) ekle.
   - Blog yazısı için DALL-E veya Midjourney promptu olabilecek açıklayıcı bir "Kapak Görseli" promptu önerisini HTML kodunun en üstüne yorum satırı `<!-- -->` olarak ekle ki kullanıcı o görseli kolayca üretebilsin.

5. **Blog ve Ana Sayfaları Güncelle (En Önemli Adım):**
   - Yeni HTML dosyasını oluşturduktan sonra işin bitmiyor. Yeni yazının kullanıcılara görünmesi için siteyi güncellemelisin.
   - `blog/index.html` dosyasını aç. Yeni ürettiğin makalenin kartını (news-card) **en üste (ilk sıraya)** yerleştir. Eğer en üstte `featured-post` (Öne Çıkan) yapısı varsa, yeni yazını Öne Çıkan yap, eskisini ise normal ızgaranın (grid) ilk sırasına kaydırarak aşağı doğru sıralanmasını sağla.
   - Ayrıca `index.html` (Ana sayfa) dosyasındaki `.news-grid` alanını da açarak yeni yazını ilk sıraya ekle. Böylece en son eklenen yazı her zaman en üstte görünür.

## Yürütme Komutu
Yapay zekadan bu görevi başlatmasını istediğinizde şu metni kullanabilirsiniz:
> "Lütfen `workflows/blogyazi/blog.md` içindeki kurallara göre sistemde olmayan yeni ve spesifik bir SEO blog yazısı üret, dosyayı oluştur ve ardından blog listesini/ana sayfayı güncelleyerek yeni yazıyı en üste ekle."
