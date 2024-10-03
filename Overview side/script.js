/** @format */

document.getElementById("profile-picture").onclick = function () {
  var overlay = document.getElementById("image-overlay");
  var overlayImg = overlay.querySelector(".overlay-profilbild");
  overlay.classList.add("active");
  overlayImg.style.width = "300px"; // Vergrößert das Bild auf 300px
};

function closeOverlay() {
  var overlay = document.getElementById("image-overlay");
  var overlayImg = overlay.querySelector(".overlay-profilbild");
  overlay.classList.remove("active");
  overlayImg.style.width = "120px"; // Setzt die Bildgröße auf die Anfangsgröße zurück
}


function openPopup() {
  document.getElementById("discordPopup").style.display = "flex";
  setTimeout(() => {
    document.getElementById("discordPopup").classList.add("active");
  }, 10); // Delay hinzufügen, damit die CSS-Animation wirken kann
}

function closePopup() {
  document.getElementById("discordPopup").classList.remove("active");
  setTimeout(() => {
    document.getElementById("discordPopup").style.display = "none";
  }, 300); // Warte bis die Animation beendet ist
}

function openEmailPopup() {
  document.getElementById("emailPopup").style.display = "flex";
  setTimeout(() => {
      document.getElementById("emailPopup").classList.add("active");
  }, 10); // Delay hinzufügen, damit die CSS-Animation wirken kann
}

function closeEmailPopup() {
  document.getElementById("emailPopup").classList.remove("active");
  setTimeout(() => {
      document.getElementById("emailPopup").style.display = "none";
  }, 300); // Warte bis die Animation beendet ist
}

document.getElementById("profile-picture").onclick = function () {
  var overlay = document.getElementById("image-overlay");
  var overlayImg = overlay.querySelector(".overlay-profilbild");
  overlay.classList.add("active");
  overlayImg.style.width = "300px"; // Vergrößert das Bild auf 300px
};

function closeOverlay() {
  var overlay = document.getElementById("image-overlay");
  var overlayImg = overlay.querySelector(".overlay-profilbild");
  overlay.classList.remove("active");
  overlayImg.style.width = "120px"; // Setzt die Bildgröße auf die Anfangsgröße zurück
}

function openPopup() {
  document.getElementById("discordPopup").style.display = "flex";
  setTimeout(() => {
      document.getElementById("discordPopup").classList.add("active");
  }, 10); // Delay hinzufügen, damit die CSS-Animation wirken kann
}

function closePopup() {
  document.getElementById("discordPopup").classList.remove("active");
  setTimeout(() => {
      document.getElementById("discordPopup").style.display = "none";
  }, 300); // Warte bis die Animation beendet ist
}

function openEmailPopup() {
  document.getElementById("emailPopup").style.display = "flex";
  setTimeout(() => {
      document.getElementById("emailPopup").classList.add("active");
  }, 10); // Delay hinzufügen, damit die CSS-Animation wirken kann
}

function closeEmailPopup() {
  document.getElementById("emailPopup").classList.remove("active");
  setTimeout(() => {
      document.getElementById("emailPopup").style.display = "none";
  }, 300); // Warte bis die Animation beendet ist
}
