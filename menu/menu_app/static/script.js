var toggler = document.getElementsByClassName("caret");
var i;

for (i = 0; i < toggler.length; i++) {
  toggler[i].addEventListener("click", function() {
    console.log()
    this.parentElement.classList.toggle("opened");
    this.classList.toggle("caret-down");
  });
}