export default class Timer {
    constructor(root) {
        root.innerHTML = Timer.getHTML();

        this.el = {
            timerButtons: root.querySelectorAll(".timer-btn-set"),
            mins: root.querySelector(".timer-part-mins"),
            secs: root.querySelector(".timer-part-secs"),
            control: root.querySelector(".timer-btn-control"),
            sound: root.querySelector("#sound-effect")
        };

        this.interval = null;

        this.remainingSeconds = 10;


        this.updateInterfaceControls();
        this.updateInterfaceTime();

        // Add event listener to buttons for setting timer
        this.el.timerButtons.forEach(item => {
            item.addEventListener("click", event => {
                this.stop();
                this.remainingSeconds = event.target.innerHTML * 60;
                this.updateInterfaceTime();
            })
        })

        // Event listener to start timer
        this.el.control.addEventListener("click", () => {

            // Asks the user for permission for notifications
            this.notificationPermission();

            if (this.interval === null) {
                this.start();
            } else {
                this.stop();
            }
        })

    }

    // Returns mins, secs as array
    getTimeAsString() {
        const minutes = Math.floor(this.remainingSeconds / 60);
        const seconds = this.remainingSeconds % 60;
        const padMins = minutes.toString().padStart(2, "0");
        const padSecs = seconds.toString().padStart(2, "0");
        return [padMins, padSecs];
    }

    // Updates the time display
    updateInterfaceTime() {
        const [mins, secs] = this.getTimeAsString();
        this.el.mins.textContent = mins;
        this.el.secs.textContent = secs;
        if (this.interval !== null) {
            this.updateDocumentTitle(mins, secs);
        }
    }

    // Updates the document title while the timer is running
    updateDocumentTitle(mins, secs) {
        if (this.remainingSeconds > 1) {
            document.title = `${mins}:${secs} — Calma`;
        } else {
            document.title = "Calma";
        }
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
                this.el.sound.play();
                this.notificationSend("Time to take a break!")
            }
        }, 1000);

        this.updateInterfaceControls();
    }

    stop() {
        clearInterval(this.interval);

        this.interval = null;

        this.updateInterfaceControls();
    }

    // Sends notifications to the user
    notificationSend(message) {
        // check whether permission has been granted
        if (Notification.permission === "granted") {
            // If yes, sent notification
            new Notification(message);
        }
    }

    // Ask user for notifcation permission
    notificationPermission() {
        if (Notification.permission !== 'denied' || Notification.permission === "default") {
            Notification.requestPermission(function (permission) {});
        }
    }

    // Return HTML
    static getHTML() {
        return `
        <button type="button" class="timer-btn-set">5</button>
        <button type="button" class="timer-btn-set">10</button>
        <button type="button" class="timer-btn-set">25</button>
        <br>
        <span class="timer-part timer-part-mins">00</span>
        <span class="timer-part">:</span>
        <span class="timer-part timer-part-secs">00</span>
        <br>
<br>
        <button type="button" class="timer-btn timer-btn-control timer-btn-start">
        <i class="bi bi-play-fill"></i>
        </button>
        <audio id="sound-effect">
        <source src="media/sound-effect.mp3">
        </audio>
        `;
    }
}