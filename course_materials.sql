SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `course_materials`
--
CREATE DATABASE IF NOT EXISTS `course_materials` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `course_materials`;

--
-- Table structure for table `course_materials`
--

DROP TABLE IF EXISTS `course_materials`;
CREATE TABLE IF NOT EXISTS `course_materials` (
  `course_id` int(11) NOT NULL PRIMARY KEY,
  `course_name` varchar(64) NOT NULL,
  `section_id` int(11) NOT NULL
  `trainerID` int(11) NOT NULL,
  `trainerName` char(13) NOT NULL,

  PRIMARY KEY (`course_id`),
) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4
-- COLLATE = utf8mb4_0900_ai_ci;

--
-- Dumping data for table `course_materials`
--

INSERT INTO course_materials(`course_id`,`course_name`,`section_id`,`trainerID`, `trainerName`) VALUES 
( '101', 'Basics of engineering', 'G1', '123', 'John Green');
( '202', 'Advanced Mechanics', 'G2','124', 'John Blue');
( '103', 'Law of indices', 'G3','125', 'John Red');
( '101', 'Basics of engineering', 'G6','126', 'John Yellow');
( '101', 'Basics of engineering', 'G7','127', 'John Purple');


COMMIT;