<?php
$connect = mysqli_connect("localhost","root","","be_project");
    if(!$connect){
      echo "Connection Failed";
    }

      $occ= $_GET["occ"];
    $SQL="$occ" ;

    /*$SQL = "INSERT INTO yourdatabasename.data (date,temperature,humidity,pressure) VALUES ('$dateS','".$_GET["temp"]."','".$_GET["hum"]."','".$_GET["pr"]."')";     */

    // Execute SQL statement
    //$connect->query($SQL);
    $row=mysqli_query($connect,$SQL);
    $row = mysqli_fetch_assoc($row); 

    //print_r($row)
    echo json_encode($row);
    //return $row;
?>