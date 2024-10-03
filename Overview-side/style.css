/** @format */

body, html {
  margin: 0;
  padding: 0;
  font-family: "Comfortaa", sans-serif;
  background: url("background.jpg") no-repeat center center fixed;
  background-size: cover;
  overflow:auto ;
}

.header {
    text-align: center;
    position: relative;
}

.profilbild {
    width: 120px;
    height: auto;
    border-radius: 50%;
    transition: transform 0.3s ease, width 0.3s ease;
    cursor: pointer;
}

.profile-picture-container {
    position: relative;
    display: inline-block;
}

.profilbild:hover {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
}

.close-icon.show {
    display: block;
}

:root {
  --red: #e63946;
  --white: #ffffff34;
  --black: #1d1d1d;
  --overlay-color: rgba(255, 255, 255, 0.8);
  --blur-strength: 8px;
}

body::before {
  content: "";
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: var(--overlay-color);
  backdrop-filter: blur(var(--blur-strength));
  z-index: -1;
}

header {
  text-align: center;
  padding: 40px 20px;
  background: var(--white);
  margin: 30px auto;
  width: 90%;
  border-radius: 15px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.profilbild {
  width: 120px;
  height: auto;
  border-radius: 50%;
  border: 3px solid var(--red);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h1 {
  color: var(--black);
  font-size: 24px;
}

p {
  color: white;
  font-size: 18px;
  max-width: 600px;
  margin: auto;
}

.social-links {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 20px auto;
  width: 90%;
}

.social-item {
  display: flex;
  align-items: center;
  justify-content: start;
  width: 100%; /* Vollbreite innerhalb des Containers */
  margin: 10px 0;
}

.social-item a {
  display: flex;
  align-items: center;
  text-decoration: none; /* removes underline from links */
}

.social-item img {
  width: 40px;
  height: 40px;
  margin-right: 20px;
  transition: transform 0.3s ease;
}

.social-item a:hover img {
  transform: scale(1.9); /* Hover effect for images */
}

.username {
    display: inline-block;  /* Erlaubt die Transformation */
    transition: transform 0.3s ease, color 0.3s ease; /* Weiche Übergänge für Transform und Farbe */
    cursor: pointer;  /* Zeigt an, dass der Text interaktiv ist */
    margin: 5px 0;  /* Fügt vertikalen Abstand hinzu */
}

.username:hover {
    transform: translateY(-5px);  /* Bewegt den Text 5px nach oben */
    text-shadow:
    0 0 15px currentColor,  /* Erste Schicht des Glows */
    0 0 30px currentColor,  /* Zweite Schicht, breiterer Glow */
    0 0 45px currentColor;  /* Dritte Schicht, noch breiterer Glow */
}


.social-item a.username:hover {
  color: var(--red); /* Hover effect for text */
}

html, body {
  height: 100%; /* Setzt die Mindesthöhe auf 100% der Fensterhöhe */
  display: flex;
  flex-direction: column;
}

main {
  flex: 1; /* Erlaubt dem Hauptinhalt, den verfügbaren Raum einzunehmen */
}

footer {
    background-color: #2c2f3300; /* Dunkler Hintergrund für den Footer */
    color: #ffffff; /* Weiße Textfarbe */
    text-align: center; /* Zentriert den Text im Footer */
    padding: 20px 0; /* Fügt oben und unten Polsterung hinzu */
    width: 100%; /* Stellt sicher, dass der Footer die gesamte Breite einnimmt */
}

.image-overlay {
    display: flex; /* Ändert von 'none' zu 'flex', aber bleibt unsichtbar, bis aktiviert */
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.8);
    z-index: 10;
    justify-content: center;
    align-items: center;
    opacity: 0; /* Startet als unsichtbar */
    visibility: hidden; /* Nicht klickbar, bis aktiviert */
    transition: opacity 0.3s ease, visibility 0s linear 0.3s; /* Verzögert das Verschwinden der 'visibility' */
}

.overlay-profilbild {
    width: 120px; /* Startgröße gleich wie das ursprüngliche Bild */
    border-radius: 50%;
    transition: width 0.3s ease; /* Glättet die Vergrößerung */
}

.image-overlay.active {
    opacity: 1;
    visibility: visible; /* Macht das Overlay sichtbar und klickbar */
    transition: opacity 0.3s ease; /* Keine Verzögerung beim Erscheinen */
}

.close-icon {
    position: absolute;
    top: 20px;
    right: 20px;
    font-size: 24px;
    color: #fff;
    cursor: pointer;
}

.popup-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.6);
    display: none;
    align-items: center;
    justify-content: center;
    z-index: 1000;
}

.popup-content {
    background:lightcoral;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    width: 90%;
    max-width: 400px;
    transform: scale(0.9);
    transition: transform 0.3s ease-out;
}

.popup-overlay.active .popup-content {
    transform: scale(1);
}

.close-btn {
    float: right;
    font-size: 28px;
    cursor: pointer;
}

.glass-effect {
    background: rgba(255, 255, 255, 0.1);  /* Leicht transparenter weißer Hintergrund */
    border-radius: 15px;  /* Abgerundete Ecken */
    padding: 10px 20px;  /* Innenabstand */
    margin: 10px 0;  /* Außenabstand */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);  /* Subtiler Schatten für mehr Tiefe */
    backdrop-filter: blur(10px);  /* Unschärfe-Effekt für den Glas-Look */
    border: 1px solid rgba(255, 255, 255, 0.25); /* Leicht sichtbare Grenze */
}

.login-button-container {
  display: flex;
  justify-content: center;
  margin-top: 30px;
}

.login-button {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 15px;
  padding: 10px 20px;
  text-decoration: none;
  color: #fff;
  font-size: 18px;
  font-weight: 500;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.25);
  backdrop-filter: blur(10px);
  transition: background 0.3s ease, transform 0.3s ease;
}

.login-button:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: translateY(-5px);
  text-shadow: 0 0 10px var(--white);
}
