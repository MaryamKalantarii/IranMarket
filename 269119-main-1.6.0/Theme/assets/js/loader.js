// ----------------------loader
var loading = document.querySelector("#loader");
function fadeOut(el, timeFade) {
  var opacity = 1;
  var interval = setInterval(function () {
    if (opacity > 0) {
      opacity -= 0.01;
      el.style.opacity = opacity;
    } else {
      clearInterval(interval);
      el.style.display = "none";
    }
  }, timeFade);
}
fadeOut(loading, 18);
