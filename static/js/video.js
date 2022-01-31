export default class Video {
    constructor(root) {

        root.innerHTML = Video.getHTML();

        this.el = {
            activityLinks: root.querySelectorAll(".activity-link"),
            activityVideo: root.querySelector(".activity-video"),
        };

        this.el.activityLinks.forEach(item => {
            item.addEventListener("mouseover", event => {})
        })

    }

    static getHTML() {
        return `
        <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/FjHGZj2IjBk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        `;
    }
}