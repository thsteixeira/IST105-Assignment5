<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user_number = $_POST["user_number"];
    $user_text = $_POST["user_text"];

    $command = escapeshellcmd("python process.py $user_number $user_text");
    $output = shell_exec($command);

    echo "<h2>Results:</h2>";
    echo "<pre>$output</pre>";
}
?>