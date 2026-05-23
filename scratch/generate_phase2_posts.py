#!/usr/bin/env python3
import os
import re
from datetime import datetime

BASE_DIR = "/Users/fatnar/Documents/isvecenasilgelinir"
TEMPLATE_PATH = os.path.join(BASE_DIR, "agents/blog_template.html")

POSTS = [
    {
        "slug": "isvec-vatandaslik-sartlari-2026",
        "title": "İsveç Vatandaşlık Şartları 2026: Yeni Yasa ve Tüm Kurallar",
        "breadcrumb_name": "Vatandaşlık Şartları 2026",
        "category": "Göçmenlik & Hukuk",
        "meta_description": "2025 ve 2026 yıllarında yürürlüğe giren yeni İsveç vatandaşlık şartları, oturum süreleri, borçsuzluk kuralları ve yeni vatandaşlık sınavı gereksinimleri.",
        "lead_paragraph": "İsveç vatandaşlığına geçmek isteyenler için 2025 ve 2026 yıllarında yürürlüğe giren yeni yasa ve kurallarla birlikte başvuru şartları tamamen güncellendi. İşte oturum süreleri, borçsuzluk, kimlik kanıtı ve yeni vatandaşlık sınavı dahil bilmeniz gereken tüm şartlar.",
        "cta_title": "Yeni Şartlardaki En Kritik Engel: Vatandaşlık Sınavı",
        "cta_text": "2026 yılı vatandaşlık şartları arasında en çok dikkat etmeniz gereken adım, zorunlu hale getirilen Medborgarskapsprov vatandaşlık sınavıdır. Sınavda çıkacak tüm konulara hazırlık portalımızdan çalışabilirsiniz.",
        "cta_button_text": "Vatandaşlık Sınavına Şimdiden Çalışın",
        "body_content": """
<p>İsveç'te yaşayıp vatandaşlık (Medborgarskap) almayı planlayan göçmenler için süreç son dönemde yapılan yasal reformlarla daha da yapılandırılmış hale geldi. İsveç hükümeti, entegrasyonu artırmak amacıyla <strong>İsveç vatandaşlık şartları</strong> üzerinde önemli güncellemeler gerçekleştirdi. Bu rehberde, 2025 ve 2026 yılları itibarıyla geçerli olan tüm güncel kuralları tek bir yerde topladık.</p>

<h2>İsveç Vatandaşlığı Almanın Temel Şartları</h2>
<p>İsveç Göçmen Dairesi (Migrationsverket) tarafından aranan temel vatandaşlık şartları genel hatlarıyla şunlardır:</p>
<ul>
    <li><strong>Geçerli Bir Kimlik Kanıtı (Styrkt identitet):</strong> Pasaport veya resmi ulusal kimlik kartı ile kimliğin şüpheye yer bırakmayacak şekilde kanıtlanması gerekir.</li>
    <li><strong>Sürekli Oturum İzni (Permanent uppehållstillstånd - PUT):</strong> Vatandaşlığa başvurmadan önce İsveç'te sürekli oturum hakkına veya AB vatandaşları için oturum hakkına (uppehållsrätt) sahip olmanız şarttır.</li>
    <li><strong>İsveç'te Oturum Süresi (Hemvisttid):</strong> Genellikle İsveç'te kesintisiz olarak en az 5 yıl yaşamış olmanız gerekir. (İsveç vatandaşı ile evli olanlar için bu süre 3 yıldır).</li>
    <li><strong>Temiz Sicil ve Dürüst Yaşam (Hedervärt levnadssätt):</strong> Vergi dairesi (Skatteverket) veya icra dairesine (Kronofogden) ödenmemiş borcunuzun bulunmaması ve adli sicilinizin temiz olması gerekir.</li>
</ul>

<h2>2026 Yılı Yeni Yasa Değişiklikleri: Dil ve Sınav Şartı</h2>
<p>İsveç vatandaşlık şartları 2026 yılı ile birlikte en köklü değişimini yaşadı. Artık İsveç vatandaşlığına geçecek kişilerin, İsveç yasal sistemi, demokrasisi, sosyal güvenlik yapısı ve iş piyasası hakkındaki bilgilerini ölçen **zorunlu vatandaşlık sınavını (Medborgarskapsprov)** geçmeleri gerekmektedir.</p>
<div class="elite-info-box" style="border-radius: 12px; margin: 30px 0;">
    <h3 style="margin-top: 0; color: #1e293b;">Sınav Hangi Seviyede İsveççe Olacak?</h3>
    <p>Sınav tamamen İsveççe olarak yapılacaktır. Adayların soruları okuyup anlayabilmeleri için en az SFI D seviyesinde (A2/B1 okuma-anlama düzeyi) İsveççe bilgisine sahip olmaları kritik bir şarttır.</p>
</div>

<h2>İsveç Vatandaşlık Şartları Karşılaştırma Tablosu</h2>
<table class="data-table-clean" style="width: 100%; border-collapse: collapse; margin: 20px 0;">
    <thead>
        <tr style="background-color: #f1f5f9;">
            <th style="padding: 12px; border: 1px solid #e2e8f0; text-align: left;">Kriter</th>
            <th style="padding: 12px; border: 1px solid #e2e8f0; text-align: left;">Genel Şartlar</th>
            <th style="padding: 12px; border: 1px solid #e2e8f0; text-align: left;">Özel İstisnalar (Evlilik/Mülteci)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="padding: 12px; border: 1px solid #e2e8f0; font-weight: bold;">Oturum Süresi</td>
            <td style="padding: 12px; border: 1px solid #e2e8f0;">Kesintisiz 5 Yıl</td>
            <td style="padding: 12px; border: 1px solid #e2e8f0;">İsveç vatandaşı ile evlilikte 3 Yıl, mültecilerde 4 Yıl</td>
        </tr>
        <tr>
            <td style="padding: 12px; border: 1px solid #e2e8f0; font-weight: bold;">Oturum Statüsü</td>
            <td style="padding: 12px; border: 1px solid #e2e8f0;">Sürekli Oturum İzni (PUT)</td>
            <td style="padding: 12px; border: 1px solid #e2e8f0;">AB vatandaşları için 5 yıllık kesintisiz oturum hakkı</td>
        </tr>
        <tr>
            <td style="padding: 12px; border: 1px solid #e2e8f0; font-weight: bold;">Borç ve Sicil Durumu</td>
            <td style="padding: 12px; border: 1px solid #e2e8f0;">Kronofogden'de sıfır borç kaydı</td>
            <td style="padding: 12px; border: 1px solid #e2e8f0;">İşlenen suçlar için belirli bekleme süreleri (karenstid)</td>
        </tr>
        <tr>
            <td style="padding: 12px; border: 1px solid #e2e8f0; font-weight: bold;">Entegrasyon Testi</td>
            <td style="padding: 12px; border: 1px solid #e2e8f0;">Zorunlu vatandaşlık sınavını geçmek</td>
            <td style="padding: 12px; border: 1px solid #e2e8f0;">65 yaş üstü ve 18 yaş altı adaylar sınavdan muaftır</td>
        </tr>
    </tbody>
</table>

<p>İsveç vatandaşlığına geçiş sürecinde yeni şartların getirdiği bu zorunlu sınavı başarıyla tamamlamak için <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" style="color: #005bb5; font-weight: 600; text-decoration: underline;">sverigemedborgarskapsprov.com</a> hazırlık portalındaki deneme testlerini çözerek sınav formatını ve İsveççe terimleri şimdiden öğrenebilirsiniz.</p>

<div style="text-align: center; margin: 30px 0;">
    <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" class="btn btn-primary" style="display: inline-block; padding: 14px 28px; font-size: 1.1rem; border-radius: 8px; text-decoration: none; font-weight: 700; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0, 91, 181, 0.2); background-color: #005bb5; color: white;">İsveç Vatandaşlık Sınavı Denemelerini Çöz</a>
</div>
"""
    },
    {
        "slug": "isvec-vatandaslik-basvurusu",
        "title": "İsveç Vatandaşlık Başvurusu Nasıl Yapılır? Adım Adım Başvuru Rehberi",
        "breadcrumb_name": "Vatandaşlık Başvurusu",
        "category": "Göçmenlik & Hukuk",
        "meta_description": "İsveç vatandaşlık başvurusu süreci, online başvuru adımları, gerekli belgeler, işlem süreleri ve başvuru takip rehberi.",
        "lead_paragraph": "İsveç vatandaşlığına (Medborgarskap) başvurmak isteyen göçmenler için başvuru süreci, gerekli belgeler, Migrationsverket online portalı ve takip aşamalarını içeren en güncel adım adım rehber.",
        "cta_title": "Başvuru Sürecinde Sınav Şartına Dikkat Edin",
        "cta_text": "Migrationsverket vatandaşlık başvurunuzu değerlendirirken sizden resmi vatandaşlık sınavına girmenizi isteyecektir. Başvurunuzun hızlı sonuçlanması için sınav hazırlık portalımızdan pratik yapın.",
        "cta_button_text": "İnteraktif Sınav Çalışma Portalına Git",
        "body_content": """
<p>İsveç'te gerekli oturum sürelerini tamamladıktan ve diğer şartları karşıladıktan sonra yapmanız gereken adım resmi **İsveç vatandaşlık başvurusu** sürecini başlatmaktır. Başvurular doğrudan Göçmen Dairesi'ne (Migrationsverket) iletilir. Bu yazımızda, başvurunuzu hatasız yapabilmeniz için izlemeniz gereken resmi adımları sıraladık.</p>

<h2>1. Başvuru Öncesi Hazırlık ve Belgeler</h2>
<p>Vatandaşlık başvurusunu online olarak doldurmaya başlamadan önce aşağıdaki belgelerin yanınızda hazır olduğundan emin olmalısınız:</p>
<ul>
    <li><strong>Orijinal Pasaportunuz:</strong> Migrationsverket, başvuru sürecinin ilerleyen aşamalarında kimliğinizi doğrulamak için orijinal pasaportunuzu posta yoluyla talep edecektir.</li>
    <li><strong>Sürekli Oturum Belgeniz (PUT):</strong> İsveç'teki yasal oturum kartınızın bilgileri.</li>
    <li><strong>Eş/Çocuk Bilgileri:</strong> Eğer çocuklarınızı da başvurunuza dahil edecekseniz, onların kimlik belgeleri ve nüfus kayıt örnekleri.</li>
</ul>

<h2>2. Migrationsverket Portalı Üzerinden Online Başvuru</h2>
<p>İsveç vatandaşlığı başvurusu en hızlı ve güvenli şekilde Migrationsverket'in resmi internet sitesi üzerinden online olarak yapılır:</p>
<ul>
    <li>Online hizmetler kısmından <strong>BankID</strong> veya Mobil BankID kullanarak giriş yapın.</li>
    <li>Vatandaşlık başvuru formunu (Ansökan om medborgarskap) seçip kişisel bilgilerinizi, İsveç'e geliş tarihinizi ve yurtdışı seyahatlerinizi doldurun.</li>
    <li>Sürecin sonunda 1500 SEK tutarındaki başvuru harcını kredi kartı veya internet bankacılığı ile ödeyin.</li>
</ul>

<h2>3. Sınav Daveti ve Değerlendirme Aşaması</h2>
<p>2026 yılı itibarıyla yürürlüğe giren yeni yasa uyarınca, başvurunuz incelenirken Migrationsverket size resmi bir vatandaşlık sınav davet mektubu (kallelse) gönderecektir. Sınavı başarıyla geçtikten sonra sınav sonucunuz otomatik olarak dosyanıza işlenecek ve karar aşamasına geçilecektir.</p>

<div class="elite-info-box" style="border-radius: 12px; margin: 30px 0;">
    <h3 style="margin-top: 0; color: #1e293b;">Tavsiye: Seyahatlerinizi Doğru Hesaplayın</h3>
    <p>Başvuru formunda İsveç dışına yaptığınız tüm tatil ve seyahatleri gün gün yazmanız istenir. Yıllık toplamda 6 haftayı geçen yurtdışı kalış süreleriniz, 5 yıllık zorunlu oturum süresinden (hemvisttid) düşülebilir.</p>
</div>

<p>Vatandaşlık başvurunuzun olumlu sonuçlanması için sınav daveti aldığınızda Medborgarskapsprov'u tek seferde geçmeniz son derece önemlidir. Sınava en iyi şekilde hazırlanmak için <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" style="color: #005bb5; font-weight: 600; text-decoration: underline;">sverigemedborgarskapsprov.com</a> adresini ziyaret edin.</p>

<div style="text-align: center; margin: 30px 0;">
    <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" class="btn btn-primary" style="display: inline-block; padding: 14px 28px; font-size: 1.1rem; border-radius: 8px; text-decoration: none; font-weight: 700; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0, 91, 181, 0.2); background-color: #005bb5; color: white;">Vatandaşlık Sınavı Sorularını Çöz</a>
</div>
"""
    },
    {
        "slug": "isvec-vatandasligi-kac-para-ucretler",
        "title": "İsveç Vatandaşlığı Kaç Para? 2026 Güncel Başvuru Ücretleri",
        "breadcrumb_name": "Vatandaşlık Ücretleri",
        "category": "Göçmenlik & Hukuk",
        "meta_description": "İsveç vatandaşlığı başvuru harçları, pasaport yenileme, evrak çevirisi ve vatandaşlık sınavı kayıt ücretlerinin detaylı dökümü.",
        "lead_paragraph": "İsveç vatandaşlığına başvurunun maliyeti nedir? Migrationsverket başvuru harcı, pasaport yenileme, evrak çevirileri ve yeni vatandaşlık sınavı maliyetleri hakkında 2026 yılı güncel bilgiler.",
        "cta_title": "Sınavda Hata Yapıp Ekstra Masraf Ödemeyin",
        "cta_text": "İsveç vatandaşlık sınavında başarısız olmak hem sürecinizi uzatır hem de gelecekteki olası tekrar sınavı harçları nedeniyle bütçenize yük getirir. Portalımızdaki testlerle tek seferde geçmeyi garantileyin.",
        "cta_button_text": "Sınav Hazırlığına Hemen Başla",
        "body_content": """
<p>İsveç vatandaşlığı almayı düşünen birçok göçmen için sürecin finansal boyutu da merak konusudur. Resmi başvurudan pasaport alımına kadar geçen süreçte karşınıza çıkacak masrafları önceden bilmek planlama yapmanızı kolaylaştırır. Peki, **İsveç vatandaşlığı kaç para** ve hangi harç ödemeleri zorunludur? İşte güncel kalemler.</p>

<h2>Migrationsverket Vatandaşlık Başvuru Harcı</h2>
<p>İsveç vatandaşlığı başvurusu yaparken devlete ödenmesi gereken standart resmi harç tutarı <strong>1.500 SEK</strong> (İsveç Kronu) olarak belirlenmiştir. Bu ücret, başvurunuz online olarak sisteme yüklendiği esnada tahsil edilir. Başvurunuzun olumsuz sonuçlanması durumunda bu harç bedeli **iade edilmez**.</p>

<h3>Uzatma ve Çocuklar İçin Ücretler</h3>
<ul>
    <li>18 yaşından küçük çocuklar, ebeveynlerinin başvurusu ile birlikte başvurduklarında herhangi bir ek başvuru ücreti ödemezler (ücretsizdir).</li>
    <li>Tek başına başvuran çocuklar veya özel yasal vasileri aracılığıyla başvuran küçükler için ücret 175 SEK'tir.</li>
    <li>Vatansız (stateless) kişiler belirli şartlar altında bu harçtan muaf tutulabilmektedir.</li>
</ul>

<h2>Sınav ve Diğer Ekstra Maliyetler</h2>
<p>Sadece başvuru harcıyla süreç bitmemektedir. Adayların karşısına çıkabilecek diğer maliyetler şu şekildedir:</p>
<table class="data-table-clean" style="width: 100%; border-collapse: collapse; margin: 20px 0;">
    <thead>
        <tr style="background-color: #f1f5f9;">
            <th style="padding: 12px; border: 1px solid #e2e8f0; text-align: left;">Maliyet Kalemi</th>
            <th style="padding: 12px; border: 1px solid #e2e8f0; text-align: left;">Ortalama Tutar (SEK)</th>
            <th style="padding: 12px; border: 1px solid #e2e8f0; text-align: left;">Açıklama</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="padding: 12px; border: 1px solid #e2e8f0; font-weight: bold;">Başvuru Harcı</td>
            <td style="padding: 12px; border: 1px solid #e2e8f0;">1.500 SEK</td>
            <td style="padding: 12px; border: 1px solid #e2e8f0;">Yetişkin adaylar için Migrationsverket harcı</td>
        </tr>
        <tr>
            <td style="padding: 12px; border: 1px solid #e2e8f0; font-weight: bold;">Vatandaşlık Sınavı</td>
            <td style="padding: 12px; border: 1px solid #e2e8f0;">Ücretsiz (Pilot Dönemi)</td>
            <td style="padding: 12px; border: 1px solid #e2e8f0;">Ağustos 2026 sınavı ücretsizdir. İleride cüzi bir ücret talep edilebilir.</td>
        </tr>
        <tr>
            <td style="padding: 12px; border: 1px solid #e2e8f0; font-weight: bold;">Resmi Evrak Çevirileri</td>
            <td style="padding: 12px; border: 1px solid #e2e8f0;">500 - 1.500 SEK</td>
            <td style="padding: 12px; border: 1px solid #e2e8f0;">Türkiye'den alınan doğum belgesi vb. evrakların yetkili tercüman çevirileri</td>
        </tr>
        <tr>
            <td style="padding: 12px; border: 1px solid #e2e8f0; font-weight: bold;">Pasaport Cüzdan Ücreti</td>
            <td style="padding: 12px; border: 1px solid #e2e8f0;">400 SEK</td>
            <td style="padding: 12px; border: 1px solid #e2e8f0;">Vatandaşlık onaylandıktan sonra İsveç Polisi'ne ödenen pasaport defter bedeli</td>
        </tr>
    </tbody>
</table>

<div class="elite-info-box" style="border-radius: 12px; margin: 30px 0;">
    <h3 style="margin-top: 0; color: #1e293b;">Bütçe Dostu Hazırlık İpucu</h3>
    <p>Vatandaşlık sınavında başarısız olup süreci uzatmak yerine, ilk seferde geçmek en ekonomik yoldur. Deneme sınavları ve interaktif konu anlatımları için hazırlık portalımızı kullanarak sınav başarınızı garantileyebilirsiniz.</p>
</div>

<p>İsveç vatandaşlık sınavı hazırlıklarında bütçenizi ve zamanınızı korumak adına en etkili interaktif denemeleri sunan <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" style="color: #005bb5; font-weight: 600; text-decoration: underline;">sverigemedborgarskapsprov.com</a> sitesindeki ücretsiz ve premium kaynakları inceleyebilirsiniz.</p>

<div style="text-align: center; margin: 30px 0;">
    <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" class="btn btn-primary" style="display: inline-block; padding: 14px 28px; font-size: 1.1rem; border-radius: 8px; text-decoration: none; font-weight: 700; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0, 91, 181, 0.2); background-color: #005bb5; color: white;">Sınav Çalışmalarına Hemen Başlayın</a>
</div>
"""
    },
    {
        "slug": "isvec-vatandasi-ile-evlilik",
        "title": "İsveç Vatandaşı ile Evlilik ve Oturum İzni: Vatandaşlık Şartları",
        "breadcrumb_name": "Evlilik ve Vatandaşlık",
        "category": "Göçmenlik & Hukuk",
        "meta_description": "İsveç vatandaşı ile evlilik veya sambo (birlikte yaşam) yoluyla oturum izni alma, 3 yılda vatandaşlık kazanma şartları ve sınav yükümlülüğü.",
        "lead_paragraph": "İsveç vatandaşı biriyle evlenmek veya sambo (birlikte yaşama) ilişkisi kurmak İsveç'te oturum izni ve vatandaşlık hakkı sağlar mı? Eş durumundan vatandaşlığa geçiş süreleri ve şartları.",
        "cta_title": "Evlilik Yolunda Vatandaşlık Sınavına Şimdiden Hazırlanın",
        "cta_text": "Eş durumundan 3 yılda İsveç vatandaşlığına başvururken de zorunlu vatandaşlık sınavını (Medborgarskapsprov) geçmeniz gerekmektedir. Hazırlık testlerimizi çözerek kendinizi sınayın.",
        "cta_button_text": "Vatandaşlık Testlerini Çözmeye Başla",
        "body_content": """
<p>İsveç vatandaşı olan biriyle evlenmek veya birlikte yaşamak (Sambo), İsveç'e taşınmak ve burada yeni bir hayat kurmak isteyenler için yasal yollardan biridir. Ancak yaygın inanışın aksine, bir İsveç vatandaşıyla evlenmek size **doğrudan veya otomatik olarak** İsveç vatandaşlığı kazandırmaz. Süreç belirli aşamalardan ve şartlardan oluşur.</p>

<h2>Evlilik ve Sambo Yoluyla Oturum İzni (Uppehållstillstånd)</h2>
<p>İsveç vatandaşı bir eş veya partner üzerinden İsveç'e gelebilmek için öncelikle aile birleşimi oturum iznine başvurulmalıdır. Bu başvuruda göç dairesinin aradığı en önemli şartlardan biri **Geçim ve Barınma Şartı (Försörjningskrav)**'dır:</p>
<ul>
    <li>İsveç'teki eşin (sponsorun) çiftin birlikte yaşayabileceği büyüklükte bir eve (kiralık veya mülk) sahip olması gerekir.</li>
    <li>İsveç'teki eşin, ortak yaşam masraflarını karşılayabilecek düzeyde düzenli ve yeterli bir gelire sahip olduğunu Skatteverket belgeleriyle kanıtlaması şarttır.</li>
</ul>

<h2>Eş Durumundan Hızlandırılmış İsveç Vatandaşlığı</h2>
<p>Normal şartlarda İsveç vatandaşlığı almak için kesintisiz olarak 5 yıl İsveç'te yaşamak (hemvisttid) gerekirken, bir İsveç vatandaşı ile evli veya sambo olan kişiler için bu süre **3 yıla düşmektedir**.</p>
<p>Bu hızlandırılmış haktan yararlanabilmek için aşağıdaki özel kurallar geçerlidir:</p>
<ul>
    <li>Son 2 yıldır eşinizle/partnerinizle aynı evde kesintisiz olarak yaşıyor olmanız (birlikte ikamet) gerekir.</li>
    <li>Eşinizin en az 2 yıldır resmi olarak İsveç vatandaşı olması şarttır.</li>
    <li>İsveç'teki yaşamınız boyunca dürüst ve temiz bir sicile sahip olmanız, borç kaydınızın bulunmaması gerekir.</li>
</ul>

<div class="elite-info-box" style="border-radius: 12px; margin: 30px 0;">
    <h3 style="margin-top: 0; color: #1e293b;">Evlilik Yoluyla Başvuruda Sınav Zorunluluğu</h3>
    <p>3 yıllık sürenin sonunda vatandaşlık başvurusu yaparken, standart başvuranlar gibi sizin de İsveç yasal sistemi, coğrafyası ve kültürü üzerine yapılan zorunlu vatandaşlık sınavını (Medborgarskapsprov) geçmeniz gerekmektedir.</p>
</div>

<p>İsveç vatandaşlığı alma sürecinizi kısaltan evlilik yolunda, sınav engelini kolayca aşabilmek ve eşinizle birlikte İsveççe terimleri pratik etmek için <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" style="color: #005bb5; font-weight: 600; text-decoration: underline;">sverigemedborgarskapsprov.com</a> sitesindeki soru ve konu özetlerini kullanabilirsiniz.</p>

<div style="text-align: center; margin: 30px 0;">
    <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" class="btn btn-primary" style="display: inline-block; padding: 14px 28px; font-size: 1.1rem; border-radius: 8px; text-decoration: none; font-weight: 700; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0, 91, 181, 0.2); background-color: #005bb5; color: white;">Eş Durumu Sınav Hazırlığına Git</a>
</div>
"""
    },
    {
        "slug": "isvec-vatandasi-turkiyede-kac-gun-kalabilir",
        "title": "İsveç Vatandaşları Türkiye'de Kaç Gün Kalabilir? Vize Kuralları",
        "breadcrumb_name": "İsveç Vatandaşlarının Türkiye'de Kalış Süresi",
        "category": "Göçmenlik & Hukuk",
        "meta_description": "İsveç pasaportu sahiplerinin Türkiye'de vizesiz kalma süreleri (90 gün kuralı), ikamet izni süreçleri ve çifte vatandaşlık avantajları.",
        "lead_paragraph": "İsveç vatandaşı (pasaportu) olan kişilerin Türkiye seyahatlerinde vizesiz kalabileceği süreler, ikamet izni (e-ikamet) şartları ve çifte vatandaşlık sahiplerinin Türkiye'deki hakları.",
        "cta_title": "Çifte Vatandaş Olup Türkiye Seyahatlerinde Sınırları Kaldırın",
        "cta_text": "İsveç vatandaşlığına geçerek hem İsveç hem de Türk pasaportunun gücünden yararlanın. İsveç vatandaşlığı sınavını geçmek için en iyi hazırlık portalına şimdiden üye olun.",
        "cta_button_text": "Vatandaşlık Sınavına Şimdiden Hazırlan",
        "body_content": """
<p>İsveç vatandaşlığı alan veya İsveç pasaportuna sahip olarak Türkiye'yi ziyaret etmek isteyen kişilerin uyması gereken yasal kurallar ve süre sınırları bulunmaktadır. Özellikle İsveç vatandaşlığına geçip Türk vatandaşlığından çıkan veya çifte vatandaşlığı bulunan kişiler için Türkiye'deki kalış süreleri merak edilmektedir. İşte 2026 güncel kuralları.</p>

<h2>Türkiye'de Vizesiz Kalma Süresi (90 Gün Kuralı)</h2>
<p>Türkiye Cumhuriyeti ile İsveç Krallığı arasındaki anlaşmalar gereği, İsveç pasaportuna sahip vatandaşlar Türkiye'ye yapacakları turistik seyahatlerde vizeden muaftır. Bu muafiyetin sınırları şu şekildedir:</p>
<ul>
    <li>İsveç vatandaşları, Türkiye'de **her 180 gün içinde en fazla 90 gün** vizesiz olarak kalabilirler.</li>
    <li>Bu süre tek seferde kullanılabileceği gibi, parça parça giriş-çıkış yapılarak da tamamlanabilir.</li>
    <li>90 günlük sürenin aşılması durumunda vize ihlali cezası uygulanır ve sınır dışı edilme riski ortaya çıkar.</li>
</ul>

<h2>90 Günden Fazla Kalmak İsteyenler Ne Yapmalı?</h2>
<p>Türkiye'de 90 günden daha uzun süre kalmayı planlayan İsveç vatandaşlarının, süreleri dolmadan önce İl Göç İdaresi Müdürlüğü'ne başvurarak **Kısa Dönem İkamet İzni (e-ikamet)** almaları gerekmektedir. Eğitim, iş veya evlilik gibi nedenlerle ikamet izni alınabilmektedir.</p>

<div class="elite-info-box" style="border-radius: 12px; margin: 30px 0;">
    <h3 style="margin-top: 0; color: #1e293b;">Çifte Vatandaşlar ve Mavi Kart Sahipleri</h3>
    <p>Hem Türk hem de İsveç vatandaşlığı bulunan çifte vatandaşlar, Türkiye'ye Türk kimlik kartı veya pasaportuyla giriş yaptıklarında herhangi bir süre sınırına tabi değillerdir. Türk vatandaşlığından izinle çıkan eski Türk vatandaşları ise 'Mavi Kart' (Blue Card) ibraz ederek Türkiye'de sınırsız kalma ve çalışma hakkına sahip olurlar.</p>
</div>

<h2>Çifte Vatandaşlık ve Seyahat Kolaylığı</h2>
<p>İsveç ve Türkiye, vatandaşlarının çifte vatandaş (Dubbelt medborgarskap) olmasına tam izin vermektedir. İsveç vatandaşlığını kazandığınızda Türk vatandaşlığınızı koruyabilir, böylece Türkiye seyahatlerinizde hiçbir vize veya gün sınırı olmadan memleketinizde kalabilirsiniz.</p>

<p>Bu büyük avantaja kavuşmak ve İsveç pasaportunu cebinize koymak için önünüzdeki en büyük yasal adım olan vatandaşlık entegrasyon sınavını başarıyla vermelisiniz. Sınava hazırlıkta lider platform olan <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" style="color: #005bb5; font-weight: 600; text-decoration: underline;">sverigemedborgarskapsprov.com</a>'u kullanarak hazırlıklarınızı hızlandırabilirsiniz.</p>

<div style="text-align: center; margin: 30px 0;">
    <a href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" class="btn btn-primary" style="display: inline-block; padding: 14px 28px; font-size: 1.1rem; border-radius: 8px; text-decoration: none; font-weight: 700; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0, 91, 181, 0.2); background-color: #005bb5; color: white;">İsveç Vatandaşlık Sınavına Çalışmaya Başla</a>
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

    iso_date = "2026-05-23"
    date_turkish = "23 Mayıs 2026"

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

    # Replace CTA link to target the external preparation site
    old_btn = 'href="../../iletisim/" class="btn btn-primary"'
    new_btn = 'href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" class="btn btn-primary"'
    html_output = html_output.replace(old_btn, new_btn)

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

    # Strip featured-post class and associated styles from existing featured posts
    content = re.sub(r'class="news-card featured-post"', 'class="news-card"', content)
    content = re.sub(r'style="height: 400px; object-fit: cover;"', '', content)

    # Build the new card
    img_path = f"../assets/images/{slug}.png" if is_blog_index else f"assets/images/{slug}.png"
    link_path = f"{slug}/" if is_blog_index else f"blog/{slug}/"
    contact_path = f"../iletisim/" if is_blog_index else f"iletisim/"
    
    category_btn_text = "Hukuki Danışmanlık"

    card_html = f"""                    <article class="news-card featured-post">
                        <div class="news-img-wrapper">
                            <img src="{img_path}" alt="{title}" class="news-img" style="height: 400px; object-fit: cover;">
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

    # Inject new card inside <div class="news-grid">
    content = re.sub(r'(<div class="news-grid">)', r'\1\n' + card_html, content, count=1)

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
    print("Generating 5 Phase 2 Swedish Citizenship blog posts...")
    
    # 1. Generate post index files
    for post in POSTS:
        generate_post(post)
        
    # 2. Prepend cards to home page index.html and blog index.html
    # We prepend them in reverse order (from 5 to 1) so that post 1 ends up on top!
    home_index = os.path.join(BASE_DIR, "index.html")
    blog_index = os.path.join(BASE_DIR, "blog/index.html")
    
    for post in reversed(POSTS):
        prepend_card(home_index, post["slug"], post["title"], post["lead_paragraph"], post["category"], "23 Mayıs 2026", is_blog_index=False)
        prepend_card(blog_index, post["slug"], post["title"], post["lead_paragraph"], post["category"], "23 Mayıs 2026", is_blog_index=True)
        update_seo_script(post["slug"], "2026-05-23")

    print("\n✅ Phase 2 Generation process completed!")

if __name__ == "__main__":
    main()
