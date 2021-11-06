-- phpMyAdmin SQL Dump
-- version 4.9.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Sep 27, 2021 at 08:33 AM
-- Server version: 5.7.26
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `mydb`
--
CREATE DATABASE IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `mydb`;

-- --------------------------------------------------------
-- -----------------------------------------------------
-- Table `person`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `person` (

  `id` INT NOT NULL UNIQUE,
  `name` varchar(64) NOT NULL,
  `email` varchar(64) NOT NULL,
  `pwd` varchar(64) NOT NULL,
  PRIMARY KEY (`id`))
  
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

INSERT INTO `person` (`id`, `name`, `email`, `pwd`) VALUES
(001, 'Ally', 'ally@engineer.com', 'engineer001'),
(002, 'Bob', 'bob@engineer.com', 'engineer002'),
(003, 'Colin', 'colin@engineer.com', 'engineer003'),
(004, 'Daniel', 'daniel@engineer.com', 'engineer004'),
(005, 'Emma', 'emma@engineer.com', 'engineer005'),
(761, 'Fred', 'fred@trainer.com', 'trainer761'),
(762, 'Grace', 'grace@trainer.com', 'trainer762'),
(763, 'Helen', 'helen@trainer.com', 'trainer763'),
(764, 'Isabel', 'isabel@trainer.com', 'trainer764'),
(765, 'John', 'john@trainer.com', 'trainer765'),
(366, 'Kevin', 'kevin@hr.com', 'hr366'),
(367, 'Leo', 'leo@hr.com' , 'hr367'),
(368, 'Matt', 'matt@hr.com', 'hr368'),
(369, 'Nat', 'nat@hr.com', 'hr369');



-- --------------------------------------------------------
-- -----------------------------------------------------
-- Table `engineers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `engineers` (

  `engineer_id` INT NOT NULL UNIQUE,
  `engineer_completed_courses` varchar(64), 
  `engineer_inprogress_courses` varchar(64), 
  PRIMARY KEY (`engineer_id`))
  
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

INSERT INTO `engineers` (`engineer_id`, `engineer_completed_courses`, `engineer_inprogress_courses`) VALUES
(001, 'C101-C1, C102-C2, C103-C2', 'C201-C2, C202-C1'),
(002, 'C101-C1, C104-C2', 'C201-C1, C204-C2'),
(003, 'C101-C1, C103-C2', 'C201-C1'),
(004, 'C101-C2, C102-C2, C103-C1, C105-C3', 'C205-C2'),
(005, 'C101-C3, C103-C2, C104-C1, C105-C2', 'C203-C2');



-- --------------------------------------------------------
-- -----------------------------------------------------
-- Table `trainers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `trainers` (
  `trainer_id` INT NOT NULL UNIQUE,
  `trainer_course_class_id` varchar(200) NOT NULL,

  PRIMARY KEY (`trainer_id`),
  UNIQUE INDEX `trainer_course_section_id_UNIQUE` (`trainer_course_class_id`))
  
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

INSERT INTO `trainers` (`trainer_id`, `trainer_course_class_id`) VALUES
(761, 'C101-C1, C101-C2, C101-C3, C102-C1, C102-C2, C102-C3, C201-C1, C201-C2, C202-C1, C202-C2, C301-C1, C301-C2, C301-C3, C302-C1, C302-C2, C302-C3'),
(762,'C103-C1, C103-C2, C103-C3, C203-C1, C203-C2, C303-C1, C303-C2, C303-C3, C304-C1, C304-C2, C304-C3'),
(763, 'C104-C1, C104-C2, C104-C3, C105-C1, C105-C2, C105-C3, C204-C1, C204-C2, C205-C1, C205-C2, C305-C1, C305-C2, C305-C3'),
(764, 'C206-C1, C206-C2, C206-C3, C207-C1, C207-C2, C207-C3, C208-C1, C208-C2, C208-C3'),
(765, 'C209-C1, C209-C2, C209-C3, C210-C1, C210-C2, C210-C3');



-- --------------------------------------------------------
-- -----------------------------------------------------
-- Table `hr`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hr` (
  `hr_id` INT NOT NULL UNIQUE,
  `courses_assigned` varchar(400) NOT NULL,

  PRIMARY KEY (`hr_id`))
  
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

INSERT INTO `hr` (`hr_id`,`courses_assigned`) VALUES
(366, 'C101, C102, C103, C104, C105, C305'),
(367, 'C201, C202, C203'),
(368, 'C204, C205'),
(369, 'C301, C302, C303, C304');




-- --------------------------------------------------------
-- -----------------------------------------------------
-- Table `quiz`
-- -----------------------------------------------------
CREATE TABLE `quiz` (
  `quiz_id` varchar(75) NOT NULL UNIQUE,
  `FK_trainer_id` INT NOT NULL,
  `quiz_title` VARCHAR(75) NOT NULL,
  `quiz_duration` VARCHAR(75) NOT NULL,
  PRIMARY KEY (`quiz_id`))

    ENGINE = InnoDB
    DEFAULT CHARACTER SET = utf8;


-- --------------------------------------------------------
-- -----------------------------------------------------
-- Table `quiz_qn_ans`
-- -----------------------------------------------------
CREATE TABLE `quiz_qn_ans` (
  `quiz_qn_id` varchar(75) NOT NULL UNIQUE,

  `MCQ_Qn1` varchar(75) NOT NULL,
  `MCQ_Qn1_A` VARCHAR(75) NOT NULL,
  `MCQ_Qn1_B` varchar(75) NOT NULL,
  `MCQ_Qn1_C` VARCHAR(75) NOT NULL,
  `MCQ_Qn1_D` VARCHAR(75) NOT NULL,
  `MCQ_Qn1_Ans` varchar(75) NOT NULL,
  `MCQ_Qn1_Score` INT NOT NULL,

  `MCQ_Qn2` varchar(75) NOT NULL,
  `MCQ_Qn2_A` VARCHAR(75) NOT NULL,
  `MCQ_Qn2_B` varchar(75) NOT NULL,
  `MCQ_Qn2_C` VARCHAR(75) NOT NULL,
  `MCQ_Qn2_D` VARCHAR(75) NOT NULL,
  `MCQ_Qn2_Ans` varchar(75) NOT NULL,
  `MCQ_Qn2_Score` INT NOT NULL,

  `TandF_Qn1` varchar(75) NOT NULL,
  `TandF_Qn1_Ans` VARCHAR(75) NOT NULL,
  `TandF_Qn1_Score` INT NOT NULL,

  `TandF_Qn2` varchar(75) NOT NULL,
  `TandF_Qn2_Ans` VARCHAR(75) NOT NULL,
  `TandF_Qn2_Score` INT NOT NULL,
  
  PRIMARY KEY (`quiz_qn_id`))

  ENGINE = InnoDB
  DEFAULT CHARACTER SET = utf8;



-- --------------------------------------------------------
-- -----------------------------------------------------
-- Table `course_details`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `course_details` (
    `course_id` varchar(64) NOT NULL UNIQUE,
    `course_name` varchar(100) NOT NULL,
    `course_type` varchar(30) NOT NULL,
    `course_prerequisite` varchar(64), 
    `course_brief` varchar(200) NOT NULL,
    `course_class` varchar(200) NOT NULL,
    `lessons` varchar(200) NOT NULL,
    `start_date` DATETIME NOT NULL, 
    `end_date` DATETIME NOT NULL, 
    PRIMARY KEY (`course_id`))

ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

INSERT INTO `course_details` (`course_id`,`course_name`,`course_type`, `course_prerequisite`,`course_brief`, `course_class`, `lessons`, `start_date`, `end_date`) VALUES
('C101', 'Basic Mathematics', 'Assigned', NULL , 'This is a Year1 course which would be required to be completed prior to C201 Intermediate Mathematics', 'C101-C1, C101-C2, C101-C3', 'C101-L1, C101-L2, C101-L3, C101-L4', '2021-10-25 09:00:00', `start_date` + INTERVAL 4 month),
('C102', 'Basic Engineering Mathematics', 'Assigned', NULL, 'This is a Year1 course which would be required to be completed prior to Intermediate Mathematics', 'C102-C1, C102-C2, C102-C3', 'C102-L1, C102-L2', '2021-10-25 09:00:00', `start_date` + INTERVAL 4 month ),
('C103', 'Introduction to Engineering', 'Biddable', NULL, 'This is a Year1 course which would be required to be completed prior to Engineering Project Management', 'C103-C1, C103-C2', 'C103-L1, C103-L2, C103-L3', '2021-10-25 09:00:00', `start_date` + INTERVAL 4 month),
('C104', 'Principles of Electrical Engineering', 'Assigned', NULL, 'This is a Year1 course which would be required to be completed prior to Applications of Electrical Engineering', 'C104-C1, C104-C2, C104-C3, C104-C4', 'C104-L1, C104-L2', '2021-10-25 09:00:00', `start_date` + INTERVAL 4 month),
('C105', 'Engineering Design and Solutions', 'Biddable', NULL, 'This is a Year1 course which would be required to be completed prior to Consumer Psychology', 'C105-C1, C105-C2, C105-C3', 'C105-L1, C105-L2, C105-L3', '2021-10-25 09:00:00', `start_date` + INTERVAL 4 month),

('C201', 'Intermediate Mathematics', 'Biddable', 'C101', 'This is a Year1 course which requires the completion of C101 Basic Mathematics', 'C201-C1, C201-C2', 'C201-L1, C201-L2, C201-L3, C201-L4', '2021-10-25 09:00:00', `start_date` + INTERVAL 4 month),
('C202', 'Intermediate Engineering Mathematics', 'Biddable', 'C102', 'This is a Year1 course which requires the completion of C102 Basic Engineering Mathematics','C202-C1, C202-C2', 'C202-L1, C202-L2', '2021-10-25 09:00:00', `start_date` + INTERVAL 4 month),
('C203', 'Engineering Project Management', 'Biddable', 'C103' , 'This is a Year1 course which requires the completion of C103 Introduction to Engineering','C203-C1, C203-C2', 'C203-L1, C203-L2, C203-L3', '2021-10-25 09:00:00', `start_date` + INTERVAL 4 month),
('C204', 'Applications of Electrical Engineering', 'Biddable', 'C104', 'This is a Year1 course which requires the completion of C104 Principles of Electrical Engineering', 'C204-C1, C204-C2', 'C204-L1, C204-L2', '2021-10-25 09:00:00', `start_date` + INTERVAL 4 month),
('C205', 'Consumer Psychology', 'Biddable', 'C102','This is a Year1 course which requires the completion of C105 Engineering Design and Solutions', 'C205-C1, C205-C2', 'C205-L1, C205-L2, C205-L3', '2021-10-25 09:00:00', `start_date` + INTERVAL 4 month),

('C301', 'Advanced Mathematics', 'Biddable', 'C101, C201', 'This is a biddable course, please refer to OASIS for more information', 'C301-C1, C301-C2, C301-C2', 'C301-L1, C301-L2, C301-L3, C301-L4', '2021-10-25 09:00:00', `start_date` + INTERVAL 4 month),
('C302', 'Advanced Engineering Mathematics', 'Biddable', 'C102, C202', 'This is a biddable course, please refer to OASIS for more information', 'C302-C1, C302-C2, C302-C3', 'C302-L1, C302-L2', '2021-10-25 09:00:00', `start_date` + INTERVAL 4 month),
('C303', 'Emerging Technologies', 'Biddable', 'C203', 'This is a biddable course, please refer to OASIS for more information', 'C303-C1, C303-C2, C303-C3', 'C303-L1, C303-L2, C303-L3', '2021-10-25 09:00:00', `start_date` + INTERVAL 4 month),
('C304', 'Financial Technology', 'Biddable', 'C203', 'This is a biddable course, please refer to OASIS for more information','C304-C1, C304-C2, C304-C3', 'C304-L1, C304-L2', '2021-11-25 09:00:00', `start_date` + INTERVAL 4 month),
('C305', 'Event Management & Operations', 'Biddable', NULL, 'This is a biddable course, please refer to OASIS for more information', 'C305-C1', 'C305-L1, C305-L2, C305-L3', '2021-10-25 09:00:00', `start_date` + INTERVAL 4 month);




-- --------------------------------------------------------
-- -----------------------------------------------------
-- Course's Class Table
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `course_class` (

  `course_class_id` varchar(20) NOT NULL UNIQUE,
  `course_id` varchar(20)  NOT NULL,
  `seats_available` INT  NOT NULL ,

  PRIMARY KEY (`course_class_id`))

ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

INSERT INTO `course_class` (`course_class_id`,`course_id`, `seats_available`) VALUES
('C101-C1', 'C101',20),
('C101-C2', 'C101',40),
('C101-C3', 'C101',40),
('C102-C1', 'C102',30),
('C102-C2', 'C102',30),
('C102-C3', 'C102',30),
('C103-C1', 'C103',50),
('C103-C2', 'C103',50),
('C104-C1', 'C104',50),
('C104-C2', 'C104',10),
('C104-C3', 'C104',15),
('C104-C4', 'C104',20),
('C105-C1', 'C105',30),
('C105-C2', 'C105',30),
('C105-C3', 'C105',20),
('C201-C1', 'C201',40),
('C201-C2', 'C201',40),
('C202-C1', 'C202',40),
('C202-C2', 'C202',40),
('C203-C1', 'C203',50),
('C203-C2', 'C203',50),
('C204-C1', 'C204',30),
('C204-C2', 'C204',25),
('C205-C1', 'C205',35),
('C205-C2', 'C205',35),
('C301-C1', 'C301',70),
('C301-C2', 'C303',30),
('C301-C3', 'C303',30),
('C302-C1', 'C302',0),
('C302-C2', 'C303',30),
('C302-C3', 'C303',30),
('C303-C1', 'C303',30),
('C303-C2', 'C303',0),
('C303-C3', 'C303',30),
('C304-C1', 'C304',70),
('C304-C2', 'C304',40),
('C304-C3', 'C304',0),
('C305-C1', 'C305',10);




-- --------------------------------------------------------
-- -----------------------------------------------------
-- Course's Lesson Table
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `course_lesson` (

  `course_lesson_id` varchar(20) NOT NULL UNIQUE,
  `course_id` varchar(20)  NOT NULL,
  `pdf_material` varchar(300)  NOT NULL,
  `ppt_material` varchar(300)  NOT NULL,
  `video_material` varchar(300)  NOT NULL,
  `doc_material` varchar(300)  NOT NULL,
  `quiz_id` varchar(20)  DEFAULT NULL,
  PRIMARY KEY (`course_lesson_id`))

ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

INSERT INTO `course_lesson` (`course_lesson_id`,`course_id`, `pdf_material`,`ppt_material`,`video_material`,`doc_material`) VALUES
('C101-L1', 'C101', 'pdf1.pdf, pdf2.pdf', 'ppt1.pptx, ppt2.pptx', 'vid1.mp4, vid2.mp4, vid3.mp4', 'doc1.docx, doc2.docx, doc3.docx'),
('C101-L2', 'C101', 'pdf3.pdf, pdf4.pdf', 'ppt3.pptx, ppt4.pptx', 'vid1.mp4, vid3.mp4', 'doc1.docx, doc2.docx'),
('C101-L3', 'C101', 'pdf5.pdf', 'ppt2.pptx, ppt4.pptx', 'vid1.mp4, vid2.mp4, vid3.mp4', 'doc1.docx, doc2.docx, doc3.docx'),
('C101-L4', 'C101', 'pdf5.pdf, pdf4.pdf', 'ppt3.pptx, ppt4.pptx', 'vid1.mp4, vid3.mp4', 'doc1.docx, doc2.docx'),
('C102-L1', 'C102', 'pdf3.pdf, pdf4.pdf', 'ppt1.pptx, ppt2.pptx', 'vid2.mp4', 'doc1.docx, doc2.docx, doc3.docx'),
('C102-L2', 'C102', 'pdf1.pdf, pdf5.pdf', 'ppt2.pptx, ppt4.pptx', 'vid1.mp4, vid3.mp4', 'doc1.docx, doc2.docx'),
('C103-L1', 'C103', 'pdf6.pdf', 'ppt3.pptx, ppt4.pptx', 'vid1.mp4, vid2.mp4, vid3.mp4', 'doc1.docx, doc2.docx, doc3.docx'),
('C103-L2', 'C103', 'pdf5.pdf, pdf2.pdf', 'ppt1.pptx, ppt2.pptx', 'vid2.mp4', 'doc1.docx, doc2.docx'),
('C103-L3', 'C103', 'pdf5.pdf', 'ppt2.pptx, ppt4.pptx', 'vid1.mp4, vid2.mp4, vid3.mp4', 'doc1.docx, doc2.docx, doc3.docx'),
('C104-L1', 'C104', 'pdf3.pdf, pdf4.pdf', 'ppt2.pptx, ppt4.pptx', 'vid1.mp4, vid2.mp4, vid3.mp4', 'doc1.docx, doc2.docx'),
('C104-L2', 'C104', 'pdf1.pdf, pdf5.pdf', 'ppt1.pptx, ppt2.pptx', 'vid2.mp4', 'doc1.docx, doc2.docx'),
('C105-L1', 'C105', 'pdf5.pdf', 'ppt3.pptx, ppt4.pptx', 'vid1.mp4, vid2.mp4, vid3.mp4', 'doc1.docx, doc2.docx, doc3.docx'),
('C105-L2', 'C105', 'pdf3.pdf, pdf6.pdf', 'ppt1.pptx, ppt2.pptx', 'vid2.mp4', 'doc1.docx, doc2.docx'),
('C105-L3', 'C105', 'pdf5.pdf', 'ppt2.pptx, ppt4.pptx', 'vid1.mp4, vid3.mp4', 'doc1.docx, doc2.docx, doc3.docx'),

('C201-L1', 'C201', 'pdf1.pdf, pdf5.pdf', 'ppt2.pptx, ppt4.pptx', 'vid1.mp4, vid2.mp4, vid3.mp4', 'doc1.docx, doc2.docx'),
('C201-L2', 'C201', 'pdf6.pdf', 'ppt1.pptx, ppt2.pptx', 'vid1.mp4, vid3.mp4', 'doc1.docx, doc2.docx, doc3.docx'),
('C201-L3', 'C201', 'pdf5.pdf', 'ppt3.pptx, ppt4.pptx', 'vid2.mp4', 'doc1.docx, doc2.docx'),
('C201-L4', 'C201', 'pdf3.pdf, pdf4.pdf', 'ppt2.pptx, ppt4.pptx', 'vid1.mp4, vid2.mp4, vid3.mp4', 'doc1.docx, doc2.docx'),
('C202-L1', 'C202', 'pdf5.pdf, pdf6.pdf', 'ppt1.pptx, ppt2.pptx', 'vid2.mp4', 'doc1.docx, doc2.docx, doc3.docx'),
('C202-L2', 'C202', 'pdf5.pdf', 'ppt2.pptx, ppt4.pptx', 'vid1.mp4, vid2.mp4, vid3.mp4', 'doc1.docx, doc2.docx'),
('C203-L1', 'C203', 'pdf5.pdf', 'ppt3.pptx, ppt4.pptx', 'vid1.mp4, vid3.mp4', 'doc1.docx, doc2.docx'),
('C203-L3', 'C203', 'pdf5.pdf, pdf2.pdf', 'ppt1.pptx, ppt2.pptx', 'vid2.mp4', 'doc1.docx, doc2.docx, doc3.docx'),
('C203-L2', 'C203', 'pdf5.pdf', 'ppt3.pptx, ppt4.pptx', 'vid2.mp4', 'doc1.docx, doc2.docx'),
('C204-L1', 'C204', 'pdf1.pdf, pdf5.pdf', 'ppt1.pptx, ppt2.pptx', 'vid1.mp4, vid2.mp4, vid3.mp4', 'doc1.docx, doc2.docx'),
('C204-L2', 'C204', 'pdf3.pdf, pdf4.pdf', 'ppt1.pptx, ppt3.pptx', 'vid2.mp4', 'doc1.docx, doc2.docx'),
('C205-L1', 'C205', 'pdf6.pdf', 'ppt2.pptx, ppt4.pptx', 'vid1.mp4, vid3.mp4', 'doc1.docx, doc2.docx, doc3.docx'),
('C205-L2', 'C205', 'pdf5.pdf', 'ppt3.pptx, ppt4.pptx', 'vid2.mp4', 'doc1.docx, doc2.docx'),
('C205-L3', 'C205', 'pdf1.pdf, pdf5.pdf', 'ppt1.pptx, ppt2.pptx', 'vid1.mp4, vid2.mp4, vid3.mp4', 'doc1.docx, doc2.docx, doc3.docx'),

('C301-L1', 'C301', 'pdf3.pdf, pdf6.pdf', 'ppt1.pptx, ppt2.pptx', 'vid1.mp4, vid2.mp4, vid3.mp4', 'doc1.docx, doc2.docx'),
('C301-L2', 'C301', 'pdf5.pdf, pdf2.pdf', 'ppt2.pptx, ppt4.pptx', 'vid2.mp4', 'doc1.docx, doc2.docx, doc3.docx'),
('C301-L3', 'C301', 'pdf5.pdf', 'ppt1.pptx, ppt3.pptx', 'vid1.mp4, vid2.mp4, vid3.mp4', 'doc1.docx, doc2.docx'),
('C301-L4', 'C301', 'pdf6.pdf', 'ppt3.pptx, ppt4.pptx', 'vid1.mp4, vid3.mp4', 'doc1.docx, doc2.docx, doc3.docx'),
('C302-L1', 'C302', 'pdf3.pdf, pdf4.pdf', 'ppt1.pptx, ppt2.pptx', 'vid1.mp4, vid2.mp4, vid3.mp4', 'doc1.docx, doc2.docx'),
('C302-L2', 'C302', 'pdf5.pdf', 'ppt2.pptx, ppt4.pptx', 'vid2.mp4', 'doc1.docx, doc2.docx, doc3.docx'),
('C303-L1', 'C303', 'pdf5.pdf, pdf2.pdf', 'ppt1.pptx, ppt3.pptx', 'vid1.mp4, vid2.mp4, vid3.mp4', 'doc1.docx, doc2.docx'),
('C303-L2', 'C303', 'pdf5.pdf, pdf6.pdf', 'ppt1.pptx, ppt2.pptx', 'vid2.mp4', 'doc1.docx, doc2.docx'),
('C303-L3', 'C303', 'pdf5.pdf', 'ppt3.pptx, ppt4.pptx', 'vid2.mp4', 'doc1.docx, doc2.docx, doc3.docx'),
('C304-L1', 'C304', 'pdf5.pdf', 'ppt2.pptx, ppt4.pptx', 'vid1.mp4, vid3.mp4', 'doc1.docx, doc2.docx'),
('C304-L2', 'C304', 'pdf3.pdf, pdf4.pdf', 'ppt1.pptx, ppt2.pptx', 'vid1.mp4, vid2.mp4, vid3.mp4', 'doc1.docx, doc2.docx, doc3.docx'),
('C305-L1', 'C305', 'pdf5.pdf, pdf6.pdf', 'ppt2.pptx, ppt4.pptx', 'vid2.mp4', 'doc1.docx, doc2.docx'),
('C305-L2', 'C305', 'pdf5.pdf', 'ppt3.pptx, ppt4.pptx', 'vid1.mp4, vid3.mp4', 'doc1.docx, doc2.docx'),
('C305-L3', 'C305', 'pdf1.pdf, pdf5.pdf', 'ppt1.pptx, ppt2.pptx', 'vid1.mp4, vid2.mp4, vid3.mp4', 'doc1.docx, doc2.docx, doc3.docx');






-- --------------------------------------------------------
-- -----------------------------------------------------
-- Table `progress`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `progress` (

  `progress_id` varchar(64) NOT NULL UNIQUE,
  `engineer_id` INT NOT NULL, 
  `course_id` varchar(64) NOT NULL, 
  `lesson` varchar(300) NOT NULL,
  `pdf_material` varchar(300) DEFAULT NULL,
  `ppt_material` varchar(300) DEFAULT NULL,
  `video_material` varchar(300) DEFAULT NULL,
  `doc_material` varchar(300) DEFAULT NULL,
  `quiz_id` varchar(20)  DEFAULT NULL,
  PRIMARY KEY (`progress_id`))
  
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

INSERT INTO `progress` (`progress_id`, `engineer_id`, `course_id`, `lesson`) VALUES
('1 C201-C2', 1, 'C201', 'C201-L1'),
('1 C204-C2', 1, 'C204', 'C204-L1'),
('2 C201-C1', 2, 'C201', 'C201-L1'),
('2 C204-C2', 2, 'C204', 'C204-L1'),
('3 C201-C1', 3, 'C201', 'C201-L1'),
('4 C205-C2', 4, 'C205', 'C205-L1'),
('5 C203-C2', 5, 'C203', 'C203-L1');




-- --------------------------------------------------------
-- -----------------------------------------------------
-- Enrollment's Table
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `enrollment` (

  `enrollment_id` INT(20) NOT NULL UNIQUE AUTO_INCREMENT,
  `engineer_id` INT(20) DEFAULT NULL,
  `course_id` VARCHAR(20) DEFAULT NULL ,
  `course_class_id` VARCHAR(30) DEFAULT NULL ,

  PRIMARY KEY (`enrollment_id`))

ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- --------------------------------------------------------
-- -----------------------------------------------------
-- Alter Personell's Table
-- -----------------------------------------------------
ALTER TABLE `engineers`
  ADD CONSTRAINT `engineer_ibfk_1` FOREIGN KEY (`engineer_id`) REFERENCES `person` (`id`);

ALTER TABLE `trainers`
  ADD CONSTRAINT `trainer_ibfk_1` FOREIGN KEY (`trainer_id`) REFERENCES `person` (`id`);

ALTER TABLE `hr`
  ADD CONSTRAINT `hr_ibfk_1` FOREIGN KEY (`hr_id`) REFERENCES `person` (`id`);