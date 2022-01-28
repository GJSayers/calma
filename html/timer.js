export default class Timer {
    constructor(root) {
        root.innerHTML = Timer.getHTML();

        this.el = {
            mins: root.querySelector(".timer-part-mins"),
            secs: root.querySelector(".timer-part-secs"),
            control: root.querySelector(".timer-btn-control"),
            reset: root.querySelector(".timer-btn-reset")
        };

        this.interval = null;
        this.remainingSeconds = 0;

        this.el.control.addEventListener("click", () => {
            // When Control button is clickec
        })

        this.el.reset.addEventListener("click", () => {
            // When Reset button is clickec
        })

    }

    static getHTML() {
        return `
        <span class="timer-part timer-part-mins">00</span>
        <span class="timer-part">:</span>
        <span class="timer-part timer-part-secs">00</span>
        <br>
        <button type="button" class="timer-btn timer-btn-control timer-btn-start">
            <i class="bi bi-play-fill"></i>
        </button>
        <button type="button" class="timer-btn timer-btn-reset">
            <i class="bi bi-stopwatch"></i>
        </button> 
        `;
    }
}