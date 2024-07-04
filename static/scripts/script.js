const panels = document.querySelectorAll(".panel");
let intervalId;

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
