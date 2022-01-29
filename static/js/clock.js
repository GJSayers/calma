export default class Clock {
    constructor(root) {

        setInterval(() => {
            const d = new Date;
            const time = d.toLocaleTimeString([], {
                hour: '2-digit',
                minute: '2-digit'
            });
            root.innerHTML = time;
        }, 1000);

    }
}