#!/usr/bin/env python3
import os
import re
from datetime import datetime

BASE_DIR = "/Users/fatnar/Documents/isvecenasilgelinir"
TEMPLATE_PATH = os.path.join(BASE_DIR, "agents/blog_template.html")

POSTS = [
    {
        "slug": "isvec-vatandaslik-sinavi-nedir-2026",
        "title": "İsveç Vatandaşlık Sınavı (Medborgarskapsprov) Nedir? 2026 Yeni Şartlar",
        "breadcrumb_name": "Vatandaşlık Sınavı Nedir",
        "category": "Göçmenlik & Hukuk",
        "meta_description": "6 Haziran 2026'da yürürlüğe girecek yeni İsveç vatandaşlık sınavı (Medborgarskapsprov) kuralları, sınavın amacı ve yasal çerçeve rehberi.",
        "lead_paragraph": "İsveç hükümetinin toplumsal entegrasyonu artırmak amacıyla yürürlüğe koyduğu yeni İsveç vatandaşlık sınavı (Medborgarskapsprov) sistemi 6 Haziran 2026 itibarıyla resmen başlıyor. Peki bu sınav nedir, kimleri kapsıyor ve İsveç vatandaşlığı alırken süreç nasıl işleyecek?",
        "cta_title": "İsveç Vatandaşlık Sınavına Şimdiden Hazırlanın",
        "cta_text": "Ağustos 2026'daki ilk resmi sınava hazırlanmak ve İsveç toplumu, tarihi ve kültürü hakkındaki soruları eksiksiz yanıtlamak için Türkiye'nin en popüler hazırlık platformunu kullanın.",
        "cta_button_text": "Vatandaşlık Sınavı Hazırlık Portalına Git",
        "body_content": """
<p>İsveç'te uzun süredir tartışılan ve göçmenlik politikalarının en önemli adımlarından biri olan <strong>zorunlu vatandaşlık sınavı (Medborgarskapsprov)</strong>, 2026 yılı itibarıyla hayata geçiriliyor. Universitets- och högskolerådet (UHR) tarafından hazırlanan ve organize edilen bu sınav, İsveç vatandaşlığına başvuracak kişilerin ülkenin demokratik değerleri, toplumsal yapısı, hakları ve yükümlülükleri konusundaki bilgilerini ölçmeyi amaçlamaktadır.</p>

<h2>İsveç Vatandaşlık Sınavının Amacı Nedir?</h2>
<p>İsveç hükümetinin yaptığı resmi açıklamalara göre, vatandaşlık testi sadece bir eleme aracı değil, aynı zamanda yeni vatandaşların İsveç toplumuna uyum sürecini (integration) hızlandırmayı amaçlayan bir adımdır. Sınavın temel hedefleri şunlardır:</p>
<ul>
    <li>Adayların İsveç'teki temel demokratik kuralları ve anayasal hakları bilmesini sağlamak.</li>
    <li>İsveç sosyal güvenlik sistemi, iş piyasası kuralları ve günlük yaşama dair temel bilgileri test etmek.</li>
    <li>Vatandaşlık bağının önemini ve ortak toplumsal değerleri pekiştirmek.</li>
</ul>

<div class="elite-info-box" style="border-radius: 12px; margin: 30px 0;">
    <h3 style="margin-top: 0; color: #1e293b;">Kritik Bilgi: Sınav Hangi Dilde Yapılacak?</h3>
    <p>İsveç vatandaşlık sınavı <strong>tamamen İsveççe (Svenska)</strong> dilinde gerçekleştirilecektir. Sınavda herhangi bir çeviri veya ek dil desteği sunulmayacaktır. Bu nedenle adayların en az SFI D seviyesinde (A2/B1 okuma-anlama) İsveççe bilgisine sahip olmaları kritik bir önem taşımaktadır.</p>
</div>

<h2>2026 Yılı Vatandaşlık Sınavı Temel Kuralları</h2>
<table class="data-table-clean" style="width: 100%; border-collapse: collapse; margin: 20px 0;">
    <thead>
        <tr style="background-color: #f1f5f9;">
            <th style="padding: 12px; border: 1px solid #e2e8f0; text-align: left;">Özellik</th>
            <th style="padding: 12px; border: 1px solid #e2e8f0; text-align: left;">Detaylar</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="padding: 12px; border: 1px solid #e2e8f0; font-weight: bold;">Yürürlük Tarihi</td>
            <td style="padding: 12px; border: 1px solid #e2e8f0;">6 Haziran 2026</td>
        </tr>
        <tr>
            <td style="padding: 12px; border: 1px solid #e2e8f0; font-weight: bold;">İlk Sınav Tarihi</td>
            <td style="padding: 12px; border: 1px solid #e2e8f0;">15 Ağustos 2026 (Kayıtlar Haziran 2026 başında başlar)</td>
        </tr>
        <tr>
            <td style="padding: 12px; border: 1px solid #e2e8f0; font-weight: bold;">Sınav Formatı</td>
            <td style="padding: 12px; border: 1px solid #e2e8f0;">Kağıt üzerinde, yaklaşık 60 çoktan seçmeli soru (90 dakika)</td>
        </tr>
        <tr>
            <td style="padding: 12px; border: 1px solid #e2e8f0; font-weight: bold;">Sınav Yeri</td>
            <td style="padding: 12px; border: 1px solid #e2e8f0;">Ağustos 2026'daki ilk sınav sadece Stockholm'de yapılacaktır</td>
        </tr>
        <tr>
            <td style="padding: 12px; border: 1px solid #e2e8f0; font-weight: bold;">Kayıt Şartı</td>
            <td style="padding: 12px; border: 1px solid #e2e8f0;">Yalnızca Migrationsverket'ten resmi davet (kallelse) alanlar kayıt olabilir</td>
        </tr>
    </tbody>
</table>

<h2>Sınava Nasıl Hazırlanmalısınız?</h2>
<p>İsveç vatandaşlık sınavını tek seferde geçmek, vatandaşlık sürecinizin uzamasını engellemek için son derece önemlidir. Resmi kaynakların yanı sıra, sınav formatına birebir uyumlu interaktif testlerle pratik yapmak en etkili hazırlık yöntemidir.</p>

<p>Sınava hazırlık sürecinde eksiklerinizi görmek ve gerçek sınav deneyimini simüle etmek için <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" style="color: #005bb5; font-weight: 600; text-decoration: underline;">sverigemedborgarskapsprov.com</a> platformu üzerinden deneme sınavlarını çözebilir, İsveççe terimler ve toplumsal bilgiler üzerinde kendinizi test edebilirsiniz.</p>

<div style="text-align: center; margin: 30px 0;">
    <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" class="btn btn-primary" style="display: inline-block; padding: 14px 28px; font-size: 1.1rem; border-radius: 8px; text-decoration: none; font-weight: 700; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0, 91, 181, 0.2); background-color: #005bb5; color: white;">İsveç Vatandaşlık Sınavı Çalışma Portalına Git</a>
</div>
"""
    },
    {
        "slug": "isvec-vatandaslik-sinavi-ne-zaman-agustos-2026",
        "title": "İlk İsveç Vatandaşlık Sınavı Ne Zaman Yapılacak? Ağustos 2026 Detayları",
        "breadcrumb_name": "Sınav Ne Zaman Yapılacak",
        "category": "Göçmenlik & Hukuk",
        "meta_description": "İlk resmi İsveç vatandaşlık sınavı 15 Ağustos 2026'da yapılıyor. Sınav tarihi, yeri ve katılım detayları hakkında resmi UHR açıklamaları.",
        "lead_paragraph": "İsveç vatandaşlığına giden yolda en çok merak edilen sorulardan biri yanıt buldu: İlk resmi İsveç vatandaşlık sınavı (Medborgarskapsprov) 15 Ağustos 2026 tarihinde düzenlenecek. Sınav takvimi, kayıt başlangıcı ve sınav yerleri hakkında bilmeniz gereken her şeyi derledik.",
        "cta_title": "15 Ağustos Sınavına Eksiksiz Hazırlanın",
        "cta_text": "Sınavın kağıt üzerinde ve kısıtlı sürede yapılacağını unutmayın. Hızlı soru çözme ve İsveççe okuma anlama becerilerinizi şimdiden geliştirin.",
        "cta_button_text": "İnteraktif Sınav Sorularını Çöz",
        "body_content": """
<p>İsveç Yükseköğretim Kurulu (<strong>UHR</strong>), 2026 yılında yürürlüğe girecek olan vatandaşlık sınavının ilk resmi oturumunun <strong>15 Ağustos 2026</strong> cumartesi günü gerçekleştirileceğini duyurdu. Bu ilk sınav, sistemin pilot uygulaması (utprövningsprov) niteliğinde olup, gelecekteki sınavların yapısını şekillendirmek açısından büyük öneme sahiptir.</p>

<h2>Sınav Takvimi ve Önemli Tarihler</h2>
<p>Ağustos ayındaki sınava girmek isteyen adayların başvuru süreçlerini çok yakından takip etmesi gerekmektedir. İşte resmi UHR takvimine göre dikkat etmeniz gereken tarihler:</p>
<ul>
    <li><strong>Haziran 2026 Başı:</strong> Sınav kayıt sistemi (anmälan) resmen açılacaktır. Adaylar BankID veya resmi kimlik bilgileri ile online kayıt yapabilecektir.</li>
    <li><strong>Temmuz 2026 Ortası:</strong> Kayıtların kapanması ve sınav giriş belgelerinin (kallelse/bekräftelse) gönderilmesi.</li>
    <li><strong>15 Ağustos 2026 (Saat 10:00):</strong> Sınavın gerçekleştirilmesi.</li>
    <li><strong>Eylül 2026:</strong> Sınav sonuçlarının açıklanması ve Migrationsverket dosyalarına işlenmesi.</li>
</ul>

<div class="elite-info-box" style="border-radius: 12px; margin: 30px 0;">
    <h3 style="margin-top: 0; color: #1e293b;">Önemli Detay: İlk Sınav Yalnızca Stockholm'de!</h3>
    <p>UHR'nin yayınladığı resmi bilgilere göre, 15 Ağustos 2026 tarihindeki ilk sınav <strong>yalnızca Stockholm şehrindeki sınav merkezlerinde</strong> yapılacaktır. Göteborg, Malmö veya diğer İsveç şehirlerinde yaşayan ve bu sınava girmek üzere davet edilen adayların sınav günü Stockholm'de hazır bulunmaları gerekmektedir.</p>
</div>

<h2>Sınav Başvurusu İçin Ne Gerekiyor?</h2>
<p>Her isteyen bireysel olarak Ağustos 2026 sınavına kayıt yaptıramaz. Sınava başvurabilmek için öncelikle Migrationsverket'ten vatandaşlık başvurusu sürecinde olduğunuzu ve bu sınava girmeniz gerektiğini belirten resmi bir randevu davet mektubu almış olmanız gerekmektedir. Davet mektubu alan adaylar, UHR'nin kayıt sistemi üzerinden Stockholm'deki kontenjanlar dolmadan yerlerini ayırtmalıdır.</p>

<p>Sınav tarihine kadar kendinizi test etmek ve İsveç vatandaşlık sınavı soru tiplerine aşina olmak için <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" style="color: #005bb5; font-weight: 600; text-decoration: underline;">sverigemedborgarskapsprov.com</a> adresini ziyaret edebilir, her gün yeni eklenen deneme sınavlarıyla hazırlık yapabilirsiniz.</p>

<div style="text-align: center; margin: 30px 0;">
    <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" class="btn btn-primary" style="display: inline-block; padding: 14px 28px; font-size: 1.1rem; border-radius: 8px; text-decoration: none; font-weight: 700; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0, 91, 181, 0.2); background-color: #005bb5; color: white;">Sınav Sorularını ve Denemeleri Görüntüle</a>
</div>
"""
    },
    {
        "slug": "isvec-vatandaslik-sinavi-basvurusu-ve-kayit",
        "title": "İsveç Vatandaşlık Sınavı Başvurusu ve Kayıt İşlemleri (Haziran 2026)",
        "breadcrumb_name": "Başvuru ve Kayıt Süreci",
        "category": "Göçmenlik & Hukuk",
        "meta_description": "İsveç vatandaşlık sınavı (Medborgarskapsprov) kaydı nasıl yapılır? UHR portalı, Migrationsverket davet mektubu ve randevu süreci rehberi.",
        "lead_paragraph": "İsveç vatandaşlık sınavına girmek için gerekli olan başvuru süreci Haziran 2026'da başlıyor. Sınav kaydı nasıl yapılır, başvuru için hangi belgeler istenir ve adım adım kayıt adımları nelerdir? Bu yazımızda tüm kayıt detaylarını inceliyoruz.",
        "cta_title": "Sınav Kaydından Sonra Çalışmalara Başlayın",
        "cta_text": "Kayıt işlemlerini tamamladıktan sonra zaman kaybetmeden hazırlık yapmalısınız. İsveç vatandaşlık sınavı müfredatına en uygun interaktif deneme sınavları platformumuzda.",
        "cta_button_text": "Deneme Sınavları ile Kendini Dene",
        "body_content": """
<p>İsveç vatandaşlığına geçiş sürecinde zorunlu hale gelen Medborgarskapsprov için resmi kayıtlar Haziran 2026 başında açılıyor. Sınav koordinasyonunu yürüten <strong>Universitets- och högskolerådet (UHR)</strong>, adayların kayıt sırasında izlemesi gereken resmi adımları yayınladı. İşte adım adım İsveç vatandaşlık sınavı başvuru rehberi.</p>

<h2>Adım 1: Migrationsverket Davet Mektubunu (Kallelse) Bekleyin</h2>
<p>Vatandaşlık sınavına girmek için ilk ve en önemli şart, Migrationsverket'ten gelen resmi davet mektubudur. Göçmen dairesi, başvurunuzu inceledikten sonra sınava girmeniz gerektiğini belirten benzersiz bir referans numarası içeren bir mektup yollayacaktır. Bu mektup elinize ulaşmadan UHR sistemi üzerinden sınava kayıt yaptırmanız mümkün değildir.</p>

<h2>Adım 2: UHR Sınav Kayıt Portalına Giriş Yapın</h2>
<p>Davet mektubunuz geldikten sonra UHR'nin resmi sınav portalına (<em>uhr.se/medborgarskapsprovet</em>) giderek kaydınızı oluşturmalısınız:</p>
<ul>
    <li>Sisteme güvenli bir şekilde giriş yapmak için <strong>İsveç BankID</strong> (Mobile BankID) kullanmanız gerekmektedir.</li>
    <li>Kişisel kimlik numaranız (Personnummer) ve Migrationsverket davet referans numaranızı sisteme girmelisiniz.</li>
    <li>Ağustos 2026 sınavı için şu an tek sınav merkezi olan <strong>Stockholm</strong> seçeneğini işaretleyerek uygun saat dilimini seçmelisiniz.</li>
</ul>

<h2>Adım 3: Sınav Giriş Belgesini Alın ve Yazdırın</h2>
<p>Kayıt işlemini başarıyla tamamladıktan sonra e-posta adresinize bir onay mesajı (bekräftelse) gönderilecektir. Sınav gününden yaklaşık 2 hafta önce ise sınav salonu, sıra numarası ve sınav saatinin yer aldığı resmi sınav giriş belgeniz sistemde tanımlanacaktır. Sınav günü bu belgenin çıktısını ve geçerli bir İsveç kimlik kartını (Legitimation) yanınızda bulundurmanız zorunludur.</p>

<div class="elite-info-box" style="border-radius: 12px; margin: 30px 0;">
    <h3 style="margin-top: 0; color: #1e293b;">Özel İhtiyaç Desteği (Anpassat prov)</h3>
    <p>Okuma güçlüğü (disleksi), görme veya işitme kaybı gibi sağlık sorunları olan adaylar, kayıt esnasında bunu belirterek sınav süresinin uzatılmasını veya sınav kağıdının daha büyük fontlarla basılmasını talep edebilirler. Bu talepler için doktor raporu sunulması zorunludur.</p>
</div>

<p>Kayıt işlemlerinizi tamamladıktan sonra sınav günü heyecanını yenmek ve soru tiplerine önceden alışmak için <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" style="color: #005bb5; font-weight: 600; text-decoration: underline;">sverigemedborgarskapsprov.com</a> sitesindeki interaktif testleri çözebilir, eksik konularınızı hızla tespit edebilirsiniz.</p>

<div style="text-align: center; margin: 30px 0;">
    <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" class="btn btn-primary" style="display: inline-block; padding: 14px 28px; font-size: 1.1rem; border-radius: 8px; text-decoration: none; font-weight: 700; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0, 91, 181, 0.2); background-color: #005bb5; color: white;">Kayıt Sonrası Hazırlık Platformuna Git</a>
</div>
"""
    },
    {
        "slug": "isvec-vatandaslik-sinavi-konulari-mufredat",
        "title": "İsveç Vatandaşlık Sınavında Hangi Konular Çıkacak? Sınav Müfredatı",
        "breadcrumb_name": "Sınav Konuları ve Müfredat",
        "category": "Göçmenlik & Hukuk",
        "meta_description": "İsveç vatandaşlık sınavında sorulacak toplumsal bilgi (samhällskunskap) konuları, demokrasi, hukuk sistemi ve İsveç tarihi müfredatı.",
        "lead_paragraph": "İsveç vatandaşlık sınavında başarılı olmak için hangi konulara çalışmalısınız? UHR tarafından belirlenen resmi 'Samhällsorientering' müfredatı, İsveç tarihi, yasal sistemi, demokratik değerleri ve iş piyasasını kapsıyor. Detaylı konu başlıklarını inceleyin.",
        "cta_title": "Müfredattaki Tüm Konulardan Deneme Çözün",
        "cta_text": "İsveç tarihi, coğrafyası, yasaları ve anayasal hakları kapsayan yüzlerce özgün soruyla sınavı riske atmadan şimdiden çalışmaya başlayın.",
        "cta_button_text": "Müfredat Sorularını İncele",
        "body_content": """
<p>İsveç vatandaşlık testi (Medborgarskapsprov), adayların İsveç toplumuna entegrasyon seviyesini ve ülkenin işleyişi hakkındaki bilgilerini ölçmek amacıyla tasarlanmıştır. Sınav soruları, İsveç belediyelerinin yeni gelen göçmenlere verdiği <strong>Toplumsal Bilgilendirme (Samhällsorientering)</strong> dersleri ve resmi kaynaklar temel alınarak hazırlanmaktadır.</p>

<h2>İsveç Vatandaşlık Sınavı Konu Başlıkları</h2>
<p>Sınavda sorulacak sorular temel olarak 4 ana kategoriye ayrılmaktadır. Bu konular şunlardır:</p>

<h3>1. İsveç Hukuk Sistemi ve Demokratik Yapı</h3>
<ul>
    <li><strong>Demokrasinin Esasları:</strong> İsveç Anayasası (Grundlagar), ifade özgürlüğü, insan hakları ve eşitlik ilkeleri.</li>
    <li><strong>Yönetim Biçimi:</strong> Parlamenter monarşi, Riksdag (parlamento), hükümet (regeringen) ve belediyelerin (kommuner) görevleri.</li>
    <li><strong>Hukuk Devleti:</strong> Mahkemeler, polis teşkilatı, vatandaşların yasal hak ve sorumlulukları.</li>
</ul>

<h3>2. İsveç Sosyal Güvenlik Sistemi ve Refah Devleti</h3>
<ul>
    <li><strong>Sağlık ve Bakım:</strong> Sağlık sistemi (vårdval), yaşlı bakımı, çocuk ve aile destekleri.</li>
    <li><strong>Försäkringskassan:</strong> Ebeveyn izni (föräldrapenning), hastalık sigortası ve işsizlik yardımları.</li>
    <li><strong>Eğitim Sistemi:</strong> Skolverket standartları, okul zorunluluğu (skolplikt), üniversite eğitimi ve yetişkin eğitimi (Komvux).</li>
</ul>

<h3>3. İsveç İş Piyasası ve Çalışma Hayatı</h3>
<ul>
    <li><strong>İsveç Modeli (Den svenska modellen):</strong> Sendikalar (fackförbund) ve işveren örgütleri arasındaki anlaşmalar.</li>
    <li><strong>İş Hukuku:</strong> Çalışma saatleri, yıllık izin hakları, işten çıkarma kuralları (LAS) ve iş sağlığı güvenliği.</li>
    <li><strong>Vergi Sistemi:</strong> Skatteverket kuralları, gelir vergisi, KDV ve sosyal güvenlik primleri.</li>
</ul>

<h3>4. İsveç Tarihi, Coğrafyası ve Kültürü</h3>
<ul>
    <li><strong>Tarihsel Dönemeçler:</strong> İsveç'in modernleşme süreci, tarafsızlık politikası ve AB üyeliği.</li>
    <li><strong>Coğrafi Bilgiler:</strong> İsveç'in bölgeleri, büyük şehirleri ve çevre koruma bilinci (Allemansrätten).</li>
    <li><strong>Kültürel Yapı:</strong> Ulusal bayramlar, dini ve laik gelenekler, toplumsal cinsiyet eşitliği kültürü.</li>
</ul>

<h2>Sınav Sorularına Nasıl Hazırlanmalısınız?</h2>
<p>Müfredat oldukça geniş bir alanı kapsasa da, sınavda çıkacak sorular pratik ve güncel hayat bilgisine dayalı olacaktır. Sınavın İsveççe olması nedeniyle, konulara İsveççe terimlerle çalışmak oldukça önemlidir. Örneğin, <em>Riksdagen</em>, <em>Grundlagar</em>, <em>Allemansrätten</em> veya <em>LAS</em> gibi kavramların ne anlama geldiğini iyi bilmelisiniz.</p>

<p>İsveç vatandaşlık sınavı müfredatındaki tüm bu konuları kapsayan, özenle hazırlanmış interaktif soru bankasına ulaşmak ve kendinizi test etmek için <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" style="color: #005bb5; font-weight: 600; text-decoration: underline;">sverigemedborgarskapsprov.com</a> sitesini kullanabilir, sınavdaki başarı oranınızı artırabilirsiniz.</p>

<div style="text-align: center; margin: 30px 0;">
    <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" class="btn btn-primary" style="display: inline-block; padding: 14px 28px; font-size: 1.1rem; border-radius: 8px; text-decoration: none; font-weight: 700; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0, 91, 181, 0.2); background-color: #005bb5; color: white;">Müfredata Uygun Deneme Sınavlarını Çöz</a>
</div>
"""
    },
    {
        "slug": "isvec-vatandaslik-sinavi-soru-sayisi-sure-format",
        "title": "İsveç Vatandaşlık Sınavı Formatı: Soru Sayısı, Süre ve Puanlama",
        "breadcrumb_name": "Sınav Formatı ve Süre",
        "category": "Göçmenlik & Hukuk",
        "meta_description": "İsveç vatandaşlık sınavı kaç soru, sınav süresi kaç dakika? Çoktan seçmeli soru formatı ve sınav uygulama detayları.",
        "lead_paragraph": "İsveç vatandaşlık sınavı (Medborgarskapsprov) formatı netleşti. 90 dakika sürecek olan sınavda adaylara çoktan seçmeli sorular yöneltilecek. Soru sayısı, puanlama sistemi ve sınav uygulama esaslarını detaylıca inceliyoruz.",
        "cta_title": "Zamana Karşı Yarışın: Deneme Sınavları Çözün",
        "cta_text": "90 dakikalık süreyi en verimli şekilde kullanmak için hazırlık sitemizde zaman sınırlı deneme testlerini çözerek hız kazanın.",
        "cta_button_text": "Zaman Sınırlı Deneme Çöz",
        "body_content": """
<p>İsveç Yükseköğretim Kurulu (UHR) tarafından hazırlanan resmi yönergelere göre, 2026 yılından itibaren uygulanacak olan İsveç vatandaşlık sınavının formatı adayların heyecanını azaltacak şekilde standart bir yapıya kavuşturuldu. Sınavın teknik yapısı, süresi ve puanlanması ile ilgili en son güncellemeler şu şekildedir:</p>

<h2>Soru Sayısı ve Yapısı</h2>
<p>İsveç vatandaşlık sınavında adaylara **yaklaşık 60 çoktan seçmeli (flervalsfrågor) soru** sorulacaktır. Sınavdaki soruların yapısı şu şekildedir:</p>
<ul>
    <li>Her sorunun <strong>4 seçeneği</strong> (A, B, C, D) bulunacaktır.</li>
    <li>Soruların yalnızca <strong>1 doğru cevabı</strong> olacaktır.</li>
    <li>Yanlış cevaplar doğru cevapları götürmeyecektir (Net puanlama sistemi uygulanacaktır).</li>
</ul>

<h2>Sınav Süresi ve Kuralları</h2>
<p>Sınav için belirlenen toplam süre **90 dakikadır (1.5 saat)**. Adayların sınav başladıktan sonra ilk 30 dakika boyunca salondan çıkmalarına izin verilmeyecektir. Sınav esnasında sözlük, akıllı telefon, tablet, ders notu veya yardımcı herhangi bir materyal kullanılması kesinlikle yasaktır.</p>

<div class="elite-info-box" style="border-radius: 12px; margin: 30px 0;">
    <h3 style="margin-top: 0; color: #1e293b;">Kağıt Üzerinde Sınav Formatı (Pappersprov)</h3>
    <p>Ağustos 2026 tarihindeki ilk pilot sınav **kağıt üzerinde (paper-based)** yapılacaktır. Adaylar soruları optik forma veya doğrudan sınav kağıdına kurşun kalem kullanarak işaretleyeceklerdir. Dijital sınav sistemine geçiş ise 2027 yılı itibarıyla kademeli olarak planlanmaktadır.</p>
</div>

<h2>Geçme Puanı ve Sonuçlar</h2>
<p>Sınavı geçmek (Godkänd) için gereken tam doğru sayısı UHR tarafından resmi olarak belirlenir. Genellikle bu oran toplam soruların **%60 ile %70'ine** denk gelmektedir (yaklaşık 36-42 doğru cevap). Sınav sonuçları doğrudan göç dairesine (Migrationsverket) iletilecek ve adayın başvuru dosyasına eklenecektir. Sınavda başarısız olan adaylar için herhangi bir hak sınırı bulunmamakta, adaylar bir sonraki sınav döneminde tekrar başvurabilmektedir.</p>

<p>Sınav formatına alışmak, 90 dakikalık süreyi doğru yönetmek ve İsveççe çoktan seçmeli soru yapısını tecrübe etmek için <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" style="color: #005bb5; font-weight: 600; text-decoration: underline;">sverigemedborgarskapsprov.com</a> sitesindeki süre sınırlı deneme testlerinden yararlanabilirsiniz.</p>

<div style="text-align: center; margin: 30px 0;">
    <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" class="btn btn-primary" style="display: inline-block; padding: 14px 28px; font-size: 1.1rem; border-radius: 8px; text-decoration: none; font-weight: 700; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0, 91, 181, 0.2); background-color: #005bb5; color: white;">90 Dakikalık Deneme Sınavını Başlat</a>
</div>
"""
    },
    {
        "slug": "isvec-vatandaslik-sinavi-kimler-muaf-istisnalar",
        "title": "Kimler İsveç Vatandaşlık Sınavından Muaftır? Tüm İstisnalar (2026)",
        "breadcrumb_name": "Sınavdan Muafiyet Şartları",
        "category": "Göçmenlik & Hukuk",
        "meta_description": "İsveç vatandaşlık sınavına girmek zorunda olmayanlar kimler? Yaş sınırları, eğitim belgeleri (SFI D betyg) ve sağlık muafiyetleri.",
        "lead_paragraph": "İsveç vatandaşlığı başvurusunda bulunacak herkesin sınava girmesi zorunlu mu? Hükümetin belirlediği muafiyet (undantag) kurallarına göre belirli yaş grupları, eğitim dereceleri ve sağlık durumları sınavdan muaftır. Muafiyet şartlarını inceleyin.",
        "cta_title": "Sınav Şartınızı Kontrol Edin ve Hazırlanın",
        "cta_text": "Muafiyet kapsamında değilseniz, vatandaşlık sürecinizin sekteye uğramaması için sınav hazırlıklarına şimdiden başlamalısınız.",
        "cta_button_text": "Sınav Hazırlığına Başla",
        "body_content": """
<p>İsveç'te 2026 yılında yürürlüğe giren yeni vatandaşlık yasası çerçevesinde Medborgarskapsprov zorunlu kılınmış olsa da, yasa koyucu belirli durumdaki kişilerin bu sınavdan muaf tutulmasına (<strong>undantag från provskyldighet</strong>) karar vermiştir. İşte en güncel UHR ve Migrationsverket verilerine göre sınavdan muaf tutulacak gruplar:</p>

<h2>1. Yaş Sınırları Nedir?</h2>
<p>Vatandaşlık yasasına göre belirli yaşın altındaki ve üstündeki kişiler sınav şartından muaftır:</p>
<ul>
    <li><strong>18 Yaşından Küçükler:</strong> İsveç vatandaşlığına başvuran çocuklar sınava girmek zorunda değildir.</li>
    <li><strong>65 Yaşından Büyükler:</strong> Başvuru tarihi itibarıyla 65 yaş ve üzerinde olan adaylar vatandaşlık sınavından tamamen muaftır.</li>
</ul>

<h2>2. Eğitim ve Dil Belgeleri ile Muafiyet</h2>
<p>İsveççe dil yeterliliğini ve toplumsal uyumunu resmi eğitim kurumları aracılığıyla kanıtlamış kişiler sınavdan muaf sayılabilirler:</p>
<ul>
    <li><strong>SFI D Derecesi (Betyg kurs D):</strong> İsveççe Göçmenler İçin Eğitim (SFI) programını D kursunu geçerek (A, B, C, D veya E notu ile) tamamlayanlar ve bunu resmi belge ile kanıtlayanlar sınav yükümlülüğünden muaf tutulmaktadır.</li>
    <li><strong>İsveç Lise veya Üniversite Mezunları:</strong> Eğitim dili İsveççe olan bir liseden (Gymnasieskola) mezun olanlar veya İsveç üniversitelerinde derece tamamlayanlar sınavdan muaftır.</li>
</ul>

<div class="elite-info-box" style="border-radius: 12px; margin: 30px 0;">
    <h3 style="margin-top: 0; color: #1e293b;">Önemli: Sağlık ve Engel Durumu Muafiyeti</h3>
    <p>Zihinsel veya fiziksel engeli, ağır kronik hastalıkları veya sınav koşullarını yerine getirmesine engel olacak kalıcı sağlık sorunları olan kişiler, İsveç'teki yetkili bir hekimden alacakları resmi sağlık raporu (Läkarintyg) ile sınavdan muafiyet talebinde bulunabilirler. Bu raporlar Migrationsverket tarafından titizlikle incelenmektedir.</p>
</div>

<h2>Muaf Değilseniz Ne Yapmalısınız?</h2>
<p>Eğer yukarıdaki muafiyet şartlarından hiçbirini karşılamıyorsanız, vatandaşlık başvurunuzun onaylanması için sınavı geçmek zorundasınız. Sınav hazırlık sürecinizi planlamak ve sınavda sorulabilecek sorulara şimdiden göz atmak için <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" style="color: #005bb5; font-weight: 600; text-decoration: underline;">sverigemedborgarskapsprov.com</a> hazırlık portalını ziyaret edebilirsiniz.</p>

<div style="text-align: center; margin: 30px 0;">
    <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" class="btn btn-primary" style="display: inline-block; padding: 14px 28px; font-size: 1.1rem; border-radius: 8px; text-decoration: none; font-weight: 700; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0, 91, 181, 0.2); background-color: #005bb5; color: white;">Muaf Olmayanlar İçin Hazırlık Soruları</a>
</div>
"""
    },
    {
        "slug": "isvec-vatandaslik-sinavina-nasil-hazirlanilir-kaynaklar",
        "title": "İsveç Vatandaşlık Sınavına Nasıl Hazırlanılır? En İyi Çalışma Kaynakları",
        "breadcrumb_name": "Sınava Nasıl Hazırlanılır",
        "category": "Göçmenlik & Hukuk",
        "meta_description": "Medborgarskapsprov sınavına hazırlanmak için resmi UHR eğitim materyalleri ve sverigemedborgarskapsprov.com sınav çalışma portalı rehberi.",
        "lead_paragraph": "İsveç vatandaşlık sınavını tek seferde geçmek için nasıl bir çalışma yöntemi izlemelisiniz? Resmi kitaplar, toplumsal bilgilendirme dersleri ve hazırlıkta kullanabileceğiniz en iyi interaktif çalışma platformlarını açıklıyoruz.",
        "cta_title": "En Güncel Kaynaklarla Sınava Hazırlanın",
        "cta_text": "İsveç vatandaşlık testi için özel olarak hazırlanmış denemeler, kelime kartları ve konu özetleri ile sınavı garantileyin.",
        "cta_button_text": "Sınav Çalışma Kartlarını İncele",
        "body_content": """
<p>İsveç vatandaşlık sınavı (Medborgarskapsprov) yaklaştıkça, adayların en çok sorduğu soru 'Nereden çalışmalıyım?' oluyor. Sınav konuları geniş bir yelpazeye dağıldığı için düzenli ve doğru kaynaklarla çalışmak hayati önem taşımaktadır. İşte İsveç vatandaşlık sınavına hazırlanırken kullanabileceğiniz en iyi kaynaklar ve yöntemler.</p>

<h2>1. Resmi Kaynak: 'Boken om Sverige' (İsveç Hakkındaki Kitap)</h2>
<p>İsveç belediyeleri tarafından yeni gelen göçmenlere verilen Samhällsorientering derslerinin temel kitabı olan <strong>'Boken om Sverige'</strong> (İsveç Hakkında Kitap), sınav hazırlığının temelini oluşturur. Kitap şu konularda detaylı bilgiler içerir:</p>
<ul>
    <li>İsveç'te bireysel haklar, özgürlükler ve cinsiyet eşitliği.</li>
    <li>İsveç'in yönetim yapısı, seçim sistemi ve belediyeler.</li>
    <li>Sosyal güvenlik, sağlık, çocuk yardımları ve emeklilik sistemi.</li>
</ul>
<p>Bu kitabı internet üzerinden PDF olarak ücretsiz indirebilir veya sesli kitap formatında dinleyebilirsiniz.</p>

<h2>2. Samhällsorientering Portalları</h2>
<p>İsveç devletinin resmi web siteleri olan <em>informationsverige.se</em> ve <em>uhr.se</em> üzerindeki toplumsal bilgi içerikleri, sınavda çıkacak teorik soruların temel kaynağıdır. Bu portallardaki İsveççe makaleleri okumak hem dilinizi geliştirecek hem de sınav konularını kavramanıza yardımcı olacaktır.</p>

<h2>3. En Etkili Yöntem: sverigemedborgarskapsprov.com Denemeleri</h2>
<p>Sadece okumak sınav başarısı için yeterli olmayabilir. Çoktan seçmeli sınav formatına alışmak, İsveççe soru kalıplarını öğrenmek ve zamana karşı kendinizi test etmek için interaktif deneme sınavları çözmek en pratik yöntemdir.</p>

<p>Adaylar için özel olarak geliştirilmiş olan <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" style="color: #005bb5; font-weight: 600; text-decoration: underline;">sverigemedborgarskapsprov.com</a> portalı, gerçek sınav formatında hazırlanmış deneme sınavları, konu konu ayrılmış testler ve İsveççe terim açıklamaları sunarak sınav hazırlık sürecinizi en verimli hale getirir.</p>

<h2>Sınavı Geçmek İçin 3 Altın Tavsiye</h2>
<ol>
    <li><strong>Her Gün Düzenli Çalışın:</strong> Son haftaya yığmak yerine her gün 20-30 dakika İsveç toplumsal yapısı hakkında okumalar yapın.</li>
    <li><strong>Kavramları Ezberleyin:</strong> Hukuk, vergi ve yönetim alanındaki İsveççe terimleri (Örn: <em>Riksdagen</em>, <em>Skatteverket</em>, <em>Grundlagar</em>) öğrenin.</li>
    <li><strong>Sürekli Pratik Yapın:</strong> Bol bol soru çözerek hangi konularda zayıf olduğunuzu tespit edin.</li>
</ol>

<div style="text-align: center; margin: 30px 0;">
    <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" class="btn btn-primary" style="display: inline-block; padding: 14px 28px; font-size: 1.1rem; border-radius: 8px; text-decoration: none; font-weight: 700; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0, 91, 181, 0.2); background-color: #005bb5; color: white;">Çalışmaya Başlamak İçin Tıklayın</a>
</div>
"""
    },
    {
        "slug": "isvec-vatandaslik-sinavi-hakkinda-sikca-sorulanlar",
        "title": "İsveç Vatandaşlık Sınavı Hakkında En Çok Sorulan 10 Soru ve Cevapları",
        "breadcrumb_name": "Sınav Hakkında SSS",
        "category": "Göçmenlik & Hukuk",
        "meta_description": "İsveç vatandaşlık testi (Medborgarskapsprov) ile ilgili en çok merak edilen 10 soru, sınav hakları, ücretler ve sonuç açıklama süreçleri.",
        "lead_paragraph": "İsveç vatandaşlık sınavı (Medborgarskapsprov) ile ilgili akıllarda birçok soru işareti var. Sınav ücretli mi, başarısız olursam ne olur, sınav nerede yapılacak? En çok merak edilen 10 sorunun resmi yanıtlarını bir araya getirdik.",
        "cta_title": "Kafanızdaki Soru İşaretlerini Giderin ve Pratik Yapın",
        "cta_text": "Sınavla ilgili tüm detayları öğrendikten sonra hazırlık sürecini başlatmak için en kapsamlı deneme sınavlarına göz atın.",
        "cta_button_text": "Sıkça Sorulan Soru Denemelerini Çöz",
        "body_content": """
<p>İsveç vatandaşlık sınavı (Medborgarskapsprov) 2026 yılı Haziran ayı itibarıyla yürürlüğe giriyor. Bu yeni döneme dair göçmenler arasında en çok konuşulan ve merak edilen 10 soruyu ve resmi UHR/Migrationsverket yanıtlarını sizler için derledik.</p>

<h2>1. İsveç vatandaşlık sınavı ücretli mi?</h2>
<p>Ağustos 2026'da yapılacak ilk pilot sınavlar (utprövningsprov) için adaylardan herhangi bir sınav katılım ücreti alınmayacaktır. Ancak ilerleyen dönemlerdeki standart sınavlar için cüzi bir başvuru ücreti talep edilmesi gündemdedir.</p>

<h2>2. Sınavda başarısız olursam vatandaşlık başvurum reddedilir mi?</h2>
<p>Hayır, sınavdan kalmanız doğrudan vatandaşlık reddine yol açmaz. Sınavda başarısız olan adaylara tekrar sınava girme hakkı tanınacaktır. Ancak sınavı geçene kadar vatandaşlık başvurunuz sonuçlandırılmayıp askıda bekletilecektir.</p>

<h2>3. Sınava kaç kez girme hakkım var?</h2>
<p>UHR yönergelerine göre adayların vatandaşlık sınavına giriş sayısında herhangi bir kısıtlama veya üst sınır bulunmamaktadır.</p>

<h2>4. Sınavda sözlük veya çevirici kullanabilir miyim?</h2>
<p>Sınav esnasında basılı veya dijital herhangi bir sözlük, kelime listesi, çeviri cihazı veya cep telefonu kullanılması kesinlikle yasaktır.</p>

<h2>5. Sınav ne kadar sürecek ve kaç soru sorulacak?</h2>
<p>Sınav süresi 90 dakikadır. Adaylara çoktan seçmeli formatta yaklaşık 60 soru yöneltilecektir.</p>

<h2>6. İlk vatandaşlık sınavı nerede yapılacak?</h2>
<p>Ağustos 2026'da düzenlenecek olan ilk resmi sınav yalnızca Stockholm şehrindeki belirlenmiş sınav merkezlerinde yapılacaktır.</p>

<h2>7. Sınav soruları önceden yayınlanacak mı?</h2>
<p>Hayır, sınav güvenliğini korumak amacıyla sorular önceden yayınlanmayacaktır. Ancak örnek soru tipleri UHR portalında paylaşılacaktır.</p>

<h2>8. Kimler vatandaşlık sınavından muaftır?</h2>
<p>18 yaşından küçükler, 65 yaşından büyükler, SFI D kursu betyg derecesine sahip olanlar ve ciddi sağlık engeli doktor raporu ile kanıtlanmış olanlar sınavdan muaftır.</p>

<h2>9. Sınav sonuçları ne zaman ve nasıl açıklanır?</h2>
<p>Sınav sonuçları yaklaşık 3-4 hafta içinde UHR portalı üzerinden açıklanacak ve elektronik ortamda doğrudan Migrationsverket sistemine gönderilecektir.</p>

<h2>10. Sınava hazırlık için en iyi platform hangisidir?</h2>
<p>Sınav formatına en yakın soru tiplerini çözmek ve interaktif olarak çalışmak için Türkiye kökenli göçmenlerin en çok tercih ettiği hazırlık sitesi olan <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" style="color: #005bb5; font-weight: 600; text-decoration: underline;">sverigemedborgarskapsprov.com</a> platformunu kullanabilirsiniz.</p>

<div style="text-align: center; margin: 30px 0;">
    <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" class="btn btn-primary" style="display: inline-block; padding: 14px 28px; font-size: 1.1rem; border-radius: 8px; text-decoration: none; font-weight: 700; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0, 91, 181, 0.2); background-color: #005bb5; color: white;">SSS Deneme Sınavlarını Çözmeye Başla</a>
</div>
"""
    },
    {
        "slug": "isvec-vatandaslik-sinavi-pilot-uygulama-utprovningsprov",
        "title": "Ağustos 2026 Pilot İsveç Vatandaşlık Sınavı (Utprövningsprov) Nedir?",
        "breadcrumb_name": "Pilot Vatandaşlık Sınavı",
        "category": "Göçmenlik & Hukuk",
        "meta_description": "UHR'nin Ağustos 2026'da düzenleyeceği pilot vatandaşlık sınavı (utprövningsprov) nedir, katılım şartları ve ücretsiz deneme süreci.",
        "lead_paragraph": "İsveç vatandaşlık sınavı sisteminin ilk adımı olan Ağustos 2026 pilot uygulaması (Utprövningsprov) hakkında resmi duyurular yapıldı. Bu pilot sınavın amacı nedir, kimler katılabilir ve gelecekteki sınavlar için ne anlama geliyor?",
        "cta_title": "Pilot Sınav Formatına Şimdiden Alışın",
        "cta_text": "Pilot sınavda sorulabilecek örnek soruları incelemek ve İsveç vatandaşlık sınavına sıfır hata ile hazırlanmak için hemen sitemizi ziyaret edin.",
        "cta_button_text": "Pilot Sınav Sorularını Deneyin",
        "body_content": """
<p>İsveç Yükseköğretim Kurulu (UHR), vatandaşlık sınavını ülke genelinde yaygınlaştırmadan önce sistemin teknik altyapısını ve soruların uygunluğunu test etmek üzere bir **pilot sınav (utprövningsprov)** gerçekleştireceğini duyurdu. 15 Ağustos 2026 tarihinde yapılacak olan bu pilot sınav, yeni sistemin göçmenler üzerindeki ilk yansıması olacaktır.</p>

<h2>Pilot Sınavın (Utprövningsprov) Amacı Nedir?</h2>
<p>UHR'nin açıklamasına göre pilot sınavın temel hedefleri şunlardır:</p>
<ul>
    <li>Hazırlanan çoktan seçmeli soruların anlaşılırlığını ve zorluk derecesini ölçmek.</li>
    <li>Sınav gözetimi, kağıt dağıtımı ve optik okuma süreçlerindeki olası aksaklıkları tespit etmek.</li>
    <li>90 dakikalık sınav süresinin 60 soru için yeterli olup olmadığını doğrulamak.</li>
</ul>

<div class="elite-info-box" style="border-radius: 12px; margin: 30px 0;">
    <h3 style="margin-top: 0; color: #1e293b;">Katılımcı Seçimi Nasıl Yapılacak?</h3>
    <p>Pilot sınava katılacak kişiler Migrationsverket tarafından vatandaşlık başvurusu devam eden adaylar arasından rastgele veya belirli kriterlere göre seçilecektir. Davet edilen kişilerin sınava katılımı tamamen ücretsizdir ve bu sınavda başarılı olanlar resmi olarak sınav şartını yerine getirmiş kabul edilecektir.</p>
</div>

<h2>Sınav Sonrası Süreç Nasıl İşleyecek?</h2>
<p>Pilot sınavdan elde edilen istatistiksel veriler ışığında, sorular revize edilecek ve 2027 yılından itibaren düzenlenecek kalıcı sınavların standartları belirlenecektir. Pilot sınava davet edilmek, vatandaşlık sürecinizi hızlandırmak için büyük bir şanstır, bu nedenle davet mektubu aldığınız takdirde sınava iyi hazırlanarak katılım sağlamanız önerilir.</p>

<p>Bu pilot sınavın müfredatına, soru dağılımına ve örnek sorularına erişmek için <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" style="color: #005bb5; font-weight: 600; text-decoration: underline;">sverigemedborgarskapsprov.com</a> hazırlık portalından yararlanabilir, sınav günü stresinizi en aza indirebilirsiniz.</p>

<div style="text-align: center; margin: 30px 0;">
    <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" class="btn btn-primary" style="display: inline-block; padding: 14px 28px; font-size: 1.1rem; border-radius: 8px; text-decoration: none; font-weight: 700; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0, 91, 181, 0.2); background-color: #005bb5; color: white;">Pilot Sınavı Denemesini Çöz</a>
</div>
"""
    },
    {
        "slug": "isvec-vatandaslik-sinavi-dil-ve-isvecce-seviyesi",
        "title": "İsveç Vatandaşlık Sınavı Dil Şartı: İsveççe Seviyesi Ne Olmalıdır?",
        "breadcrumb_name": "Sınav Dil Şartı Seviyesi",
        "category": "Göçmenlik & Hukuk",
        "meta_description": "İsveç vatandaşlık sınavına girmek için hangi seviyede İsveççe bilmek gerekiyor? Dil sınavı (Språkprov) ne zaman başlıyor?",
        "lead_paragraph": "İsveç vatandaşlık sınavının en çok tartışılan yönlerinden biri dil şartıdır. Sınavın tamamen İsveççe olacağı göz önüne alındığında, adayların hangi seviyede dil bilmesi gerekiyor? Gelecekte planlanan Språkprov dil sınavı detaylarını inceliyoruz.",
        "cta_title": "İsveççe Terim Bilginizi Deneme Sınavlarıyla Artırın",
        "cta_text": "Vatandaşlık sınavında sorulacak soruları anlamak için gerekli olan İsveççe hukuk, tarih ve politika terimlerini hazırlık portalımızdan öğrenin.",
        "cta_button_text": "İsveççe Sınav Sorularını Çöz",
        "body_content": """
<p>İsveç vatandaşlık testi (Medborgarskapsprov) ile ilgili göçmenlerin en çok zorlanacağı konu şüphesiz sınav dilidir. Sınavda herhangi bir İngilizce veya Türkçe çeviri desteği olmayacağı için, soruları anlayıp doğru cevaplayabilmek adına belirli bir seviyede **İsveççe (Svenska)** bilgisi yasal bir gereklilik haline gelmektedir.</p>

<h2>İsveççe Dil Seviyesi Ne Olmalı?</h2>
<p>Resmi olarak sınav için spesifik bir dil sertifikası (TISUS vb.) sunma zorunluluğu olmasa da, UHR'nin hazırladığı soruların dil karmaşıklığı **SFI D Kursu (Avrupa Ortak Dil Çerçevesi'ne göre A2/B1 seviyesi)** düzeyindedir. Adayların sınavı başarıyla tamamlayabilmesi için şu dil becerilerine sahip olması gerekir:</p>
<ul>
    <li>İsveççe gazete haberlerini, resmi duyuruları ve mektupları rahatça okuyup anlayabilmek.</li>
    <li>Hukuk, siyaset ve sosyal güvenlik alanındaki temel kavramları (Örn: <em>riksdag</em>, <em>regering</em>, <em>lagstiftning</em>, <em>tingsrätt</em>) bilmek.</li>
    <li>Çoktan seçmeli sorulardaki ince anlam farklarını ayırt edebilmek.</li>
</ul>

<h2>2027 Dil Sınavı (Språkprov) Yolda!</h2>
<p>Şu an 2026 yılında yürürlüğe giren sınav sadece 'toplumsal bilgi' (samhällskunskap) konularını içermektedir. Ancak İsveç hükümetinin planları doğrultusunda, **2027 yılı itibarıyla** toplumsal bilgi sınavına ek olarak ayrı bir **resmi İsveççe dil sınavı (Språkprov)** da vatandaşlık şartları arasına eklenecektir. Bu nedenle İsveççe öğrenme sürecini hızlandırmak gelecekteki başvurular için de hayati derecede önemlidir.</p>

<div class="elite-info-box" style="border-radius: 12px; margin: 30px 0;">
    <h3 style="margin-top: 0; color: #1e293b;">İsveççe Çalışma Pratiği Nasıl Yapılmalı?</h3>
    <p>Toplumsal bilgi konularını doğrudan İsveççe kaynaklardan okumak en iyi yöntemdir. Türkçe çevirilerle konuyu anlamak kolay olsa da, sınav anında sorular İsveççe olacağı için kavramların İsveççe karşılıklarına aşina olmak gerekir.</p>
</div>

<p>İsveç vatandaşlık sınavında çıkacak İsveççe soruların benzerlerini çözmek, dil seviyenizin sınav için yeterli olup olmadığını test etmek için <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" style="color: #005bb5; font-weight: 600; text-decoration: underline;">sverigemedborgarskapsprov.com</a> portalındaki deneme sınavlarını süre kısıtlamalı olarak çözerek kendinizi geliştirebilirsiniz.</p>

<div style="text-align: center; margin: 30px 0;">
    <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" class="btn btn-primary" style="display: inline-block; padding: 14px 28px; font-size: 1.1rem; border-radius: 8px; text-decoration: none; font-weight: 700; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0, 91, 181, 0.2); background-color: #005bb5; color: white;">İsveççe Deneme Sınavlarını Başlat</a>
</div>
"""
    }
]

def generate_post(post):
    slug = post["slug"]
    title = post["title"]
    breadcrumb_name = post["breadcrumb_name"]
    category = post["category"]
    meta_description = post["meta_description"]
    lead_paragraph = post["lead_paragraph"]
    body_content = post["body_content"]
    cta_title = post["cta_title"]
    cta_text = post["cta_text"]
    cta_button_text = post["cta_button_text"]

    iso_date = "2026-05-22"
    date_turkish = "22 Mayıs 2026"

    schema_markup = f"""    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BlogPosting",
      "headline": "{title}",
      "image": "https://isvecenasilgelinir.com/assets/images/{slug}.png",
      "datePublished": "{iso_date}T09:00:00+02:00",
      "dateModified": "{iso_date}T12:00:00+02:00",
      "author": {{
        "@type": "Organization",
        "name": "İsveç'e Nasıl Gelinir?"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "İsveç'e Nasıl Gelinir?",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://isvecenasilgelinir.com/assets/images/logo.png"
        }}
      }},
      "description": "{meta_description}"
    }}
    </script>"""

    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template = f.read()

    # Format HTML
    html_output = template.format(
        TITLE=title,
        SLUG=slug,
        META_DESCRIPTION=meta_description,
        SCHEMA_MARKUP=schema_markup,
        BREADCRUMB_NAME=breadcrumb_name,
        CATEGORY=category,
        DATE_TURKISH=date_turkish,
        LEAD_PARAGRAPH=lead_paragraph,
        BODY_CONTENT=body_content,
        CTA_TITLE=cta_title,
        CTA_TEXT=cta_text,
        CTA_BUTTON_TEXT=cta_button_text
    )

    post_dir = os.path.join(BASE_DIR, "blog", slug)
    os.makedirs(post_dir, exist_ok=True)
    post_file = os.path.join(post_dir, "index.html")

    with open(post_file, 'w', encoding='utf-8') as f:
        f.write(html_output)

    print(f"[SUCCESS] Created blog post at: {post_file}")

def prepend_card(file_path, slug, title, lead_paragraph, category, date_turkish, is_blog_index=False):
    if not os.path.exists(file_path):
        print(f"Error: Cannot find list page to update: {file_path}")
        return
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Strip featured-post class and associated styles from existing featured posts
    content = re.sub(r'class="news-card featured-post"', 'class="news-card"', content)
    content = re.sub(r'style="height: 400px; object-fit: cover;"', '', content)

    # 2. Build the new card
    img_path = f"../assets/images/{slug}.png" if is_blog_index else f"assets/images/{slug}.png"
    link_path = f"{slug}/" if is_blog_index else f"blog/{slug}/"
    contact_path = f"../iletisim/" if is_blog_index else f"iletisim/"
    
    category_btn_text = "Hukuki Danışmanlık"

    card_html = f"""                    <article class="news-card featured-post">
                        <div class="news-img-wrapper">
                            <img src="{img_path}" alt="{title}" class="news-img">
                        </div>
                        <div class="news-content">
                            <span class="news-category">{category}</span>
                            <h3><a href="{link_path}">{title}</a></h3>
                            <p>{lead_paragraph}</p>
                            <a href="{link_path}" class="btn-read-more">Hemen İncele &rarr;</a>
                            <div class="news-meta-footer">
                                <span class="news-date">{date_turkish}</span>
                                <a href="{contact_path}" class="card-contact-link" style="color: #005bb5;">{category_btn_text}</a>
                            </div>
                        </div>
                    </article>"""

    # 3. Inject new card inside <div class="news-grid">
    content = re.sub(r'(<div class="news-grid">)', r'\1\n' + card_html, content, count=1)

    # 4. Limit cards to exactly 5 on homepage (1 featured + 4 normal)
    if not is_blog_index:
        grid_start_tag = '<div class="news-grid">'
        grid_start_idx = content.find(grid_start_tag)
        if grid_start_idx != -1:
            wrapper_tag = '<div class="view-all-wrapper"'
            wrapper_idx = content.find(wrapper_tag, grid_start_idx)
            if wrapper_idx != -1:
                grid_content_end = content.rfind('</div>', grid_start_idx, wrapper_idx)
                if grid_content_end != -1:
                    grid_section = content[grid_start_idx + len(grid_start_tag):grid_content_end]
                    articles = re.findall(r'(<article[^>]*>.*?</article>)', grid_section, re.DOTALL)
                    if len(articles) > 5:
                        kept_articles = articles[:5]
                        new_grid_content = "\n" + "\n".join(kept_articles) + "\n                    "
                        content = (
                            content[:grid_start_idx + len(grid_start_tag)] +
                            new_grid_content +
                            content[grid_content_end:]
                        )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Prepended card to listing: {file_path}")

def update_seo_script(slug, iso_date):
    script_path = os.path.join(BASE_DIR, "scratch/fix_seo_issues.py")
    if not os.path.exists(script_path):
        print(f"Error: SEO script not found at {script_path}")
        return
        
    with open(script_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    match = re.search(r'(DATE_MAP\s*=\s*\{)', content)
    if match:
        target = match.group(1)
        new_target = target + f'\n    f"{{BASE_URL}}/blog/{slug}/": "{iso_date}",'
        content = content.replace(target, new_target)
        
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated date mapping in SEO script for slug: {slug}")
    else:
        print("Warning: Could not find DATE_MAP in SEO script to update.")

def main():
    print("Generating 10 Swedish Citizenship Test blog posts...")
    
    # 1. Generate post index files
    for post in POSTS:
        generate_post(post)
        
    # 2. Prepend cards to home page index.html and blog index.html
    # We prepend them in reverse order (from 10 to 1) so that post 1 ends up on top of the list!
    home_index = os.path.join(BASE_DIR, "index.html")
    blog_index = os.path.join(BASE_DIR, "blog/index.html")
    
    for post in reversed(POSTS):
        prepend_card(home_index, post["slug"], post["title"], post["lead_paragraph"], post["category"], "22 Mayıs 2026", is_blog_index=False)
        prepend_card(blog_index, post["slug"], post["title"], post["lead_paragraph"], post["category"], "22 Mayıs 2026", is_blog_index=True)
        update_seo_script(post["slug"], "2026-05-22")

    print("\n✅ Generation process completed!")

if __name__ == "__main__":
    main()
