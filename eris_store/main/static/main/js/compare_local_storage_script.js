window.onload = function () {
    if (localStorage.getItem('bgButton') !== null) {
        var color = localStorage.getItem('bgButton');
        document.getElementById('accordion').innerText = color;
    }
    const button = document.body.querySelector('');
    button.addEventListener('click', function () {
        if (button.innerText.toLowerCase() === 'off') {
            button.innerText = 'on';
            localStorage.setItem('bgButton', 'on');
        } else {
            button.innerText = 'off';
            localStorage.setItem('bgButton', 'off');
        }
    });
}

