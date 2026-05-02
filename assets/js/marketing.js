/**
 * Marketing Automation JS
 * Handles Assistant Widget, Quiz, and Lead Magnet Popups
 */

document.addEventListener('DOMContentLoaded', () => {
    initAssistant();
    initLeadPopup();
    if (document.querySelector('.quiz-container')) {
        initQuiz();
    }
});

// 1. Floating Assistant
function initAssistant() {
    const trigger = document.createElement('div');
    trigger.className = 'floating-assistant-trigger';
    trigger.innerHTML = `<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>`;
    
    const panel = document.createElement('div');
    panel.className = 'assistant-panel';
    panel.innerHTML = `
        <div class="assistant-header">
            <span>İsveç Rehber Asistanı</span>
            <button class="close-panel" style="background:none; border:none; color:white; cursor:pointer;">&times;</button>
        </div>
        <div class="assistant-body" id="assistant-content">
            <div class="assistant-msg">Merhaba! İsveç yolculuğunuzda size nasıl yardımcı olabilirim? Aşağıdaki seçeneklerden birini seçebilir veya bize doğrudan yazabilirsiniz.</div>
            <div class="assistant-options">
                <button class="option-btn" data-next="oturum">Oturum & Çalışma İzni</button>
                <button class="option-btn" data-next="hukuki">Hukuki Yardım & Avukat</button>
                <button class="option-btn" data-next="egitim">Eğitim & Üniversite</button>
                <button class="option-btn" data-next="diger">Diğer Konular</button>
            </div>
        </div>
    `;

    document.body.appendChild(trigger);
    document.body.appendChild(panel);

    trigger.onclick = () => panel.classList.toggle('active');
    panel.querySelector('.close-panel').onclick = () => panel.classList.remove('active');

    // Simple routing logic
    panel.addEventListener('click', (e) => {
        if (e.target.classList.contains('option-btn')) {
            const next = e.target.dataset.next;
            handleAssistantStep(next);
        }
    });
}

function handleAssistantStep(step) {
    const content = document.getElementById('assistant-content');
    let html = '';

    switch(step) {
        case 'oturum':
            html = `<div class="assistant-msg">İsveç'te oturum ve çalışma izni süreçleri 2026 itibariyle değişti. Size en uygun yolu bulmamız için iletişim bilgilerinizi bırakın, uzmanlarımız sizi arasın.</div>
                    <a href="/iletisim/" class="btn btn-primary btn-block">İletişime Geç</a>`;
            break;
        case 'hukuki':
            html = `<div class="assistant-msg">İsveç'te Türkçe konuşan uzman avukatlarımızla (aile, göçmenlik, iş hukuku) yanınızdayız. Ücretsiz ön görüşme için formumuzu doldurun.</div>
                    <a href="/hukuki-yardim/#yardim-al" class="btn btn-primary btn-block">Hukuki Yardım Formu</a>`;
            break;
        case 'egitim':
            html = `<div class="assistant-msg">Üniversite başvuruları ve SI bursları hakkında her şeyi içeren 2026 Eğitim Rehberimizi incelediniz mi?</div>
                    <a href="/blog/isvecte-universite-egitimi/" class="btn btn-primary btn-block">Rehberi Oku</a>`;
            break;
        default:
            html = `<div class="assistant-msg">Bize her türlü sorunuzu mesaj olarak iletebilirsiniz. En kısa sürede dönüş yapacağız.</div>
                    <a href="/iletisim/" class="btn btn-primary btn-block">Mesaj Gönder</a>`;
    }

    content.innerHTML = html;
}

// 2. Lead Magnet Popup
function initLeadPopup() {
    // Show after 20 seconds or on exit intent
    if (localStorage.getItem('popupShown')) return;

    const popup = document.createElement('div');
    popup.className = 'marketing-popup';
    popup.innerHTML = `
        <div class="popup-content">
            <div class="popup-image"></div>
            <button class="popup-close">&times;</button>
            <div class="popup-body">
                <h2>Ücretsiz İsveç Rehberini İndirin!</h2>
                <p>2026 İsveç Göçmenlik, Oturum ve Hukuk kurallarını içeren 40 sayfalık özel rehberimizi hemen e-postanıza gönderelim.</p>
                <form action="https://formspree.io/f/xvovbkgz" method="POST" style="margin-top:20px;">
                    <input type="email" name="email" class="form-control" placeholder="E-posta adresiniz" required style="margin-bottom:10px;">
                    <button type="submit" class="btn btn-primary btn-block">Rehberi Gönder</button>
                </form>
            </div>
        </div>
    `;

    document.body.appendChild(popup);

    const showPopup = () => {
        popup.classList.add('active');
        localStorage.setItem('popupShown', 'true');
    };

    // Trigger after 25s
    setTimeout(showPopup, 25000);

    // Trigger on mouse leave (exit intent)
    document.addEventListener('mouseleave', (e) => {
        if (e.clientY < 0) showPopup();
    });

    popup.querySelector('.popup-close').onclick = () => popup.classList.remove('active');
}

// 3. Quiz Logic
function initQuiz() {
    const steps = document.querySelectorAll('.quiz-step');
    const progressBar = document.querySelector('.quiz-progress-bar');
    let currentStep = 0;

    const updateQuiz = () => {
        steps.forEach((s, i) => s.classList.toggle('active', i === currentStep));
        progressBar.style.width = `${((currentStep + 1) / steps.length) * 100}%`;
    };

    document.querySelector('.quiz-container').onclick = (e) => {
        if (e.target.classList.contains('quiz-opt')) {
            if (currentStep < steps.length - 1) {
                currentStep++;
                updateQuiz();
            }
        }
    };
}
