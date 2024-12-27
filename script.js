const bar = document.getElementById('bar');
const close = document.getElementById('close');
const nav = document.getElementById('account-list');
const circles = document.querySelectorAll('.circle');

if (bar){
    bar.addEventListener('click',() =>{
        nav.classList.add('active');
    })
}
if (close){
    close.addEventListener('click',() =>{
        nav.classList.remove('active');
    })
}

circles.forEach(circle => {
  const progress = circle.getAttribute('data-progress');
  circle.style.setProperty('--progress', progress);
});