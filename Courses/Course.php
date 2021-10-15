<?php


class Course{

private $course_id;
    private $course_name;
    private $course_brief;
    
    public function __construct($course_id, $course_name, $course_brief){
        $this->course_id = $course_id;
        $this->course_name = $course_name;
        $this->course_brief= $course_brief;
    }

    public function getCourseID(){
        return $this->course_id;
    }

    public function getCourseName(){
        return $this->course_name;
    }

    public function getCourse_brief(){
        return $this->course_brief;
    }




}
?>
    