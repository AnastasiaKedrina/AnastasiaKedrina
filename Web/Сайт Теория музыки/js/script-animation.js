btn1=document.getElementById('button_1');
btn2=document.getElementById('button_2');

let hidden = document.getElementById('hidden');
btn1.onclick = function () {
    hidden.classList.toggle('fade');
}
btn2.onclick = function () {
    hidden.classList.toggle('fade');
}
window.onload = function () {
    hidden.classList.toggle('fade');
}

