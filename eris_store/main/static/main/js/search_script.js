const search_div = document.querySelector(".div-search-price-both-max-min");
const search_button = document.querySelector(".button-click-search-price");


search_button.addEventListener("click", function () {
    SearchClickScript();

})

function SearchClickScript() {
    search_div.style.display = search_div.style.display === 'block' ? 'none' : 'block';
}