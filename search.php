<?php

$servername = "localhost";
$username = "root";
$password = "code4good";
$dbname = "team4";

$query = $_POST["query"];
$querytype = $_POST["querytype"];


$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
   die("Connection failed: " . $conn->connect_error);
}



$sql = "SELECT $querytype from locations where $querytype = $query";


$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "Name: " . $row["LOCATIONNAME"]. "<br>";
    }
} else {
    echo "0 results";
}
$conn->close();
?> 
