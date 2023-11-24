-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 23, 2023 at 05:40 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `expert_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `module`
--

CREATE TABLE `module` (
  `module` varchar(100) NOT NULL,
  `no_of_credits` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `module`
--

INSERT INTO `module` (`module`, `no_of_credits`) VALUES
('CMP1221', 4),
('CMP2003', 4),
('DEL1001', 4),
('ELE1002', 4),
('ELE1003', 4),
('ENG1001', 3),
('ENG1005', 1),
('LAW1001', 4),
('MAR1201', 3),
('MAT5003', 4);

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `student_id` varchar(10) NOT NULL,
  `student_name` varchar(150) NOT NULL,
  `student_email` varchar(100) NOT NULL,
  `school` varchar(100) NOT NULL,
  `programme` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`student_id`, `student_name`, `student_email`, `school`, `programme`) VALUES
('1236547', 'Martin Kenzis', 'Mk@gmail.com', 'SCIT', ''),
('1800234', 'Lexis Fuller', 'LF@utech.com', 'SCIT', 'Bsc Electrical Engineering'),
('1900394', 'Alexis Martin', 'AMM@gmail.com', 'SCIT', 'Ms Information Systems'),
('1900657', 'Allison Martin', 'AM@gmail.com', 'SCIT', 'Bsc Computing'),
('1988374', 'Carin Lexier', 'CL@utech.edu.jm', 'SCIT', 'Bsc Electrical Engineering'),
('200342', 'Ashley Carter', 'Ac@utech.com', 'FOW', 'Law'),
('3003432', 'Preston Carnegie', 'Pc@utech.com', 'SCIT', 'Ms Information Systems'),
('40023664', 'Elaine Fuller', 'EF@utech.com', 'SCIT', 'BS Computing'),
('5000023', 'Kehlin Keller', 'KK@utech.com', 'SCIT', 'Bsc Electrical Engineering'),
('6000364', 'Frank', 'F@utech.com', 'SCIT', 'Bsc Electrical Engineering'),
('7004053', 'Candes Lingot', 'CL@utech.com', 'SCIT', 'Bsc Computing');

-- --------------------------------------------------------

--
-- Stand-in structure for view `student_gpa_view`
-- (See below for the actual view)
--
CREATE TABLE `student_gpa_view` (
`student_id` varchar(10)
,`student_name` varchar(150)
,`student_email` varchar(100)
,`programme` varchar(100)
,`school` varchar(100)
,`academic_year` varchar(9)
,`grade_points` double
);

-- --------------------------------------------------------

--
-- Table structure for table `student_progress`
--

CREATE TABLE `student_progress` (
  `module` varchar(100) NOT NULL,
  `student_id` varchar(10) NOT NULL,
  `academic_year` varchar(9) NOT NULL,
  `semester` int(11) NOT NULL,
  `grade_points` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student_progress`
--

INSERT INTO `student_progress` (`module`, `student_id`, `academic_year`, `semester`, `grade_points`) VALUES
('CMP1221', '1900394', '2023/2024', 1, 2.2),
('CMP1221', '1900394', '2023/2024', 2, 4.2),
('CMP1221', '3660584', '2023/2024', 1, 2.2),
('CMP1221', '6000364', '2023/2024', 1, 4.1),
('CMP2003', '1236547', '2023/2024', 1, 2.2),
('ELE1002', '200342', '2022/2023', 1, 2.2),
('ELE1002', '6000364', '2023/2024', 1, 2.2),
('ELE1003', '6000364', '2023/2024', 1, 2.2),
('ENG1001', '1800234', '2023/2024', 1, 3.3),
('ENG1001', '1900657', '2023/2024', 1, 2.3),
('ENG1001', '1900657', '2023/2024', 2, 3.6),
('ENG1005', '1236547', '2023/2024', 1, 2.2),
('ENG1005', '1800234', '2023/2024', 2, 3.4),
('ENG1005', '1900657', '2022/2023', 1, 2.2),
('ENG1005', '3660584', '2023/2024', 1, 3.2),
('ENG1005', '6000364', '2023/2024', 1, 2.2),
('ENG1005', '7004053', '2023/2024', 2, 3.2),
('LAW1001', '200342', '2023/2024', 1, 4.2),
('LAW1001', '6000364', '2023/2024', 1, 2.2),
('MAR1201', '1900394', '2022/2023', 1, 3.2),
('MAR1201', '3660584', '2023/2024', 2, 4.2),
('MAR1201', '7004053', '2023/2024', 1, 2.1),
('MAT5003', '200342', '2023/2024', 1, 3.6),
('MAT5003', '3660584', '2023/2024', 1, 3.2),
('MAT5003', '40023664', '2023/2024', 1, 2.2),
('MAT5003', '7004053', '2023/2024', 1, 3.5);

-- --------------------------------------------------------

--
-- Stand-in structure for view `student_progress_view`
-- (See below for the actual view)
--
CREATE TABLE `student_progress_view` (
`student_id` varchar(10)
,`student_name` varchar(150)
,`module` varchar(100)
,`academic_year` varchar(9)
);

-- --------------------------------------------------------

--
-- Structure for view `student_gpa_view`
--
DROP TABLE IF EXISTS `student_gpa_view`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `student_gpa_view`  AS SELECT `sp`.`student_id` AS `student_id`, `s`.`student_name` AS `student_name`, `s`.`student_email` AS `student_email`, `s`.`programme` AS `programme`, `s`.`school` AS `school`, `sp`.`academic_year` AS `academic_year`, `sp`.`grade_points` AS `grade_points` FROM (`student_progress` `sp` join `student` `s` on(`sp`.`student_id` = `s`.`student_id`))  ;

-- --------------------------------------------------------

--
-- Structure for view `student_progress_view`
--
DROP TABLE IF EXISTS `student_progress_view`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `student_progress_view`  AS SELECT `sp`.`student_id` AS `student_id`, `s`.`student_name` AS `student_name`, `sp`.`module` AS `module`, `sp`.`academic_year` AS `academic_year` FROM (`student_progress` `sp` join `student` `s` on(`sp`.`student_id` = `s`.`student_id`))  ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `module`
--
ALTER TABLE `module`
  ADD PRIMARY KEY (`module`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`student_id`);

--
-- Indexes for table `student_progress`
--
ALTER TABLE `student_progress`
  ADD PRIMARY KEY (`module`,`student_id`,`semester`),
  ADD KEY `student_id` (`student_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
