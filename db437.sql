-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 28, 2020 at 01:38 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db437`
--

-- --------------------------------------------------------

--
-- Table structure for table `campaign`
--

CREATE TABLE `campaign` (
  `CampaignID` int(11) NOT NULL,
  `UserID` int(11) NOT NULL,
  `Name` varchar(45) NOT NULL,
  `Description` varchar(45) DEFAULT NULL,
  `StartDate` varchar(45) DEFAULT NULL,
  `EndDate` varchar(45) DEFAULT NULL,
  `LocationLatitude` varchar(45) DEFAULT NULL,
  `LocationLongitude` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `donationlog`
--

CREATE TABLE `donationlog` (
  `DonationID` int(11) NOT NULL,
  `OfferingID` int(11) DEFAULT NULL,
  `NeedID` int(11) DEFAULT NULL,
  `DonationDate` varchar(45) DEFAULT NULL,
  `Is_Pickedup` int(11) DEFAULT NULL,
  `DeliveryDate` varchar(45) DEFAULT NULL,
  `IsDelivered` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `donationlog`
--

INSERT INTO `donationlog` (`DonationID`, `OfferingID`, `NeedID`, `DonationDate`, `Is_Pickedup`, `DeliveryDate`, `IsDelivered`) VALUES
(5, 1, 1, NULL, NULL, NULL, '0'),
(6, 1, 1, NULL, NULL, NULL, '0');

-- --------------------------------------------------------

--
-- Table structure for table `donationtype`
--

CREATE TABLE `donationtype` (
  `DonationTypeID` int(11) NOT NULL,
  `DonationTypeName` varchar(45) DEFAULT NULL,
  `Value` int(11) DEFAULT NULL,
  `IsValidated` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `donationtype`
--

INSERT INTO `donationtype` (`DonationTypeID`, `DonationTypeName`, `Value`, `IsValidated`) VALUES
(1, 'monetary', NULL, '1'),
(2, 'medical', 30, '1'),
(3, 'home essentials', 300, '1');

-- --------------------------------------------------------

--
-- Table structure for table `need`
--

CREATE TABLE `need` (
  `NeedID` int(11) NOT NULL,
  `DonationTypeID` int(11) DEFAULT NULL,
  `UserID` int(11) DEFAULT NULL,
  `Date` varchar(45) DEFAULT NULL,
  `isActive` tinyint(4) DEFAULT 1,
  `CashValue` int(11) DEFAULT NULL,
  `QuantityAmount` int(11) DEFAULT NULL,
  `QuantityRemaining` int(11) DEFAULT NULL,
  `Description` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `need`
--

INSERT INTO `need` (`NeedID`, `DonationTypeID`, `UserID`, `Date`, `isActive`, `CashValue`, `QuantityAmount`, `QuantityRemaining`, `Description`) VALUES
(1, 2, 1448273288, NULL, 1, 100, 10, 10, 'Aub is a tyrant and i need to sleep plz');

-- --------------------------------------------------------

--
-- Table structure for table `offering`
--

CREATE TABLE `offering` (
  `OfferingID` int(11) NOT NULL,
  `UserID` int(11) DEFAULT NULL,
  `DonationTypeID` int(11) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `QuantityAmount` int(11) DEFAULT NULL,
  `QuantityRemaining` int(11) DEFAULT NULL,
  `Date` datetime DEFAULT current_timestamp(),
  `IsActive` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `offering`
--

INSERT INTO `offering` (`OfferingID`, `UserID`, `DonationTypeID`, `description`, `QuantityAmount`, `QuantityRemaining`, `Date`, `IsActive`) VALUES
(1, 9, 2, 'i will be giving coronavirus vaccines for free', 20, 20, '2020-12-17 23:56:19', 1),
(2, 9, 2, '  i will be giving coronavirus vaccines for free ', 20, 20, '2020-12-17 23:56:52', 1);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `UserID` int(11) NOT NULL,
  `FirstName` varchar(45) NOT NULL,
  `LastName` varchar(45) NOT NULL,
  `Birthdate` varchar(45) DEFAULT NULL,
  `PhoneNumber` varchar(45) NOT NULL,
  `AddressLatitude` varchar(45) DEFAULT NULL,
  `AddressLongitude` varchar(45) DEFAULT NULL,
  `AddressDescription` varchar(45) DEFAULT NULL,
  `CreationDate` varchar(45) DEFAULT current_timestamp(),
  `ChatID` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`UserID`, `FirstName`, `LastName`, `Birthdate`, `PhoneNumber`, `AddressLatitude`, `AddressLongitude`, `AddressDescription`, `CreationDate`, `ChatID`) VALUES
(1, 'Karam', 'matte', '', '03123456', 'jabal', 'NA', '', 'nsit', '12321'),
(9, 'hassan', 'ch', '', '03333333', 'NA', 'NA', '', 'lyom', '123'),
(10, 'Abbas', 'Mcheik', 'may 5 1997', '76887339', 'NA', 'NA', '7add el 7ajiz', 'lyom', '123makhassak'),
(21, 'hassan', ' sha7sh7', '07/17/99', '7892868722', NULL, NULL, NULL, '2020-12-18 00:15:10', '123'),
(1448273288, 'Hassan', ' Chehaitly', '170799', '79100605', NULL, NULL, NULL, '2020-12-18 19:38:20', '1448273288');

-- --------------------------------------------------------

--
-- Table structure for table `volunteer`
--

CREATE TABLE `volunteer` (
  `userID` int(20) NOT NULL,
  `ChatID` int(11) NOT NULL,
  `FirstName` varchar(255) NOT NULL,
  `LastName` varchar(255) NOT NULL,
  `State` int(20) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `Offer_pickup_id` int(11) DEFAULT NULL,
  `NeedTodeliver_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `volunteer`
--

INSERT INTO `volunteer` (`userID`, `ChatID`, `FirstName`, `LastName`, `State`, `address`, `Offer_pickup_id`, `NeedTodeliver_id`) VALUES
(1448273288, 1448273288, 'Hassan', 'Chehaitly', 1, NULL, NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `campaign`
--
ALTER TABLE `campaign`
  ADD PRIMARY KEY (`CampaignID`),
  ADD KEY `FKUserID_idx` (`UserID`);

--
-- Indexes for table `donationlog`
--
ALTER TABLE `donationlog`
  ADD PRIMARY KEY (`DonationID`),
  ADD KEY `FKOfferingID_idx` (`OfferingID`),
  ADD KEY `FKNeedID_idx` (`NeedID`);

--
-- Indexes for table `donationtype`
--
ALTER TABLE `donationtype`
  ADD PRIMARY KEY (`DonationTypeID`);

--
-- Indexes for table `need`
--
ALTER TABLE `need`
  ADD PRIMARY KEY (`NeedID`),
  ADD KEY `FKDonationTypeID_idx` (`DonationTypeID`),
  ADD KEY `FKUserID_idx` (`UserID`);

--
-- Indexes for table `offering`
--
ALTER TABLE `offering`
  ADD PRIMARY KEY (`OfferingID`),
  ADD KEY `FKDonationTypeID_idx` (`DonationTypeID`),
  ADD KEY `FKUserID_idx` (`UserID`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`UserID`),
  ADD KEY `FKChatID_idx` (`ChatID`);

--
-- Indexes for table `volunteer`
--
ALTER TABLE `volunteer`
  ADD PRIMARY KEY (`userID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `donationlog`
--
ALTER TABLE `donationlog`
  MODIFY `DonationID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `donationtype`
--
ALTER TABLE `donationtype`
  MODIFY `DonationTypeID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `need`
--
ALTER TABLE `need`
  MODIFY `NeedID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `offering`
--
ALTER TABLE `offering`
  MODIFY `OfferingID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `UserID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1448273289;

--
-- AUTO_INCREMENT for table `volunteer`
--
ALTER TABLE `volunteer`
  MODIFY `userID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1448273289;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `campaign`
--
ALTER TABLE `campaign`
  ADD CONSTRAINT `FKUserID1` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`);

--
-- Constraints for table `donationlog`
--
ALTER TABLE `donationlog`
  ADD CONSTRAINT `FKNeedID` FOREIGN KEY (`NeedID`) REFERENCES `need` (`NeedID`),
  ADD CONSTRAINT `FKOfferingID` FOREIGN KEY (`OfferingID`) REFERENCES `offering` (`OfferingID`);

--
-- Constraints for table `need`
--
ALTER TABLE `need`
  ADD CONSTRAINT `FKDonationTypeID1` FOREIGN KEY (`DonationTypeID`) REFERENCES `donationtype` (`DonationTypeID`),
  ADD CONSTRAINT `FKUserID2` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`);

--
-- Constraints for table `offering`
--
ALTER TABLE `offering`
  ADD CONSTRAINT `FKDonationTypeID2` FOREIGN KEY (`DonationTypeID`) REFERENCES `donationtype` (`DonationTypeID`),
  ADD CONSTRAINT `FKUserID3` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
