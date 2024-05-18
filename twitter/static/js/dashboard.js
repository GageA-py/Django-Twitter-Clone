
const tweetBody = document.getElementById("tweet-body");

tweetBody.addEventListener('input', function() {
    const newHeight = tweetBody.scrollHeight + 'px';
    tweetBody.style.height = newHeight
});

