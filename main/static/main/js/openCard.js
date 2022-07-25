
var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var panel = this.previousElementSibling;
        if (panel.style.display === "block") {
            panel.style.display = "none";
            this.innerHTML = "Дополнительно";
        } else {
            panel.style.display = "block";
            this.innerHTML = "Свернуть";
        }
        event.stopPropagation();
    });
}