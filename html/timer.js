const displayTime = document.getElementById("displayTime")
const btnStart = document.getElementById("btnStart");
const btnReset = document.getElementById("btnReset");

const timerStart = Date.now();
let timerEnd;

btnStart.addEventListener("click", runTimer)

console.log(timerStart)


function runTimer() {
    console.log("Timer running!");
}