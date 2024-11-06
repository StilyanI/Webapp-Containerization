const b1 = document.getElementById('sp1');
const b2 = document.getElementById('sp2');
const b3 = document.getElementById('sp3');

b1.addEventListener('click',() =>{
    b1.classList.add('active');
    b2.classList.remove('active');
    b3.classList.remove('active');
});

b2.addEventListener('click',() =>{
    b1.classList.remove('active');
    b2.classList.add('active');
    b3.classList.remove('active');
});

b3.addEventListener('click',() =>{
    b1.classList.remove('active');
    b2.classList.remove('active');
    b3.classList.add('active');
});