-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';



-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `mydb` ;

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8mb4 ;
-- -----------------------------------------------------
-- Schema order
-- -----------------------------------------------------
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`engineers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`engineers` (

  `engineer_id` INT NOT NULL UNIQUE,
  `engineer_name` varchar(64) NOT NULL,
  `engineer_email` varchar(64) NOT NULL,
  `engineer_pwd` varchar(64) NOT NULL,
  `engineer_teleid` varchar(20) NOT NULL,
  `engineer_completed_coursesid` varchar(64), 
  `engineer_inprogress_coursesid` varchar(64), 
  `engineer_preassigned_coursesid` varchar(64), 
  `engineer_biddable_coursesid` varchar(64),  
  PRIMARY KEY (`engineer_id`))
  
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

INSERT INTO `engineers` (`engineer_id`, `engineer_name`, `engineer_email`, `engineer_pwd`, `engineer_teleid`, `engineer_completed_coursesid`, `engineer_inprogress_coursesid`, `engineer_preassigned_coursesid`, `engineer_biddable_coursesid`) VALUES
(001, 'Ally', 'ally@engineer.com', 'engineer001', 'ally001', 'E101, E102, E103, E104, E105', 'E201, E202, E203, E204', 'E206, E207, E208', 'E301, E302, E303') ;
INSERT INTO `engineers` (`engineer_id`, `engineer_name`, `engineer_email`, `engineer_pwd`, `engineer_teleid`, `engineer_completed_coursesid`, `engineer_inprogress_coursesid`, `engineer_preassigned_coursesid`, `engineer_biddable_coursesid`) VALUES
(002, 'Bob', 'bob@engineer.com', 'engineer002', 'bob002', 'E101, E102, E103, E105', 'E201, E202, E203, E204', 'E206, E207, E208', 'E302, E303, E304');
INSERT INTO `engineers` (`engineer_id`, `engineer_name`, `engineer_email`, `engineer_pwd`, `engineer_teleid`, `engineer_completed_coursesid`, `engineer_inprogress_coursesid`, `engineer_preassigned_coursesid`, `engineer_biddable_coursesid`) VALUES
(003, 'Colin', 'colin@engineer.com', 'engineer003', 'colin003', 'E102, E103, E104, E105', 'E201, E202, E203', 'E207, E208', 'E301, E302, E303');
INSERT INTO `engineers` (`engineer_id`, `engineer_name`, `engineer_email`, `engineer_pwd`, `engineer_teleid`, `engineer_completed_coursesid`, `engineer_inprogress_coursesid`, `engineer_preassigned_coursesid`, `engineer_biddable_coursesid`) VALUES
(004, 'Daniel', 'daniel@engineer.com', 'engineer004', 'daniel004', 'E103, E104, E105', 'E203, E204, E205', 'E206, E207, E208', 'E303, E304, E305' );
INSERT INTO `engineers` (`engineer_id`, `engineer_name`, `engineer_email`, `engineer_pwd`, `engineer_teleid`, `engineer_completed_coursesid`, `engineer_inprogress_coursesid`, `engineer_preassigned_coursesid`, `engineer_biddable_coursesid`) VALUES
(005, 'Emma', 'emma@engineer.com', 'engineer005', 'emma005','E101, E103, E104, E105', 'E201, E203, E204, E205', 'E206, E210', 'E301, E303, E305');


-- -----------------------------------------------------
-- Table `mydb`.`trainers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`trainers` (
  `trainer_id` INT NOT NULL UNIQUE,
  `trainer_name` varchar(64) NOT NULL,
  `trainer_email` varchar(64) NOT NULL,
  `trainer_pwd` varchar(64) NOT NULL,
  `trainer_teleid` varchar(20) NOT NULL,
  `trainer_course_section_id` varchar(200) NOT NULL,

  PRIMARY KEY (`trainer_id`),
  UNIQUE INDEX `trainer_course_section_id_UNIQUE` (`trainer_course_section_id`))
  
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

INSERT INTO trainers(`trainer_id`,`trainer_name`,`trainer_email`,`trainer_pwd`, `trainer_teleid`, `trainer_course_section_id`) VALUES
(761, 'Fred', 'fred@trainer.com', 'trainer761', 'fred7621', 'E101G1, E101G2, E101G3, E102G1, E102G2, E102G3, E201G1, E201G2, E202G1, E202G2, E301G1, E301G2, E301G3, E302G1, E302G2, E302G3'),
(762, 'Grace', 'grace@trainer.com', 'trainer762', 'grace762', 'E103G1, E103G2, E103G3, E203G1, E203G2, E303G1, E303G2, E303G3, E304G1, E304G2, E304G3'),
(763, 'Helen', 'helen@trainer.com', 'trainer763', 'helen763','E104G1, E104G2, E104G3, E105G1, E105G2, E105G3, E204G1, E204G2, E205G1, E205G2, E305G1, E305G2, E305G3'),
(764, 'Isabel', 'isabel@trainer.com', 'trainer764', 'isabel764', 'E206G1, E206G2, E206G3, E207G1, E207G2, E207G3, E208G1, E208G2, E208G3'),
(765, 'John', 'john@trainer.com', 'trainer765', 'john765', 'E209G1, E209G2, E209G3, E210G1, E210G2, E210G3');



-- -----------------------------------------------------
-- Table `mydb`.`hr`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`hr` (
    `hr_id` INT NOT NULL UNIQUE,
    `hr_name` varchar(64) NOT NULL,
    `hr_email` varchar(64) NOT NULL,
    `hr_pwd` varchar(64) NOT NULL,
    PRIMARY KEY (`hr_id`))

ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

INSERT INTO hr(`hr_id`,`hr_name`,`hr_email`,`hr_pwd`) VALUES
(766, 'Kevin', 'kevin@hr.com', 'hr766');
INSERT INTO hr(`hr_id`,`hr_name`,`hr_email`,`hr_pwd`) VALUES
(767, 'Leo', 'leo@hr.com' , 'hr767');
INSERT INTO hr(`hr_id`,`hr_name`,`hr_email`,`hr_pwd`) VALUES
(768, 'Matt', 'matt@hr.com', 'hr768');
INSERT INTO hr(`hr_id`,`hr_name`,`hr_email`,`hr_pwd`) VALUES
(769, 'Nat', 'nat@hr.com', 'hr769');


-- -----------------------------------------------------
-- Table `mydb`.`quiz`
-- -----------------------------------------------------
CREATE TABLE `mydb`.`quiz` (
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
    REFERENCES `mydb`.`trainers` (`trainer_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

-- -----------------------------------------------------
-- Table `mydb`.`course_details`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`course_details` (
    `course_id` varchar(64) NOT NULL UNIQUE,
    `course_name` varchar(100) NOT NULL,
    `course_prerequisite` varchar(64), 
    `course_brief` varchar(200) NOT NULL,
    `total_slots_available` INT,
    `course_period` varchar(64) NOT NULL, 
    `FK_trainer_course_section_id` varchar(200) NOT NULL ,
    `FK_quiz_id` varchar(20), 
    PRIMARY KEY (`course_id`),
	CONSTRAINT `FK_trainer_course_section_id`
		FOREIGN KEY (`FK_trainer_course_section_id`)
		REFERENCES `mydb`.`trainers`(`trainer_course_section_id`),
	CONSTRAINT `FK_quiz_id`
		FOREIGN KEY (`FK_quiz_id`)
		REFERENCES `mydb`.`quiz`(`quiz_id`))


ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

INSERT INTO course_details(`course_id`,`course_name`,`course_prerequisite`,`course_brief`, `total_slots_available`, `course_period`, `FK_trainer_course_section_id`, `FK_quiz_id`) VALUES
('E101', 'Basic Mathematics', NULL , 'This is a Year1 course which would be required to be completed prior to E201 Intermediate Mathematics', '120', 'Term1' , 'E101G1, E101G2, E101G3', 'A101'),
('E102', 'Basic Engineering Mathematics', NULL, 'This is a Year1 course which would be required to be completed prior to Intermediate Mathematics', '120', 'Term1' , 'E102G1, E102G2, E102G3', 'A102'),
('E103', 'Introduction to Engineering', NULL, 'This is a Year1 course which would be required to be completed prior to Engineering Project Management', '120', 'Term1', 'E103G1, E103G2, E103G3', 'A103'),
('E104', 'Principles of Electrical Engineering', NULL, 'This is a Year1 course which would be required to be completed prior to Applications of Electrical Engineering', '120', 'Term1', 'E104G1, E104G2, E104G3', 'A104'),
('E105', 'Engineering Design and Solutions', NULL, 'This is a Year1 course which would be required to be completed prior to Consumer Psychology', '120', 'Term1', 'E105G1, E105G2, E105G3', 'A105'),

('E201', 'Intermediate Mathematics', 'E101', 'This is a Year1 course which requires the completion of E101 Basic Mathematics', '80', 'Term2', 'E201G1, E201G2', 'A201'),
('E202', 'Intermediate Engineering Mathematics', 'E102', 'This is a Year1 course which requires the completion of E102 Basic Engineering Mathematics', '80', 'Term2', 'E202G1, E202G2', 'A202'),
('E203', 'Engineering Project Management','E103' , 'This is a Year1 course which requires the completion of E103 Introduction to Engineering', '80', 'Term2' ,'E2O3G1, E203G2', 'A203'),
('E204', 'Applications of Electrical Engineering', 'E104', 'This is a Year1 course which requires the completion of E104 Principles of Electrical Engineering', '80', 'Term2' ,'E204G1, E204G2', 'A204'),
('E205', 'Consumer Psychology', 'E105','This is a Year1 course which requires the completion of E105 Engineering Design and Solutions', '80', 'Term2' , 'E205G1, E205G2', 'A205'),

('E206', 'Programming for Business', NULL, 'This is a pre-assigned course', '120', 'Term1', 'E206G1, E206G2, E206G3', 'A206'),
('E207', 'Company Overview', NULL, 'This is a pre-assigned course', '120', 'Term1', 'E207G1, E207G2, E207G3', 'A207'),
('E208', 'Company Products', NULL, 'This is a pre-assigned course', '120', 'Term1', 'E208G1, E208G2, E208G3', 'A208'),
('E209', 'Service Operations Management', NULL, 'This is a pre-assigned course', '120', 'Term2', 'E209G1, E209G2, E209G3', 'A209'),
('E210', 'Business Communication', NULL, 'This is a pre-assigned course', '120', 'Term2', 'E210G1, E210G2, E210G3', 'A210'),

('E301', 'Advanced Mathematics', 'E101, E201', 'This is a biddable course, please refer to OASIS for more information', '120', 'Term1', 'E301G1, E301G2, E301G3', NULL),
('E302', 'Advanced Engineering Mathematics', 'E102, E202', 'This is a biddable course, please refer to OASIS for more information', '120', 'Term1', 'E302G1, E302G2, E302G3', NULL),
('E303', 'Emerging Technologies', 'E203', 'This is a biddable course, please refer to OASIS for more information', '120', 'Term1', 'E303G1, E303G2, G3', NULL),
('E304', 'Financial Technology', 'E203', 'This is a biddable course, please refer to OASIS for more information', '120', 'Term1', 'E304G1, E304G2, G3', NULL),
('E305', 'Event Management & Operations', NULL, 'This is a biddable course, please refer to OASIS for more information', '120', 'Term2', 'E30G1, E304G2, E304G3', NULL);


-- -----------------------------------------------------
-- Table `mydb`.`quiz_qn`
-- -----------------------------------------------------
CREATE TABLE `mydb`.`quiz_qn` (
  `qn_id` BIGINT NOT NULL AUTO_INCREMENT,
  `quiz_id` varchar(75) NOT NULL,
  `qn_score` SMALLINT(6) NOT NULL DEFAULT 0,
  `qn_content` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`qn_id`),
  CONSTRAINT `fk_qn_quiz`
    FOREIGN KEY (`quiz_id`)
    REFERENCES `mydb`.`quiz` (`quiz_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`ans_key`
-- -----------------------------------------------------
CREATE TABLE `mydb`.`ans_key` (
  `ans_id` VARCHAR(75) NOT NULL,
  `quiz_id` VARCHAR(75) NOT NULL,
  `qn_id` VARCHAR(75) NOT NULL,
  `correct` TINYINT(1) NOT NULL DEFAULT 0,
  `ans_key` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`ans_id`),
  INDEX `idx_answer_quiz` (`quiz_id` ASC),
  CONSTRAINT `fk_answer_quiz`
    FOREIGN KEY (`quiz_id`)
    REFERENCES `mydb`.`quiz` (`quiz_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;



ALTER TABLE `mydb`.`ans_key` 
ADD INDEX `idx_ans_qn` (`qn_id` ASC);
ALTER TABLE `mydb`.`ans_key` 
ADD CONSTRAINT `fk_ans_qn`
  FOREIGN KEY (`qn_id`)
  REFERENCES `mydb`.`quiz_qn` (`quiz_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


-- -----------------------------------------------------
-- Table `mydb`.`take_table`
-- -----------------------------------------------------
CREATE TABLE `mydb`.`take_table` (
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
    REFERENCES `mydb`.`engineers` (`engineer_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

ALTER TABLE `mydb`.`take_table` 
ADD INDEX `idx_take_quiz` (`quiz_id` ASC);
ALTER TABLE `mydb`.`take_table` 
ADD CONSTRAINT `fk_take_quiz`
  FOREIGN KEY (`quiz_id`)
  REFERENCES `mydb`.`quiz` (`quiz_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


-- -----------------------------------------------------
-- Table `mydb`.`take_ans`
-- -----------------------------------------------------
CREATE TABLE `mydb`.`take_ans` (
  `take_ans_id` BIGINT NOT NULL AUTO_INCREMENT,
  `take_id` VARCHAR(75) NOT NULL,
  `qn_id` BIGINT NOT NULL,
  `ans_id` BIGINT NOT NULL,
  PRIMARY KEY (`take_ans_id`),
  INDEX `idx_answer_take` (`take_id` ASC),
  CONSTRAINT `fk_answer_take`
    FOREIGN KEY (`take_id`)
    REFERENCES `mydb`.`take_table` (`take_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

ALTER TABLE `mydb`.`take_ans` 
ADD INDEX `idx_tanswer_qn` (`qn_id` ASC);
ALTER TABLE `mydb`.`take_ans` 
ADD CONSTRAINT `fk_tanswer_qn`
  FOREIGN KEY (`qn_id`)
  REFERENCES `mydb`.`quiz_qn` (`qn_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `mydb`.`take_ans` 
ADD INDEX `idx_tanswer_answer` (`ans_id` ASC);
ALTER TABLE `mydb`.`take_ans` 
ADD CONSTRAINT `fk_tanswer_answer`
  FOREIGN KEY (`ans_id`)
  REFERENCES `mydb`.`quiz_ans` (`ans_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
  


