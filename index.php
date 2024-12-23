<?php include('check_session.php'); ?>
<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="UTF-8" />
    <script defer src="https://cloud.umami.is/script.js" data-website-id="6ac3974f-c908-4f8c-a726-ef8845e80677"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Übersichtsseite</title>
    <link
      href="https://fonts.googleapis.com/css?family=Comfortaa"
      rel="stylesheet"
    />
    <style>
      /* Allgemeine Stile */
      body {
        font-family: "Comfortaa", sans-serif;
        margin: 0;
        padding: 0;
        background: linear-gradient(135deg, #3498db, #8e44ad);
        color: #fff;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        text-align: center;
      }

      h1 {
        font-size: 3em;
        margin-bottom: 20px;
        letter-spacing: 1px;
      }

      /* Styling für die Links */
      .link-container {
        display: flex;
        flex-direction: column;
        gap: 20px;
        align-items: center;
        margin-bottom: 40px;
        padding: 0 20px; /* Padding an den Seiten für Mobilgeräte */
        width: 100%;
        box-sizing: border-box;
      }

      a {
        padding: 15px 30px;
        background: #fff;
        color: #3498db;
        text-decoration: none;
        border-radius: 30px;
        font-size: 1.2em;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
        max-width: 400px;
        width: 100%; /* Links füllen den verfügbaren Platz */
        box-sizing: border-box;
      }

      a:hover {
        background-color: #3498db;
        color: #fff;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
        transform: translateY(-5px);
      }

      /* Loader und Progress-Bar */
      #progress {
        position: fixed;
        top: 0;
        left: 0;
        height: 5px;
        background: #fff;
        width: 0;
        transition: width 2s ease-out;
      }

      /* Footer */
      footer {
        margin-top: 20px;
        color: rgba(255, 255, 255, 0.8);
        font-size: 0.9em;
      }

      footer a {
        color: #3498db;
        text-decoration: underline;
        font-style: italic;
      }

      footer a:hover {
        color: #fff;
      }

      /* Mobile Optimierungen */
      @media (max-width: 768px) {
        h1 {
          font-size: 2.2em; /* Kleinere Schriftgröße für mobile Geräte */
        }

        a {
          font-size: 1em; /* Kleinere Schriftgröße für Links */
        }

        .link-container {
          padding: 0 10px; /* Weniger Padding an den Seiten für schmalere Bildschirme */
        }
      }
    </style>
  </head>
  <body>
    <!-- Fortschrittsanzeige -->
    <div id="progress"></div>

    <!-- Begrüßungstext -->
    <h1>Willkommen auf meiner Webseite!</h1>

    <!-- Links zu den verschiedenen Projekten -->
    <div class="link-container">
      <a href="quiz.php">Englisch Quiz</a>
      <a href="Nikolas/html/index.php">Informatik Projekt Cédric und Nikolas</a>
      <a href="IFrame.php">Iframe Experimente</a>
      <a href="/Offizieller-Chillicord/index.php"
        >Offizieller Chillicord Minecraft Server</a
      >
      <a href="/Ethik-Projekt/index.php"
        >Ethik Projekt (Lale Sokolov und Stefan Baretzki)</a
      >
      <a href="/discord-bot-tos/index.php">Discord Bot TOS</a>
    </div>

    <!-- Footer -->
    <footer>
      <p>Kontakt: <a href="mailto:info@zacklack.de">info@zacklack.de</a></p>
    </footer>

    <script>
      // Fortschrittsbalken beim Laden der Seite animieren
      window.onload = function () {
        document.getElementById("progress").style.width = "100%";
      };
    </script>
  </body>
</html>
