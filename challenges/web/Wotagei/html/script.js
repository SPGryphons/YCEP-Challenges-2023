var video = document.getElementById("myVideo");
var seekBar = document.getElementById("seekBar");
var playPauseButton = document.getElementById("playPauseButton");
var muteButton = document.getElementById("muteButton");

playPauseButton.addEventListener("click", function () {
    if (video.paused) {
        video.play();
        playPauseButton.innerHTML = '<i class="fas fa-pause" aria-hidden="true"></i>';
    } else {
        video.pause();
        playPauseButton.innerHTML = '<i class="fas fa-play" aria-hidden="true"></i>';
    }
});

muteButton.addEventListener("click", function () {
    if (video.muted) {
        video.muted = false;
        muteButton.innerHTML = '<i class="fas fa-volume-up" aria-hidden="true"></i>';
    } else {
        video.muted = true;
        muteButton.innerHTML = '<i class="fas fa-volume-off" aria-hidden="true"></i>';
    }
});

seekBar.addEventListener("input", function () {
    var seekTime = video.duration * (seekBar.value / 100);
    video.currentTime = seekTime;
});

video.addEventListener("timeupdate", function () {
    var seekValue = (100 / video.duration) * video.currentTime;
    seekBar.value = seekValue;
});

seekBar.addEventListener("mousedown", function () {
    video.pause();
});

seekBar.addEventListener("mouseup", function () {
    video.play();
});

var loginButton = document.getElementById("loginButton");

loginButton.addEventListener("click", function () {
    // Add login logic here
    alert("Login button clicked!");
});
