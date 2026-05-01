/**
 * isvecenasilgelinir
 * Ana JavaScript Dosyası
 */

document.addEventListener("DOMContentLoaded", () => {
    console.log("İsveç'e Nasıl Gelinir? sitesi başlatıldı.");

    // AJAX Form Submission for Formspree
    const contactForms = document.querySelectorAll('.home-contact-form');
    
    contactForms.forEach(form => {
        form.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalBtnText = submitBtn.textContent;
            submitBtn.textContent = "Gönderiliyor...";
            submitBtn.disabled = true;

            // Create or find message element
            let msgEl = form.querySelector('.form-status-msg');
            if (!msgEl) {
                msgEl = document.createElement('div');
                msgEl.className = 'form-status-msg';
                msgEl.style.marginTop = '15px';
                msgEl.style.padding = '10px';
                msgEl.style.borderRadius = '8px';
                msgEl.style.textAlign = 'center';
                msgEl.style.fontWeight = 'bold';
                msgEl.style.transition = 'opacity 0.3s';
                form.appendChild(msgEl);
            }
            
            msgEl.style.display = 'block';
            msgEl.style.opacity = '1';

            try {
                const response = await fetch(form.action, {
                    method: form.method,
                    body: new FormData(form),
                    headers: {
                        'Accept': 'application/json'
                    }
                });
                
                if (response.ok) {
                    msgEl.textContent = "Mesajınız başarıyla iletildi. Teşekkürler!";
                    msgEl.style.backgroundColor = "#e6f4ea";
                    msgEl.style.color = "#1e8e3e";
                    form.reset();
                } else {
                    msgEl.textContent = "Bir hata oluştu. Lütfen tekrar deneyin.";
                    msgEl.style.backgroundColor = "#fce8e6";
                    msgEl.style.color = "#d93025";
                }
            } catch (error) {
                msgEl.textContent = "Bağlantı hatası. Lütfen daha sonra tekrar deneyin.";
                msgEl.style.backgroundColor = "#fce8e6";
                msgEl.style.color = "#d93025";
            } finally {
                submitBtn.textContent = originalBtnText;
                submitBtn.disabled = false;
                
                // Hide message after 5 seconds
                setTimeout(() => {
                    msgEl.style.opacity = '0';
                    setTimeout(() => msgEl.style.display = 'none', 300);
                }, 5000);
            }
        });
    });

    // Mobile Menu Toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const mainNav = document.querySelector('.main-nav');
    
    if (menuToggle && mainNav) {
        menuToggle.addEventListener('click', () => {
            mainNav.classList.toggle('active');
            menuToggle.classList.toggle('active');
        });
    }


    // Slider Logic
    const slides = document.querySelectorAll('.slide');
    const dots = document.querySelectorAll('.dot');
    const nextBtn = document.querySelector('.slider-btn.next');
    const prevBtn = document.querySelector('.slider-btn.prev');
    let currentSlide = 0;
    let slideInterval;

    if (slides.length > 0) {
        const showSlide = (index) => {
            slides.forEach((slide, i) => {
                slide.classList.remove('active');
                dots[i].classList.remove('active');
            });
            slides[index].classList.add('active');
            dots[index].classList.add('active');
        };

        const nextSlide = () => {
            currentSlide = (currentSlide + 1) % slides.length;
            showSlide(currentSlide);
        };

        const prevSlide = () => {
            currentSlide = (currentSlide - 1 + slides.length) % slides.length;
            showSlide(currentSlide);
        };

        const startSlider = () => {
            slideInterval = setInterval(nextSlide, 5000);
        };

        const resetSlider = () => {
            clearInterval(slideInterval);
            startSlider();
        };

        nextBtn.addEventListener('click', () => {
            nextSlide();
            resetSlider();
        });

        prevBtn.addEventListener('click', () => {
            prevSlide();
            resetSlider();
        });

        dots.forEach((dot, index) => {
            dot.addEventListener('click', () => {
                currentSlide = index;
                showSlide(currentSlide);
                resetSlider();
            });
        });

        startSlider();
    }
});
