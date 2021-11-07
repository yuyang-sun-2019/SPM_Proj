<?php

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

// Update Progress
if($recieved_data -> action == 'update_progress'){
    $query ="
    INSERT INTO progress (progress_id, engineer_id, course_id, lesson, pdf_material, ppt_material, video_material, doc_material, quiz_id) VALUES ('".$recieved_data->id."', '".$recieved_data->engineer_id."', '".$recieved_data->course_id."', '".$recieved_data->course_lesson_id."', NULL, NULL, NULL, NULL, NULL);
    ";
    $statement = $connect->prepare($query);
    $statement->execute();

    $output = array(
        'message' => 'Engineer progress has been updated.'
    );
    echo json_encode($output);}


// Update Progress Course Materials
if($recieved_data -> action == 'update_progress_material'){
    $query ="
    UPDATE progress SET ".$recieved_data->course_material." = '".$recieved_data->id."' WHERE progress.progress_id = '".$recieved_data->progress_id."'
    ";
    $statement = $connect->prepare($query);
    $statement->execute();

    $output = array(
        'message' => 'Engineer progress materials has been updated.'
    );
    echo json_encode($output);}



// Update Progress Lesson
if($recieved_data -> action == 'update_progress_lesson'){
    $query ="
    UPDATE progress SET lesson = '".$recieved_data->id."' WHERE progress.progress_id = '".$recieved_data->progress_id."';
    UPDATE `progress` SET `pdf_material` = NULL, `ppt_material` = NULL, `video_material` = NULL, `doc_material` = NULL, `quiz_id` = NULL WHERE `progress`.`progress_id` = '".$recieved_data->progress_id."';
    ";
    $statement = $connect->prepare($query);
    $statement->execute();

    $output = array(
        'message' => 'Engineer progress lesson has been updated.'
    );
    echo json_encode($output);}

// Update Progress Lesson
if($recieved_data -> action == 'reassign_course'){
    $query ="
    UPDATE progress SET lesson = '".$recieved_data->course_lesson."', `pdf_material` = NULL, `ppt_material` = NULL, `video_material` = NULL, `doc_material` = NULL, `quiz_id` = NULL WHERE progress.progress_id = '".$recieved_data->id."'
    ";
    $statement = $connect->prepare($query);
    $statement->execute();

    $output = array(
        'message' => 'Engineer has been reassigned to the Course.'
    );
    echo json_encode($output);}


// Update Course Lesson Quiz
if($recieved_data -> action == 'lesson_quiz'){
    $query ="
    UPDATE `course_lesson` SET `quiz_id` = '".$recieved_data->id."' WHERE `course_lesson`.`course_lesson_id` = '".$recieved_data->course_lesson_id."';
    ";
    $statement = $connect->prepare($query);
    $statement->execute();

    $output = array(
        'message' => 'Quiz has been added to the Course Lesson.'
    );
    echo json_encode($output);}



?>