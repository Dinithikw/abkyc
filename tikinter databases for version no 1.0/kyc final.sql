-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 19, 2021 at 05:50 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.2

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
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `zipcode` int(10) DEFAULT NULL,
  `price_paid` decimal(10,2) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`first_name`, `last_name`, `zipcode`, `price_paid`, `user_id`, `email`, `address`, `city`, `phone`) VALUES
('chathura', 'madusanka', NULL, NULL, 1, NULL, 'kalutara', NULL, NULL),
('mahushi', 'rajapaksha', NULL, NULL, 2, NULL, 'kagalla', NULL, NULL),
('chathura', 'jayashinghe', NULL, NULL, 3, NULL, 'panadura', NULL, NULL),
('madhushi', 'kankanam', NULL, NULL, 4, NULL, 'dkella', NULL, NULL),
('kamal', 'somarathne', NULL, NULL, 5, NULL, 'galle', NULL, NULL);

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
  `face_recognition` varchar(5) NOT NULL,
  `finger_print1` varchar(10) NOT NULL,
  `finger_print2` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `identity_information`
--

INSERT INTO `identity_information` (`serial_no`, `identification_code`, `name_with_initials`, `name_in_full`, `NIC`, `passport`, `driving_license`, `expiration_date_passport`, `expiration_date_driving_license`, `nationality`, `DOB`, `face_recognition`, `finger_print1`, `finger_print2`) VALUES
(7, '', 'chathura', 'madusanka', '940792908v', '', '', '0000-00-00', '0000-00-00', 'srilankan', '1994-03-19', '0.36', '1234', ''),
(8, '', 'chathura', 'kamal', '123456789v', '', '', '0000-00-00', '0000-00-00', 'srilankan', '1995-01-01', '0.44', '1598', ''),
(9, '', 'madhushi', 'rajapaksha', '987654321v', '', '', '0000-00-00', '0000-00-00', 'srilankan', '1995-10-04', '0.65', '1010', ''),
(61, '', 'isuru', 'supasan', '931900862v', '', '', '0000-00-00', '0000-00-00', '', '0000-00-00', '0.35', '1256', '');

-- --------------------------------------------------------

--
-- Table structure for table `identity_information_clone`
--

CREATE TABLE `identity_information_clone` (
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
  `face_recognition` varchar(5) NOT NULL,
  `finger_print1` varchar(10) NOT NULL,
  `finger_print2` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`user_id`);

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
-- Indexes for table `identity_information_clone`
--
ALTER TABLE `identity_information_clone`
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
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `identity_information`
--
ALTER TABLE `identity_information`
  MODIFY `serial_no` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=62;

--
-- AUTO_INCREMENT for table `identity_information_clone`
--
ALTER TABLE `identity_information_clone`
  MODIFY `serial_no` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
