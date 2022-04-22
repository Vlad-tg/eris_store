const button = document.getElementById('accordions');
button.addEventListener('click', function () {
    this.style.backgroundColor = this.style.backgroundColor === 'green' ? 'red' : 'green';
    if (button.innerText.toLowerCase() === 'off') {
        button.innerText = 'ON';
    } else {
        button.innerText = 'OFF';
    }

});
0