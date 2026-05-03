let bottom = document.querySelector(".bottom");
let header = document.querySelector("h1");
let hero = document.querySelector(".hero");

bottom.addEventListener("click", function() {
    alert("Hai cliccato il pulsante!");
    header.textContent = "Sistema Attivato!";
    hero.classList.toggle("attivo");
});
