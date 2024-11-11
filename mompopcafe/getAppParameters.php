<?php
  // Get the application environment parameters from the Parameter Store.
  //include ('getAppParameters.php');
  $showServerInfo = "false";
  $timeZone = "America/New_York";
  $currency = "$";
  $db_url = "localhost";
  $db_name = "mom_pop_db";
  $db_user = "hitesh";
  $db_password = "Msois@123";

  $conn = new mysqli($db_url, $db_user, $db_password, $db_name);

// Check if the connection was successful
  if ($conn->connect_error) {
      die("Connection failed: " . $conn->connect_error);
  } else {
      echo "Successfully connected to the database.";
  }
  // Display the server metadata information if the showServerInfo parameter is true.
  //include('serverInfo.php');
?>
