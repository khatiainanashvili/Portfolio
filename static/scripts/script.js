const panels = document.querySelectorAll(".panel");
let intervalId;


document.addEventListener("DOMContentLoaded", function() {
    if (panels.length > 0) {
        panels[0].classList.add('active');
    }
});


panels.forEach(element => {
    element.addEventListener('click', () => {
        removeActiveClasses();
        element.classList.add("active");
    });
});


function removeActiveClasses() {
    panels.forEach(element => {
        element.classList.remove("active");
    });
}

const panel = document.querySelector(".active");

function startActivationLoop() {
    let currentIndex = 0;
    intervalId = setInterval(() => {
        removeActiveClasses();
        panels[currentIndex].classList.add("active");
        currentIndex = (currentIndex + 1) % panels.length; 
    }, 1000);
}

function stopActivationLoop() {
    clearInterval(intervalId);
}

const container = document.querySelector(".container"); 

container.addEventListener('mouseenter', startActivationLoop);
container.addEventListener('mouseleave', stopActivationLoop);



