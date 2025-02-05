<?php
session_start();

if (!isset($_SESSION['logged_in'])) {
    echo "You must be logged in to perform this action.";
    exit;
}

// Simulating an update to the user's account
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = htmlspecialchars($_POST['email']);
    // Normally, you'd update this in a database. Here we simulate success.
    echo "Email successfully updated to: " . $email;
}
?>
