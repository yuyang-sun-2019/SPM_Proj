-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/

-- Host: 127.0.0.1:3306
-- Generation Time: Jan 14, 2019 at 06:42 AM
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `trainers`
--
CREATE DATABASE IF NOT EXISTS `trainers` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `trainers`;

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

-- B: Trainer Personal Details {TrainerID, TrainerName, CoursesTaught, TeleID, EmailID} 
DROP TABLE IF EXISTS `trainers`;
CREATE TABLE IF NOT EXISTS `trainers` (
  `trainerID` int(11) NOT NULL,
  `trainerName` char(13) NOT NULL,
  `trainer_teleID` varchar(64) NOT NULL,
  `trainer_emailID` varchar(64) NOT NULL,
  `trainer_courses` varchar(64) NOT NULL,
  PRIMARY KEY (`trainerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `trainers`
--

INSERT INTO `trainers` (`trainerID`, `trainerName`, `trainer_teleID`, `trainer_emailID`,`trainer_courses`) VALUES
('123', 'John Green', '@green','green@gmail.com','Basics of engineering'),
('124', 'John Blue', '@blue','blue@gmail.com','Basics of engineering,Advanced Mechanics'),
('125', 'John Red', '@red','red@gmail.com','Basics of engineering, Law of indices'),
('126', 'John Yellow', '@yellow','yellow@gmail.com','Basics of engineering'),
('127', 'John Purple', '@purple','purple@gmail.com','Basics of engineering');


COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
