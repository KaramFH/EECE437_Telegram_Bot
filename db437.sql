-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 14, 2021 at 05:26 PM
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
  `LocationLatitude` float DEFAULT NULL,
  `LocationLongitude` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `campaign`
--

INSERT INTO `campaign` (`CampaignID`, `UserID`, `Name`, `Description`, `StartDate`, `EndDate`, `LocationLatitude`, `LocationLongitude`) VALUES
(0, 1470290214, 'Yo', ' Ehh', NULL, NULL, 33.6887, 35.6297);

-- --------------------------------------------------------

--
-- Table structure for table `donationlog`
--

CREATE TABLE `donationlog` (
  `DonationID` int(11) NOT NULL,
  `OfferingID` int(11) DEFAULT NULL,
  `NeedID` int(11) DEFAULT NULL,
  `DonationDate` varchar(45) DEFAULT NULL,
  `Is_Pickedup` int(11) DEFAULT 0,
  `DeliveryDate` varchar(45) DEFAULT NULL,
  `IsDelivered` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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
(3, 'home essentials', 300, '1'),
(4, 'Bayt', 2147483647, '0'),
(5, 'Car', 99999, '0'),
(6, 'Phone', 1000000, '0'),
(10, 'Clothes', 69, '0'),
(11, 'Books', 9000, '0'),
(14, 'Mattresses', 676, '0');

-- --------------------------------------------------------

--
-- Table structure for table `need`
--

CREATE TABLE `need` (
  `NeedID` int(11) NOT NULL,
  `DonationTypeID` int(11) DEFAULT NULL,
  `UserID` int(11) DEFAULT NULL,
  `Date` varchar(45) DEFAULT NULL,
  `CashValue` int(11) DEFAULT NULL,
  `QuantityAmount` int(11) DEFAULT NULL,
  `QuantityRemaining` int(11) DEFAULT NULL,
  `Description` varchar(45) DEFAULT NULL,
  `Matched` int(11) DEFAULT 0,
  `Assigned` int(11) DEFAULT 0,
  `isActive` tinyint(4) DEFAULT 1,
  `confirmed` int(11) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `need`
--

INSERT INTO `need` (`NeedID`, `DonationTypeID`, `UserID`, `Date`, `CashValue`, `QuantityAmount`, `QuantityRemaining`, `Description`, `Matched`, `Assigned`, `isActive`, `confirmed`) VALUES
(1, 2, 1448273288, NULL, 100, 10, 10, 'Aub is a tyrant and i need to sleep plz', 0, 1, 0, 0),
(2, 3, 1470290214, NULL, 0, 1, 1, 'I need a daffeye', 0, 1, 1, 0),
(5, 1, 1470290214, NULL, 0, 1, 1, '1000', 0, 1, 1, 0),
(6, 1, 1470290214, NULL, 0, 100, 100, '1000000$', 0, 0, 1, 0),
(7, 2, 1470290214, NULL, 0, 1, 1, 'Profinal', 0, 1, 0, 1),
(8, 3, 1470290214, NULL, 0, 1, 1, 'Coach', 0, 0, 1, 0),
(9, 3, 1470290214, NULL, 0, 1, 1, 'Coach', 0, 0, 1, 0),
(10, 10, 1470290214, NULL, 0, 1, 1, '&&', 0, 0, 1, 0),
(11, 11, 1470290214, NULL, 44848, 5, 5, 'nnfwobfowebf', 0, 0, 1, 0),
(12, 14, 1470290214, NULL, 0, 1, 1, 'Big mattress', 0, 1, 1, 0),
(13, 6, 1448273288, NULL, 0, 250, 250, 'I need a phone for my daughter to go to unive', 0, 0, 1, 0);

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
  `IsActive` tinyint(4) DEFAULT NULL,
  `Assigned` int(11) DEFAULT 0,
  `IsPickedUp` int(11) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `offering`
--

INSERT INTO `offering` (`OfferingID`, `UserID`, `DonationTypeID`, `description`, `QuantityAmount`, `QuantityRemaining`, `Date`, `IsActive`, `Assigned`, `IsPickedUp`) VALUES
(2, 1470290214, 2, '  i will be giving coronavirus vaccines for free ', 20, 20, '2020-12-17 23:56:52', 1, 1, 1),
(3, 1470290214, 2, ' Panadol ', 1, 1, '2021-01-06 20:59:47', 1, 1, 1),
(4, 1470290214, 3, ' Fridge ', 1, 1, '2021-01-07 16:37:30', 1, 1, 1),
(5, 1470290214, 14, ' ()&@7( ', 20, 20, '2021-01-07 19:04:43', 1, 1, 0),
(6, 1448273288, 6, ' I will give away a sumsung phone ', 5, 5, '2021-01-12 21:54:25', 1, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `UserID` int(11) NOT NULL,
  `FirstName` varchar(45) NOT NULL,
  `LastName` varchar(45) NOT NULL,
  `Birthdate` varchar(45) DEFAULT NULL,
  `PhoneNumber` varchar(45) DEFAULT NULL,
  `AddressLatitude` float DEFAULT NULL,
  `AddressLongitude` float DEFAULT NULL,
  `AddressDescription` varchar(45) DEFAULT NULL,
  `CreationDate` varchar(45) DEFAULT current_timestamp(),
  `ChatID` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`UserID`, `FirstName`, `LastName`, `Birthdate`, `PhoneNumber`, `AddressLatitude`, `AddressLongitude`, `AddressDescription`, `CreationDate`, `ChatID`) VALUES
(1448273288, 'Hassan', ' Chehaitly', '170799', '79100605', 3.1, 3.2, 'k', '2020-12-18 19:38:20', '1448273288'),
(1470290214, 'Karam', ' Hasan', '020899', '78814068', 33.6699, 35.5988, 'Bakaata', '2021-01-02 22:08:33', '1470290214');

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
  `Offer_pickup_id` varchar(255) DEFAULT NULL,
  `NeedTodeliver_id` varchar(255) DEFAULT NULL,
  `PickedUp_offersID` varchar(255) DEFAULT NULL,
  `DeliveredNeeds_id` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `volunteer`
--

INSERT INTO `volunteer` (`userID`, `ChatID`, `FirstName`, `LastName`, `State`, `Offer_pickup_id`, `NeedTodeliver_id`, `PickedUp_offersID`, `DeliveredNeeds_id`) VALUES
(1448273288, 1448273288, 'Hassan', 'Chehaitly', 3, '2,5', '5,12', NULL, NULL),
(1470290214, 1470290214, 'Karam', 'Hasan', 5, '3,2,2,3,4', '1,7', 'None,3,3,3,3,3,4,4,4,4', '1,1,7');

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
  MODIFY `DonationTypeID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `need`
--
ALTER TABLE `need`
  MODIFY `NeedID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `offering`
--
ALTER TABLE `offering`
  MODIFY `OfferingID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `UserID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1470290215;

--
-- AUTO_INCREMENT for table `volunteer`
--
ALTER TABLE `volunteer`
  MODIFY `userID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1470290215;

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
