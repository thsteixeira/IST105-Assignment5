<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $number = $_POST['number'];
    $text = $_POST['text'];

    // Prepare the command to execute the Python script with arguments
    $command = escapeshellcmd("python process.py " . escapeshellarg($number) . " " . escapeshellarg($text));
    
    // Execute the command and capture the output
    $output = shell_exec($command);
    
    // Display the output
    echo "<!DOCTYPE html>
          <html>
          <head>
              <title>Results</title>
          </head>
          <body>
              <h1>Results</h1>
              <p>Outcome of the number puzzle:</p>
              <p>$output</p>
          </body>
          </html>";
}
?>