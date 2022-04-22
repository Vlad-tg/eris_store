const slides_zero_one = document.querySelector(".all-sliders-in-carousel").children;
const prev_zero_one = document.querySelector(".prev-zero-one");
const next_zero_one = document.querySelector(".next-zero-one");
let zero_one = 0;


prev_zero_one.addEventListener("click", function () {
    prevZeroOneSlide();
    resetTimer();
})

next_zero_one.addEventListener("click", function () {
    nextZeroOneSlide();
    resetTimer();
})

function prevZeroOneSlide() {
    if (zero_one === 1) {
        zero_one = 0;
        next_zero_one.style.display = 'block';
        prev_zero_one.style.display = 'none';
        prev_zero_one.style.transition = 'all 200ms ease';

    } else {
        zero_one--;
        next_zero_one.style.display = 'block';
    }
    changeZeroOneSlide();
}

function nextZeroOneSlide() {
    if (zero_one === 1) {
        zero_one = 2;
        next_zero_one.style.display = 'none';
        prev_zero_one.style.display = 'block';
    } else {
        zero_one++;
        next_zero_one.style.display = 'block';
        prev_zero_one.style.display = 'block';
    }
    changeZeroOneSlide();
}

function changeZeroOneSlide() {
    for (let i = 0; i < slides_zero_one.length; i++) {
        slides_zero_one[i].classList.remove("active");
    }

    slides_zero_one[zero_one].classList.add("active");
}

