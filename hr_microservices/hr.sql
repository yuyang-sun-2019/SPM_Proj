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
-- Database: `HRs`
--
CREATE DATABASE IF NOT EXISTS `HRs` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `HRs`;

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `HRs`;
CREATE TABLE IF NOT EXISTS `HRs` (
  `HR_ID` int(11) NOT NULL,
  `HR_Name` char(13) NOT NULL,
  `HR_password` varchar(64) NOT NULL,
  PRIMARY KEY (`HR_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `HRs`
--

INSERT INTO `HRs` (`HR_ID`, `HR_Name`, `HR_password`) VALUES
('461', 'Pink Sandy', 'pink461'),
('562', 'Conan Black', 'black562'),
('761', 'Sherry Navy', 'navy761'),
('829', 'Taylor Swift', 'swift829'),
('982', 'Bubble tea', 'tea982');


COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
