<?php
session_start();

if (isset($_SESSION['authenticated']) && $_SESSION['authenticated'] === true) {
    header('Location: privat1.php'); // Weiterleitung zu einer geschützten Seite
    exit;
}

$error = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $enteredCode = $_POST['access_code'];
    
    if ($enteredCode === '1234') {
        $_SESSION['authenticated'] = true;
        header('Location: privat1.php'); // Weiterleitung zu einer geschützten Seite
        exit;
    } else {
        $error = 'Falscher Zugangscode.';
    }
}
?>

<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Zacklack</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="login-container">
        <h1>Login</h1>
        <form method="post" action="login.php">
            <label for="access_code">Zugangscode:</label>
            <input type="password" id="access_code" name="access_code" required>
            <button type="submit">Login</button>
        </form>

        <?php if ($error): ?>
            <p style="color: red;"><?= $error ?></p>
        <?php endif; ?>
    </div>
</body>
</html>
