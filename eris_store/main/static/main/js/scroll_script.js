window.onscroll = function () {
    scrollFunction()
};

function scrollFunction() {
    if (document.body.scrollTop > 30 || document.documentElement.scrollTop > 30) {
        document.getElementById("line-center-div-all-views-id-sticky").style.display = "block";
        document.getElementById("line-text-views-under-center-line-id-sticky").style.display = "block";
        document.getElementById("line-center-div-all-views-id").style.opacity = "0";
    } else {
        document.getElementById("line-center-div-all-views-id-sticky").style.display = "none";
        document.getElementById("line-text-views-under-center-line-id-sticky").style.display = "none";
        document.getElementById("line-center-div-all-views-id").style.opacity = "1";
    }
}