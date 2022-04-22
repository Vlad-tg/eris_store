const carouse_one = document.querySelector(".div-all-carousel-under-slider-one").children;
const prev_carousel_one = document.querySelector(".prev-carousel-under-slider-one");
const next_carousel_one = document.querySelector(".next-carousel-under-slider-one");
let slid_one = 0;


prev_carousel_one.addEventListener("click", function () {
    prevCarouselOne();

})

next_carousel_one.addEventListener("click", function () {
    nextCarouselOne();

})

function prevCarouselOne() {
    if (slid_one === 1) {
        slid_one = 0;
        next_carousel_one.style.display = 'block';
        prev_carousel_one.style.display = 'none';


    } else {
        slid_one--;
        next_carousel_one.style.display = 'block';
    }
    changeCarouselOneSlide();
}

function nextCarouselOne() {
    if (slid_one === 0) {
        slid_one = 1;
        next_carousel_one.style.display = 'none';
        prev_carousel_one.style.display = 'block';
    } else {
        slid_one++;
        next_carousel_one.style.display = 'block';
        prev_carousel_one.style.display = 'block';
    }
    changeCarouselOneSlide();
}

function changeCarouselOneSlide() {
    for (let i = 0; i < carouse_one.length; i++) {
        carouse_one[i].classList.remove("active");
    }

    carouse_one[slid_one].classList.add("active");
}