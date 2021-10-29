<?php

$host = "localhost";
$username = "root";
$password = "";
$dbname = "mydb";
$tbname = "enrollment";

$connect = new PDO("mysql:host=localhost;dbname=mydb","root", "");

$recieved_data = json_decode(file_get_contents("php://input"));

$data = array();

// Delete Data
if($recieved_data -> action == 'delete'){
    $query = "
        DELETE FROM enrollment WHERE `enrollment_id` = '".$recieved_data->id."'
    ";
    $statement = $connect->prepare($query);
    $statement->execute();

    $output = array(
        'message' => 'Data Deleted'
    );
    echo json_encode($output);
}

// Update Seats
if($recieved_data -> action == 'update_seat'){
    $query = "
        UPDATE course_class SET seats_available = seats_available - 1 WHERE course_class.course_class_id = '".$recieved_data->id."'
    ";
    $statement = $connect->prepare($query);
    $statement->execute();

    $output = array(
        'message' => 'Course Class seats Updated'
    );
    echo json_encode($output);
}


// Update Seats
if($recieved_data -> action == 'update_eng'){
    $query = "
        UPDATE engineers SET engineer_inprogress_courses = CONCAT(engineer_inprogress_courses, ', ','".$recieved_data->id."') WHERE engineer_id = '".$recieved_data->engineer_id."'
    ";
    $statement = $connect->prepare($query);
    $statement->execute();

    $output = array(
        'message' => 'Engineer In-Progress Course Updated'
    );
    echo json_encode($output);
}



?>