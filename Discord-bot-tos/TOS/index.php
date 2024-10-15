<?php include('check_session.php'); ?>
<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Chillibott Discord Bot Terms of Service</title>
    <link
      href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300..700&display=swap"
      rel="stylesheet"
    />
    <style>
      /* Allgemeine Stile */
      body {
        font-family: "Comfortaa", sans-serif;
        background: linear-gradient(135deg, #3498db, #8e44ad);
        color: #fff;
        margin: 0;
        padding: 0;
        display: flex;
        flex-direction: column;
        min-height: 100vh;
      }

      header {
        background: #282c34;
        color: white;
        padding: 40px 20px;
        text-align: center;
        position: relative;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
      }

      header h1 {
        font-size: 3.5rem;
        margin: 0;
        letter-spacing: 2px;
      }

      header p {
        font-size: 1.2rem;
        margin: 10px 0 0;
        color: rgba(255, 255, 255, 0.7);
      }

      .header-decoration {
        position: absolute;
        bottom: -15px;
        left: 50%;
        transform: translateX(-50%);
        width: 150px;
        height: 10px;
        background: linear-gradient(90deg, #ff6b6b, #feca57, #ff9f43);
        border-radius: 5px;
      }

      main {
        padding: 30px 20px;
        max-width: 900px;
        margin: 20px auto;
        background: #f8f9fa;
        color: #333;
        border-radius: 8px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
      }

      section {
        padding: 20px;
        margin-bottom: 20px;
        background-color: #ffffff;
        border-left: 5px solid #007bff;
        border-radius: 5px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
      }

      section:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0, 123, 255, 0.3);
      }

      h2 {
        color: #007bff;
        font-size: 1.8rem;
        margin-bottom: 10px;
      }

      p {
        font-size: 1rem;
        line-height: 1.6;
        margin-bottom: 20px;
      }

      a {
        color: #007bff;
        text-decoration: none;
        transition: color 0.3s ease;
      }

      a:hover {
        text-decoration: underline;
        color: #0056b3;
      }

      /* Footer */
      footer {
        text-align: center;
        padding: 20px;
        background: #343a40;
        color: #ffffff;
        margin-top: auto;
        box-shadow: 0 -4px 10px rgba(0, 0, 0, 0.1);
      }

      footer p {
        font-size: 0.9rem;
        margin: 0;
      }

      footer a {
        color: #feca57;
        text-decoration: none;
      }

      footer a:hover {
        text-decoration: underline;
      }

      /* Mobile Anpassungen */
      @media (max-width: 768px) {
        header h1 {
          font-size: 2.5rem;
        }

        main {
          padding: 15px;
        }

        section {
          padding: 15px;
        }

        h2 {
          font-size: 1.5rem;
        }

        p {
          font-size: 0.9rem;
        }
      }
    </style>
  </head>
  <body>
    <header>
      <h1>Chillibott TOS</h1>
      <p>Terms of Service for Chillibott Discord Bot</p>
      <div class="header-decoration"></div>
    </header>

    <main>
      <section id="introduction">
        <h2>Einführung</h2>
        <p>
          Willkommen bei Chillibott, einem vielseitigen Discord-Bot, der
          umfangreiche Funktionen wie ein Ticket-System und Gaming-Features
          bietet. Diese Nutzungsbedingungen regeln Ihre Nutzung von Chillibott.
          Mit der Nutzung von Chillibott erklären Sie sich mit diesen
          Bedingungen einverstanden.
        </p>
      </section>

      <section id="user-agreement">
        <h2>Nutzungsvereinbarung</h2>
        <p>
          Mit der Nutzung von Chillibott stimmen Sie diesen Nutzungsbedingungen
          zu. Diese Vereinbarung unterliegt Änderungen. Es wird empfohlen,
          regelmäßig die aktuellen Nutzungsbedingungen zu prüfen, um über
          etwaige Änderungen informiert zu bleiben.
        </p>
      </section>

      <section id="use-of-chillibot">
        <h2>Nutzung von Chillibott</h2>
        <p>
          Funktionalität: Chillibott ist ein Discord-Bot, der für
          Unterhaltungs-, Management- und Dienstzwecke genutzt wird.
          Interaktionen erfolgen über Befehle, die in die Discord-Oberfläche
          integriert sind. Nutzer sind verantwortlich für die korrekte Anwendung
          dieser Befehle.
        </p>
      </section>

      <section id="data-protection">
        <h2>Datenschutz und -sicherheit</h2>
        <p>
          Chillibott befolgt die Datenschutz-Grundverordnung (DSGVO) und das
          Bundesdatenschutzgesetz (BDSG). Erhobene Daten, wie z. B.
          Benutzernamen und IDs, werden nur mit ausdrücklicher Zustimmung der
          Nutzer gesammelt und ausschließlich für betriebliche Zwecke verwendet.
        </p>
        <blockquote>
          "Die Erhebung und Verarbeitung personenbezogener Daten erfolgt auf
          Grundlage des Art. 6 Abs. 1 lit. a der DSGVO" -
          <i>Europäische Datenschutz-Grundverordnung</i>
        </blockquote>
        <p>
          Die Nutzer haben jederzeit das Recht, auf ihre Daten zuzugreifen, sie
          zu ändern oder deren Löschung zu beantragen.
        </p>
      </section>

      <section id="user-conduct">
        <h2>Nutzerverhalten</h2>
        <p>
          Nutzern ist es untersagt, Chillibott für illegale Aktivitäten zu
          verwenden. Dies schließt diffamierendes, betrügerisches oder
          schädliches Verhalten ein. Außerdem müssen sich Nutzer an die
          Discord-Nutzungsbedingungen halten.
        </p>
      </section>

      <section id="liability">
        <h2>Haftung und Haftungsausschlüsse</h2>
        <p>
          Chillibott wird im Rahmen der <strong>Beta-Version</strong> angeboten.
          Es wird keine Garantie für fehlerfreien Betrieb gegeben. Die Betreiber
          haften nicht für direkte oder indirekte Schäden, die aus der Nutzung
          des Bots entstehen.
        </p>
      </section>

      <section id="amendments">
        <h2>Änderungen der Nutzungsbedingungen</h2>
        <p>
          Diese Nutzungsbedingungen können jederzeit aktualisiert oder geändert
          werden. Verstöße gegen diese Bedingungen können zur Sperrung des
          Zugangs führen. Es gilt das deutsche Recht, und alle Streitigkeiten
          unterliegen der Rechtsprechung der deutschen Gerichte.
        </p>
      </section>

      <section id="contact">
        <h2>Kontakt und Anfragen</h2>
        <p>
          Bei Fragen oder Bedenken bezüglich Chillibott oder diesen
          Nutzungsbedingungen wenden Sie sich bitte an
          <strong>'zacklack'</strong> auf Discord (ID: 544536772063920148) oder
          schreiben Sie eine E-Mail an
          <a href="mailto:info@zacklack.de">info@zacklack.de</a>.
        </p>
      </section>
    </main>

    <footer>
      <p>&copy; 2024 Chillibott. Alle Rechte vorbehalten.</p>
    </footer>
  </body>
</html>
