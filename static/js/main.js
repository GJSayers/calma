import Clock from "./clock.js";
import Timer from "./timer.js";

new Clock(
    document.querySelector("#clock"));

new Timer(
    document.querySelector(".timer"));

const videoLinks = document.querySelectorAll(".activity-link");

videoLinks.forEach(link => {
            console.log(link)
            let youtubeID = link.href.split("=")[1];
  
            link.addEventListener("click", (event) => {
                event.preventDefault();
                updateIframe(youtubeID)
            });
        })
        
            function updateIframe(youtubeID) {
                console.log(youtubeID);
                document.getElementById("videoPlayer").setAttribute("src", `https://www.youtube.com/embed/${youtubeID}`)
            }