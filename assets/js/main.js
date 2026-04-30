/**
 * isvecenasilgelinir
 * Ana JavaScript Dosyası
 */

document.addEventListener("DOMContentLoaded", () => {
    console.log("İsveç'e Nasıl Gelinir? sitesi başlatıldı.");

    // İletişim formu için basit submit yakalayıcı (şimdilik preventDefault yapıyor)
    const contactForms = document.querySelectorAll('.contact-form, .home-contact-form');
    contactForms.forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Mesajınız başarıyla alınmıştır. En kısa sürede size dönüş yapacağız!');
            form.reset();
        });
    });

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
