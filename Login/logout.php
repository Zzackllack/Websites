<?php
session_start();
session_destroy(); // Beendet alle Sessions
header('Location: login.php'); // Weiterleitung zur Login-Seite
exit;
?>
