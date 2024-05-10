document.addEventListener("DOMContentLoaded", function() {
    const logoutForm = document.getElementById("logout-form");
})


const tweetBody = document.getElementById("tweet-body");

tweetBody.addEventListener('input', function() {
    const newHeight = tweetBody.scrollHeight + 'px';
    tweetBody.style.height = newHeight
});

