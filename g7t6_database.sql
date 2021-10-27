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
(366, 'Kevin', 'kevin@hr.com', 'hr766'),
(367, 'Leo', 'leo@hr.com' , 'hr767'),
(368, 'Matt', 'matt@hr.com', 'hr768'),
(369, 'Nat', 'nat@hr.com', 'hr769');



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
(001, 'C101-C1, C102-C2, C103-C2, C104-C4, C105-C3', 'C201-C2, C202-C1'),
(002, 'C101-C1, C102-C3, C103-C2, C105-C3', 'C201-C1, C204-C2'),
(003, 'C102-C1, C103-C2, C104-C4, C105-C3', 'C201-C1'),
(004, 'C103-C2, C104-C2, C105-C3', 'C205-C2'),
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
(366, 'C101, C102, C103, C104, C105'),
(367, 'C201, C202, C203, C204, C205'),
(368, 'C206, C207, C208, C209, C210'),
(369, 'C301, C302, C303, C304, C305');




-- --------------------------------------------------------
-- -----------------------------------------------------
-- Table `quiz`
-- -----------------------------------------------------
CREATE TABLE `quiz` (
  `quiz_id` varchar(75) NOT NULL ,
  `FK_trainer_id` INT NOT NULL UNIQUE,
  `quiz_title` VARCHAR(75) NOT NULL,
  `quiz_score` INT(6) NOT NULL DEFAULT 0, 
  `quiz_start_datetime` DATETIME NULL DEFAULT NULL,
  `quiz_end_datetime` DATETIME NULL DEFAULT NULL,
  `quiz_content` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`quiz_id`),
  CONSTRAINT `FK_trainer_id`
    FOREIGN KEY (`FK_trainer_id`)
    REFERENCES `trainers` (`trainer_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);



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
('C205', 'Consumer Psychology', 'Biddable', 'C105','This is a Year1 course which requires the completion of C105 Engineering Design and Solutions', 'C205-C1, C205-C2', 'C205-L1, C205-L2, C205-L3', '2021-10-25 09:00:00', `start_date` + INTERVAL 4 month),

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
('C302-C2', 'C302',70),
('C303-C3', 'C303',70),
('C304-C4', 'C304',70),
('C305-C5', 'C305',70);




-- --------------------------------------------------------
-- -----------------------------------------------------
-- Course's Lesson Table
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `course_lesson` (

  `course_lesson_id` varchar(20) NOT NULL UNIQUE,
  `course_id` varchar(20)  NOT NULL,
  `pdf_material` varchar(300)  NOT NULL,
  `ppt_material` varchar(300)  NOT NULL,
  `quiz_id` varchar(20)  DEFAULT NULL,
  PRIMARY KEY (`course_lesson_id`))

ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

INSERT INTO `course_lesson` (`course_lesson_id`,`course_id`, `pdf_material`,`ppt_material`) VALUES
('C101-L1', 'C101', 'pdf1.pdf, pdf2.pdf', 'ppt1.pptx, ppt2.pptx'),
('C101-L2', 'C101', 'pdf3.pdf, pdf4.pdf', 'ppt3.pptx, ppt4.pptx'),
('C101-L3', 'C101', 'pdf5.pdf', 'ppt2.pptx, ppt4.pptx'),
('C101-L4', 'C101', 'pdf5.pdf, pdf4.pdf', 'ppt3.pptx, ppt4.pptx'),
('C102-L1', 'C102', 'pdf3.pdf, pdf4.pdf', 'ppt1.pptx, ppt2.pptx'),
('C102-L2', 'C102', 'pdf1.pdf, pdf5.pdf', 'ppt2.pptx, ppt4.pptx'),
('C103-L1', 'C103', 'pdf6.pdf', 'ppt3.pptx, ppt4.pptx'),
('C103-L2', 'C103', 'pdf5.pdf, pdf2.pdf', 'ppt1.pptx, ppt2.pptx'),
('C103-L3', 'C103', 'pdf5.pdf', 'ppt2.pptx, ppt4.pptx'),
('C104-L1', 'C104', 'pdf3.pdf, pdf4.pdf', 'ppt2.pptx, ppt4.pptx'),
('C104-L2', 'C104', 'pdf1.pdf, pdf5.pdf', 'ppt1.pptx, ppt2.pptx'),
('C105-L1', 'C105', 'pdf5.pdf', 'ppt3.pptx, ppt4.pptx'),
('C105-L2', 'C105', 'pdf3.pdf, pdf6.pdf', 'ppt1.pptx, ppt2.pptx'),
('C105-L3', 'C105', 'pdf5.pdf', 'ppt2.pptx, ppt4.pptx'),

('C201-L1', 'C201', 'pdf1.pdf, pdf5.pdf', 'ppt2.pptx, ppt4.pptx'),
('C201-L2', 'C201', 'pdf6.pdf', 'ppt1.pptx, ppt2.pptx'),
('C201-L3', 'C201', 'pdf5.pdf', 'ppt3.pptx, ppt4.pptx'),
('C201-L4', 'C201', 'pdf3.pdf, pdf4.pdf', 'ppt2.pptx, ppt4.pptx'),
('C202-L1', 'C202', 'pdf5.pdf, pdf6.pdf', 'ppt1.pptx, ppt2.pptx'),
('C202-L2', 'C202', 'pdf5.pdf', 'ppt2.pptx, ppt4.pptx'),
('C203-L1', 'C203', 'pdf5.pdf', 'ppt3.pptx, ppt4.pptx'),
('C203-L3', 'C203', 'pdf5.pdf, pdf2.pdf', 'ppt1.pptx, ppt2.pptx'),
('C203-L2', 'C203', 'pdf5.pdf', 'ppt3.pptx, ppt4.pptx'),
('C204-L1', 'C204', 'pdf1.pdf, pdf5.pdf', 'ppt1.pptx, ppt2.pptx'),
('C204-L2', 'C204', 'pdf3.pdf, pdf4.pdf', 'ppt1.pptx, ppt3.pptx'),
('C205-L1', 'C205', 'pdf6.pdf', 'ppt2.pptx, ppt4.pptx'),
('C205-L2', 'C205', 'pdf5.pdf', 'ppt3.pptx, ppt4.pptx'),
('C205-L3', 'C205', 'pdf1.pdf, pdf5.pdf', 'ppt1.pptx, ppt2.pptx'),

('C301-L1', 'C301', 'pdf3.pdf, pdf6.pdf', 'ppt1.pptx, ppt2.pptx'),
('C301-L2', 'C301', 'pdf5.pdf, pdf2.pdf', 'ppt2.pptx, ppt4.pptx'),
('C301-L3', 'C301', 'pdf5.pdf', 'ppt1.pptx, ppt3.pptx'),
('C301-L4', 'C301', 'pdf6.pdf', 'ppt3.pptx, ppt4.pptx'),
('C302-L1', 'C302', 'pdf3.pdf, pdf4.pdf', 'ppt1.pptx, ppt2.pptx'),
('C302-L2', 'C302', 'pdf5.pdf', 'ppt2.pptx, ppt4.pptx'),
('C303-L1', 'C303', 'pdf5.pdf, pdf2.pdf', 'ppt1.pptx, ppt3.pptx'),
('C303-L2', 'C303', 'pdf5.pdf, pdf6.pdf', 'ppt1.pptx, ppt2.pptx'),
('C303-L3', 'C303', 'pdf5.pdf', 'ppt3.pptx, ppt4.pptx'),
('C304-L1', 'C304', 'pdf5.pdf', 'ppt2.pptx, ppt4.pptx'),
('C304-L2', 'C304', 'pdf3.pdf, pdf4.pdf', 'ppt1.pptx, ppt2.pptx'),
('C305-L1', 'C305', 'pdf5.pdf, pdf6.pdf', 'ppt2.pptx, ppt4.pptx'),
('C305-L2', 'C305', 'pdf5.pdf', 'ppt3.pptx, ppt4.pptx'),
('C305-L3', 'C305', 'pdf1.pdf, pdf5.pdf', 'ppt1.pptx, ppt2.pptx');





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
-- Table `quiz_qn`
-- -----------------------------------------------------
CREATE TABLE `quiz_qn` (
  `qn_id` BIGINT NOT NULL AUTO_INCREMENT,
  `quiz_id` varchar(75) NOT NULL,
  `qn_score` SMALLINT(6) NOT NULL DEFAULT 0,
  `qn_content` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`qn_id`),
  CONSTRAINT `fk_qn_quiz`
    FOREIGN KEY (`quiz_id`)
    REFERENCES `quiz` (`quiz_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;



-- --------------------------------------------------------
-- -----------------------------------------------------
-- Table `ans_key`
-- -----------------------------------------------------
CREATE TABLE `ans_key` (
  `ans_id` VARCHAR(75) NOT NULL,
  `quiz_id` VARCHAR(75) NOT NULL,
  `qn_id` VARCHAR(75) NOT NULL,
  `correct` TINYINT(1) NOT NULL DEFAULT 0,
  `ans_key` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`ans_id`),
  INDEX `idx_answer_quiz` (`quiz_id` ASC),
  CONSTRAINT `fk_answer_quiz`
    FOREIGN KEY (`quiz_id`)
    REFERENCES `quiz` (`quiz_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;



ALTER TABLE `ans_key` 
ADD INDEX `idx_ans_qn` (`qn_id` ASC);
ALTER TABLE `ans_key` 
ADD CONSTRAINT `fk_ans_qn`
  FOREIGN KEY (`qn_id`)
  REFERENCES `quiz_qn` (`quiz_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


-- --------------------------------------------------------
-- -----------------------------------------------------
-- Table `take_table`
-- -----------------------------------------------------
CREATE TABLE `take_table` (
  `take_id` VARCHAR(75) NOT NULL,
  `engineer_id` INT NOT NULL,
  `quiz_id` VARCHAR(75) NOT NULL,
  `engineer_score` SMALLINT(6) NOT NULL DEFAULT 0,
  `startedAt` DATETIME NULL DEFAULT NULL,
  `finishedAt` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`take_id`),
  INDEX `idx_take_engineer` (`engineer_id` ASC),
  CONSTRAINT `fk_take_engineer`
    FOREIGN KEY (`engineer_id`)
    REFERENCES `engineers` (`engineer_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

ALTER TABLE `take_table` 
ADD INDEX `idx_take_quiz` (`quiz_id` ASC);
ALTER TABLE `take_table` 
ADD CONSTRAINT `fk_take_quiz`
  FOREIGN KEY (`quiz_id`)
  REFERENCES `quiz` (`quiz_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


-- --------------------------------------------------------
-- -----------------------------------------------------
-- Table `take_ans`
-- -----------------------------------------------------
CREATE TABLE `take_ans` (
  `take_ans_id` BIGINT NOT NULL AUTO_INCREMENT,
  `take_id` VARCHAR(75) NOT NULL,
  `qn_id` BIGINT NOT NULL,
  `ans_id` BIGINT NOT NULL,
  PRIMARY KEY (`take_ans_id`),
  INDEX `idx_answer_take` (`take_id` ASC),
  CONSTRAINT `fk_answer_take`
    FOREIGN KEY (`take_id`)
    REFERENCES `take_table` (`take_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

ALTER TABLE `take_ans` 
ADD INDEX `idx_tanswer_qn` (`qn_id` ASC);
ALTER TABLE `take_ans` 
ADD CONSTRAINT `fk_tanswer_qn`
  FOREIGN KEY (`qn_id`)
  REFERENCES `quiz_qn` (`qn_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `take_ans` 
ADD INDEX `idx_tanswer_answer` (`ans_id` ASC);
ALTER TABLE `take_ans` 
ADD CONSTRAINT `fk_tanswer_answer`
  FOREIGN KEY (`ans_id`)
  REFERENCES `quiz_ans` (`ans_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;



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