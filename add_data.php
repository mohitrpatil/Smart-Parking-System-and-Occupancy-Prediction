<?php
    // Connect to MySQL
    

    // Prepare the SQL statement
    
    $occ= $_GET["occ"];
    $pid=$_GET["pid"];
    
    $connect = mysqli_connect("localhost","root","","be_project");
    if(!$connect){
      echo "Connection Failed";
    }

      
    $SQL="UPDATE parkinginfo SET occupied = $occ WHERE parkingid = $pid " ;

    /*$SQL = "INSERT INTO yourdatabasename.data (date,temperature,humidity,pressure) VALUES ('$dateS','".$_GET["temp"]."','".$_GET["hum"]."','".$_GET["pr"]."')";     */

    // Execute SQL statement
    //$connect->query($SQL);
    $row=mysqli_query($connect,$SQL);

    // Go to the review_data.php (optional)
    //header("Location: index.php");
?>