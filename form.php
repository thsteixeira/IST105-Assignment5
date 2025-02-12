<!DOCTYPE html>
<html>
<head>
    <title>PHP Form</title>
</head>
<body>
    <form action="process.php" method="POST">
        <label for="year">Birth Year:</label>
        <input type="number" id="year" name="year" required><br><br>
        
        <label for="message">Name or Secret Word:</label>
        <input type="text" id="message" name="message" required><br><br>
        
        <input type="submit" value="Solve the Puzzle">
    </form>
</body>
</html>