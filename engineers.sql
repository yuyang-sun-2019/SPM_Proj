SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `Engineers`
--
CREATE DATABASE IF NOT EXISTS `engineers` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `engineers`;

-- --------------------------------------------------------

--
-- Table structure for table `engineers`
--

DROP TABLE IF EXISTS `engineers`;
CREATE TABLE IF NOT EXISTS `engineers` (
  `engineer_id` int NOT NULL,
  `engineer_pwd` varchar(64) NOT NULL,
  `engineer_name` varchar(64) NOT NULL,
  `engineer_teleid` varchar(20) NOT NULL,
  `engineer_email` varchar(20) NOT NULL,
  `engineer_completedCourses` int(11),
  `engineer_enrolledCourses` int(11),
  `engineer_assignedCourses` int(11),
  `engineer_signedupCourses` int(11),

  PRIMARY KEY (`engineer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `engineers`
--

INSERT INTO `engineers` (`engineer_id`, `engineer_pwd`, `engineer_name`, `engineer_teleid`, `engineer_email`, `engineer_completedCourses`, `engineer_enrolledCourses`, `engineer_assignedCourses`, `engineer_signedupCourses`) VALUES
(1, 'password100', 'John Doe', '@abcd', 'johndoe@gmail.com', '1,2,3', '4,5', '6,7,8', '9'),
(2, 'password101', 'Mary Doe', '@efgh', 'marydoe@gmail.com', '1,2,3', '4,5', '6,7,8,9', '10,11'),
(3, 'password102', 'Jason Doe', '@ijkl', 'jasondoe@gmail.com', '1,2,3', '4,5', '6,7,8', '9'),
(4, 'password103', 'Selena Doe', '@mnop', 'selenadoe@gmail.com', '1,2,3', '4,5', '6,7,8,9', '10,11'),
(5, 'password104', 'May Smith', '@may123', 'maysmith@gmail.com', '1,2,3', '4,5', '6,7,8', '9'),
(6, 'password105', 'Jack Smith', '@jack456', 'jacksmith@gmail.com', '1,2,3', '4,5', '6,7,8,9', '10,11');
COMMIT;
