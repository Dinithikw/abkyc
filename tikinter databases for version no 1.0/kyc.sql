-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 19, 2021 at 01:11 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kyc`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact_information`
--

CREATE TABLE `contact_information` (
  `NIC` varchar(20) NOT NULL,
  `House No` varchar(10) NOT NULL,
  `Street` varchar(25) NOT NULL,
  `City` varchar(50) NOT NULL,
  `Postal Code` int(10) NOT NULL,
  `Country` varchar(50) NOT NULL,
  `Phone No..` tinyint(20) NOT NULL,
  `Mobile No.` varchar(20) NOT NULL,
  `E-mail` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `employment_information`
--

CREATE TABLE `employment_information` (
  `NIC` varchar(15) NOT NULL,
  `Employment Status` varchar(15) NOT NULL,
  `Occupation` varchar(25) NOT NULL,
  `Job Title` varchar(25) NOT NULL,
  `Industry` varchar(25) NOT NULL,
  `Length of Services` int(5) NOT NULL,
  `Source of Income` text NOT NULL,
  `Average Income` text NOT NULL,
  `Transaction Mode` varchar(15) NOT NULL,
  `Operating Authority` varchar(15) NOT NULL,
  `Banking Products` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `identity_information`
--

CREATE TABLE `identity_information` (
  `serial_no` int(50) NOT NULL,
  `identification_code` text NOT NULL,
  `name_with_initials` varchar(50) NOT NULL,
  `name_in_full` text NOT NULL,
  `NIC` varchar(12) NOT NULL,
  `passport` varchar(50) NOT NULL,
  `driving_license` varchar(50) NOT NULL,
  `expiration_date_passport` date NOT NULL,
  `expiration_date_driving_license` date NOT NULL,
  `nationality` varchar(25) NOT NULL,
  `DOB` date NOT NULL,
  `face_recognition` blob NOT NULL,
  `finger_print1` blob NOT NULL,
  `finger_print2` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `identity_information`
--

INSERT INTO `identity_information` (`serial_no`, `identification_code`, `name_with_initials`, `name_in_full`, `NIC`, `passport`, `driving_license`, `expiration_date_passport`, `expiration_date_driving_license`, `nationality`, `DOB`, `face_recognition`, `finger_print1`, `finger_print2`) VALUES
(1, '', 'dsk', 'dinithi', '985310165V', '123', '456', '0000-00-00', '0000-00-00', 'sri lankan', '1998-01-31', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `office_use`
--

CREATE TABLE `office_use` (
  `NIC` varchar(20) NOT NULL,
  `Date (form fill)` date NOT NULL,
  `Account No.` varchar(50) NOT NULL,
  `Branch No.` varchar(20) NOT NULL,
  `Officer's S/No.` varchar(25) NOT NULL,
  `Manager's INTL` varchar(25) NOT NULL,
  `Risk Category` varchar(20) NOT NULL,
  `Name of the Officer` varchar(100) NOT NULL,
  `Signature of the Officer` text NOT NULL,
  `Date (sign by the officer)` date NOT NULL,
  `Name of the Manager` varchar(100) NOT NULL,
  `Signature of the Manager` varchar(50) NOT NULL,
  `Date (sign by the Manager)` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact_information`
--
ALTER TABLE `contact_information`
  ADD PRIMARY KEY (`NIC`);

--
-- Indexes for table `employment_information`
--
ALTER TABLE `employment_information`
  ADD PRIMARY KEY (`NIC`);

--
-- Indexes for table `identity_information`
--
ALTER TABLE `identity_information`
  ADD PRIMARY KEY (`serial_no`);

--
-- Indexes for table `office_use`
--
ALTER TABLE `office_use`
  ADD PRIMARY KEY (`NIC`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `identity_information`
--
ALTER TABLE `identity_information`
  MODIFY `serial_no` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
