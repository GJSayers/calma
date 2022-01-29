//Code modified from YouTube Tutorial by Dev Ed @ https://youtu.be/KjQ8uvAt9kQ

var timerModalBtn = document.querySelector("#timer-modal-btn");
var timerContainer = document.querySelector('.timer-container')
var breakModalBtn = document.querySelector("#break-modal-btn");
var breakContainer = document.querySelector('.break-container')
var checkInModalBtn = document.querySelector("#check-in-modal-btn");
var checkInContainer = document.querySelector('.check-in-container')
var noteModalBtn = document.querySelector("#note-modal-btn");
var noteContainer = document.querySelector('.note-container')
var modalBg = document.querySelector(".modal-bg");
var modalClose = document.querySelector(".modal-close");


//timer modal
timerModalBtn.addEventListener("click", function () {
  console.log('open')
  modalBg.classList.add("bg-active");
  timerContainer.classList.add("timer-container-active");
});
modalClose.addEventListener("click", function () {
  console.log('close')
  modalBg.classList.remove("bg-active");
  timerContainer.classList.remove("timer-container-active");
});

//break modal
breakModalBtn.addEventListener("click", function () {
  console.log('open')
  modalBg.classList.add("bg-active");
  breakContainer.classList.add("break-container-active");
});
modalClose.addEventListener("click", function () {
  console.log('close')
  modalBg.classList.remove("bg-active");
  breakContainer.classList.remove("break-container-active");
});

//note modal
noteModalBtn.addEventListener("click", function () {
  console.log('open')
  modalBg.classList.add("bg-active");
  noteContainer.classList.add("note-container-active");
});
modalClose.addEventListener("click", function () {
  console.log('close')
  modalBg.classList.remove("bg-active");
  noteContainer.classList.remove("note-container-active");
});

//check in modal
checkInModalBtn.addEventListener("click", function () {
  console.log('open')
  modalBg.classList.add("bg-active");
  checkInContainer.classList.add("check-in-container-active");
});
modalClose.addEventListener("click", function () {
  console.log('close')
  modalBg.classList.remove("bg-active");
  checkInContainer.classList.remove("check-in-container-active");
});