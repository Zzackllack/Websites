// Dark Mode Toggle
let isDarkMode = false;

function switchTheme() {
  isDarkMode = !isDarkMode;
  document.body.classList.toggle("dark-mode", isDarkMode);
  document.getElementById("theme-switcher").textContent = isDarkMode
    ? "☀️"
    : "🌗";
}

// Simulierte Ladebalken
window.onload = function () {
  document.getElementById("progress").style.width = "100%";
};
