export default class Timer {
    constructor(root) {
        root.innerHTML = Timer.getHTML();

        this.el = {
            timerButtons: root.querySelectorAll(".timer-btn-set"),
            mins: root.querySelector(".timer-part-mins"),
            secs: root.querySelector(".timer-part-secs"),
            control: root.querySelector(".timer-btn-control"),
            reset: root.querySelector(".timer-btn-reset")
        };

        this.interval = null;
        this.remainingSeconds = 0;

        // Asks the user for permission for notifications
        // Move to when they set first timer?
        this.notificationPermission(); 


        this.updateInterfaceControls();

        // Add event listener to buttons for setting timer
        this.el.timerButtons.forEach( item => {
            item.addEventListener("click", event => {
                this.stop();
                this.remainingSeconds = event.target.innerHTML * 60;
                console.log(event.target.innerHTML);
                this.updateInterfaceTime();
            })
        })
        

        // Event listener to start timer
        this.el.control.addEventListener("click", () => {
            if (this.interval === null) {
                this.start();
            } else {
                this.stop();
            }
        })

        this.el.reset.addEventListener("click", () => {
            const inputMinutes = prompt("How many minutes? (Max 1 Hour)")
 
            if (inputMinutes < 61) {
                this.stop();
                this.remainingSeconds = inputMinutes * 60;
                this.updateInterfaceTime();
            }
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
            Notification.requestPermission(function (permission) {
                // If the user accepts, let's create a notification
                if (permission === "granted") {
                    var notification = new Notification("You'll receive timer notifications");
                }
            });
        }
    }

    // Return HTML
    static getHTML() {
        return `
        <button type="button" class="timer-btn-set" id="btn-10">10</button>
        <button type="button" class="timer-btn-set" id="btn-25">25</button>
        <button type="button" class="timer-btn-set" id="btn-35">35</button>
        <br>
        <span class="timer-part timer-part-mins">00</span>
        <span class="timer-part">:</span>
        <span class="timer-part timer-part-secs">00</span>
        <br>
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