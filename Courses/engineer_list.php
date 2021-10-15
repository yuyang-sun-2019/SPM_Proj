<!doctype html>
<html lang="en">

<head>
    <title>Course List</title>

    <!-- Required meta tags -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=yes">

    <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  <link rel="stylesheet" href="style.css">
</head>
<body>

<!-- John Green leads to personal profile page -->

<nav class="navbar navbar-default">
    <div class="container-fluid">
      <div class="navbar-header">
        <a class="navbar-brand" href="Course_homepage.html">Course Homepage</a>
      </div>
      <ul class="nav navbar-nav">
        <li><a href="engineer_homepage.html">Home</a></li>
        <li><a href="engineer_past.html">Past Courses</a></li>
        <li><a href="engineer_current.html">Current Courses</a></li>
        <li class="active"><a href="engineer.list.php">Courses List</a></li>
        <li><a href="engineer_profile.html">Personal Profile</a></li>
      </ul>
      <form class="navbar-form navbar-left" action="/action_page.php">
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Search" name="search">
        </div>
        <button type="submit" class="btn btn-default">Submit</button>
      </form>
        <ul class="nav navbar-nav navbar-right">
            <li><a href="#"><span class="glyphicon glyphicon-bell"></span> Notification</a></li>
            <li><a href="#"><span class="glyphicon glyphicon-earphone"></span> Chat/Email</a></li>
            <li><a href="#"><span class="glyphicon glyphicon-log-out"></span> Logout</a></li>
    </div>
  </nav>

  <?php
  # == Part A (Display Stored Responses): ENTER CODE HERE == 
  require_once 'common.php';
  
  $dao = new CoursesDAO();
  $courses = $dao->getAllCourses();
  echo "<table border='1'>";
            echo "  <tr>
                        <th>CourseID</th>
                        <th>CourseName(in hours)</th>
                        <th>Course_brief</th>";
  foreach($courses as $course){
      echo "<tr>
              <td>{$course->getCourseID()}</td>
              <td>{$course->getCourseName()}</td>
              <td>{$course->getCourse_brief()}</td>
            </tr>";
  }
  echo "</table>";
  # ====
?>