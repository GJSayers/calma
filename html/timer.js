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
        this.remainingSeconds = 90;


        this.updateInterfaceControls();

        this.el.control.addEventListener("click", () => {
            // When Control button is clickec
        })

        this.el.reset.addEventListener("click", () => {
            // When Reset button is clickec
        })
    }

    updateInterfaceTime() {
        const minutes = Math.floor(this.remainingSeconds / 60);
        const seconds = this.remainingSeconds % 60;

        this.el.mins.textContent = minutes.toString().padStart(2, "0");
        this.el.secs.textContent = seconds.toString().padStart(2, "0");
    }

    updateInterfaceControls() {
        if (this.interval === null) {
            this.el.control.innerHTML = `<i class="bi bi-play-fill"></i>`;
            this.el.control.classList.add("timer-btn-start");
            this.el.control.classList.remove("timer-btn-stop");
        } else {
            this.el.control.innerHTML = `<i class="bi bi-pause-fill"></i>`;
            this.el.control.classList.add("timer-btn-stop");
            this.el.control.classList.remove("timer-btn-start");
        }
    }

    start() {
        if (this.remainingSeconds === 0) return;

        this.interval = setInterval(() => {
            this.remainingSeconds--;
            this.updateInterfaceTime();

            if (this.remainingSeconds === 0) {
                this.stop();
            }
        }, 1000);

        this.updateInterfaceControls();
    }

    stop() {
        clearInterval(this.interval);

        this.interval = null;

        this.updateInterfaceControls();
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