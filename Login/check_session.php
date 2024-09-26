<?php
session_start();

// Überprüfung, ob der Benutzer eingeloggt ist
if (!isset($_SESSION['authenticated']) || $_SESSION['authenticated'] !== true) {
    header('Location: /login.php'); // Umleitung zur Login-Seite
    exit;
}
?>
