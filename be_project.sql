-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 19, 2019 at 10:59 PM
-- Server version: 10.1.30-MariaDB
-- PHP Version: 7.2.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `be_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `date`
--

CREATE TABLE `date` (
  `date` date NOT NULL,
  `f1` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `date`
--

INSERT INTO `date` (`date`, `f1`) VALUES
('2019-01-15', 0.33),
('2019-01-16', 0.33),
('2019-01-17', 1),
('2019-01-18', 0.33),
('2019-01-19', 0.66),
('2019-01-20', 0.66),
('2019-02-08', 0.33),
('2019-04-17', 0.33),
('2019-04-18', 1);

-- --------------------------------------------------------

--
-- Table structure for table `parkinginfo`
--

CREATE TABLE `parkinginfo` (
  `parkingid` int(11) NOT NULL,
  `occupied` int(11) NOT NULL,
  `max` int(11) NOT NULL,
  `parkingrate` float NOT NULL,
  `parkname` varchar(50) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `parkinginfo`
--

INSERT INTO `parkinginfo` (`parkingid`, `occupied`, `max`, `parkingrate`, `parkname`) VALUES
(1, 6, 10, 16.8636, 'ABC PARKING '),
(2, 6, 15, 9.88461, 'PAY AND PARK'),
(3, 4, 20, 8.88889, 'PMC PARKING');

-- --------------------------------------------------------

--
-- Table structure for table `prediction_1`
--

CREATE TABLE `prediction_1` (
  `time` int(20) NOT NULL,
  `occd` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `prediction_1`
--

INSERT INTO `prediction_1` (`time`, `occd`) VALUES
(0, 18.6933),
(1, 21.1654),
(2, 23.6375),
(3, 26.1095),
(4, 28.5816),
(5, 31.0537),
(6, 33.5258),
(7, 35.9979),
(8, 38.47),
(9, 40.942),
(10, 43.4141),
(11, 45.8862),
(12, 48.3583),
(13, 50.8304),
(14, 53.3025),
(15, 55.7745),
(16, 58.2466),
(17, 60.7187),
(18, 63.1908),
(19, 65.6629),
(20, 68.1349),
(21, 70.607),
(22, 73.0791),
(23, 75.5512);

-- --------------------------------------------------------

--
-- Table structure for table `prediction_2`
--

CREATE TABLE `prediction_2` (
  `time` int(11) NOT NULL,
  `occd` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `prediction_2`
--

INSERT INTO `prediction_2` (`time`, `occd`) VALUES
(0, 18.436),
(1, 20.9081),
(2, 23.3801),
(3, 25.8522),
(4, 28.3243),
(5, 30.7964),
(6, 33.2685),
(7, 35.7406),
(8, 38.2127),
(9, 40.6847),
(10, 43.1568),
(11, 45.6289),
(12, 48.101),
(13, 50.5731),
(14, 53.0452),
(15, 55.5172),
(16, 57.9893),
(17, 60.4614),
(18, 62.9335),
(19, 65.4056),
(20, 67.8776),
(21, 70.3497),
(22, 72.8218),
(23, 75.2939);

-- --------------------------------------------------------

--
-- Table structure for table `prediction_3`
--

CREATE TABLE `prediction_3` (
  `time` int(11) NOT NULL,
  `occd` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `prediction_3`
--

INSERT INTO `prediction_3` (`time`, `occd`) VALUES
(0, 18.1787),
(1, 20.6508),
(2, 23.1228),
(3, 25.5949),
(4, 28.067),
(5, 30.5391),
(6, 33.0112),
(7, 35.4833),
(8, 37.9553),
(9, 40.4274),
(10, 42.8995),
(11, 45.3716),
(12, 47.8437),
(13, 50.3158),
(14, 52.7878),
(15, 55.2599),
(16, 57.732),
(17, 60.2041),
(18, 62.6762),
(19, 65.1483),
(20, 67.6203),
(21, 70.0924),
(22, 72.5645),
(23, 75.0366);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `date`
--
ALTER TABLE `date`
  ADD PRIMARY KEY (`date`);

--
-- Indexes for table `parkinginfo`
--
ALTER TABLE `parkinginfo`
  ADD PRIMARY KEY (`parkingid`);

--
-- Indexes for table `prediction_1`
--
ALTER TABLE `prediction_1`
  ADD PRIMARY KEY (`time`);

--
-- Indexes for table `prediction_2`
--
ALTER TABLE `prediction_2`
  ADD PRIMARY KEY (`time`);

--
-- Indexes for table `prediction_3`
--
ALTER TABLE `prediction_3`
  ADD PRIMARY KEY (`time`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `prediction_2`
--
ALTER TABLE `prediction_2`
  MODIFY `time` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `prediction_3`
--
ALTER TABLE `prediction_3`
  MODIFY `time` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
