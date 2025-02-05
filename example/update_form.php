<?php
echo session_id(); // Should display a session ID
print_r($_SESSION); // Should show the `logged_in` variable
session_start();

$_SESSION['logged_in'] = true;
?>

    <!DOCTYPE html>
    <html>
    <head>
        <title>Update Account</title>
    </head>
    <body>
        <h1>Update Account Information</h1>
        <form action="update_account.php" method="POST">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" value="user@example.com" required>
            <br><br>
            <button type="submit">Update</button>
        </form>
    </body>
    </html>
