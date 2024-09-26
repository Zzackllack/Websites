<?php
session_start();

// Wenn der Benutzer bereits eingeloggt ist, weiterleiten
if (isset($_SESSION['authenticated']) && $_SESSION['authenticated'] === true) {
    header('Location: /protected/index.php');
    exit;
}

$error = '';

// Prüfen, ob das Formular abgeschickt wurde
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $enteredCode = $_POST['access_code'];
    
    // Beispiel
    if ($enteredCode === '1234') {
        // Session setzen und weiterleiten
        $_SESSION['authenticated'] = true;
        header('Location: /protected/index.php');
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
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300..700&display=swap" rel="stylesheet">
    <style>
        body, html {
            margin: 0;
            padding: 0;
            font-family: "Comfortaa", sans-serif;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(180deg, rgba(63, 94, 251, 1) 0%, rgba(252, 70, 107, 1) 100%);
            background-size: cover;
            overflow: hidden;
        }

        .login-container {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 30px 40px;
            max-width: 400px;
            width: 100%;
            text-align: center;
            color: #fff;
            position: relative;
            transition: transform 0.3s ease-out, opacity 0.3s ease-out;
        }

        .login-container h1 {
            margin-bottom: 20px;
            font-size: 28px;
            color: #fff;
        }

        .login-container label {
            font-size: 18px;
            display: block;
            margin: 15px 0 5px;
            color: #fff;
        }

        .login-container input[type="password"] {
            width: 100%;
            padding: 12px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 10px;
            margin-bottom: 20px;
            background: rgba(255, 255, 255, 0.1);
            color: #fff;
            font-size: 16px;
        }

        .login-container input[type="password"]::placeholder {
            color: #ccc;
        }

        .login-container button {
            padding: 12px 20px;
            border: none;
            border-radius: 10px;
            background-color: rgba(63, 94, 251, 0.8);
            color: #fff;
            font-size: 18px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .login-container button:hover {
            background-color: rgba(252, 70, 107, 0.8);
        }

        .error-message {
            color: white;
            font-size: 16px;
            font-weight: bold;
            margin-top: 10px;
            position: absolute;
            top: -50px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(255, 0, 0, 0.7);
            padding: 10px 20px;
            border-radius: 10px;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease-out;
        }

        .error-message.show {
            top: -30px;
            opacity: 1;
            visibility: visible;
        }

        .login-container p {
            color: #fff;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h1>Login</h1>
        <form method="post" action="login.php">
            <label for="access_code">Zugangscode:</label>
            <input type="password" id="access_code" name="access_code" placeholder="Zugangscode eingeben" required>
            <button type="submit">Login</button>
        </form>

        <!-- Fehlermeldung anzeigen, falls der Code falsch ist -->
        <?php if ($error): ?>
            <div class="error-message show" id="error-message"><?= $error ?></div>
        <?php endif; ?>
        
        <p>© Zacklack 2024 - Bitte Zugangscode eingeben, um fortzufahren</p>
    </div>
    <script>
        // Pop-Out-Animation für die Fehlermeldung
        document.addEventListener('DOMContentLoaded', function() {
            const errorMessage = document.getElementById('error-message');
            if (errorMessage) {
                errorMessage.classList.add('show');
                setTimeout(() => {
                    errorMessage.classList.remove('show');
                }, 3000); // Fehlermeldung nach 3 Sekunden ausblenden
            }
        });
    </script>
</body>
</html>
