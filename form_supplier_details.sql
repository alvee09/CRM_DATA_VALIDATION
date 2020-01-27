-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 27, 2020 at 07:55 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `data_validation`
--

-- --------------------------------------------------------

--
-- Table structure for table `form_supplier_details`
--

CREATE TABLE `form_supplier_details` (
  `id` int(11) NOT NULL,
  `SuppCode` int(11) NOT NULL,
  `SupplierName` varchar(200) NOT NULL,
  `RexNo` varchar(10) NOT NULL,
  `SupplierAddress` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `form_supplier_details`
--

INSERT INTO `form_supplier_details` (`id`, `SuppCode`, `SupplierName`, `RexNo`, `SupplierAddress`) VALUES
(1, 77566, 'EPYLLION KNITWEARS LIMITED', 'BDREX00285', 'EPYLLION KNITWEARS LIMITED PLOT# I/6, I/8, I/10, I/12, ROAD# 06, SEC# 07, MIRPUR I/A 1216 DHAKA Bangladesh'),
(2, 84838, 'SUNG KWANG APPARELS LTD', 'BDREX00648', 'SUNG KWANG APPARELS LTD   Plot No#1384-86,1420-21,Vogra,Bason Sarak Chandona,Gazipur,Bangladesh. 1704 Gazipur   Bangladesh'),
(3, 77548, 'ESQUIRE KNIT COMPOSITE LTD.', 'BDREX00026', 'Esquire Knit Composite Ltd. Kanchpur, Sonargaon 1403 Narayanganj. Bangladesh'),
(4, 77523, 'COMFIT COMPOSITE KNIT LTD.', 'BDREX00329', 'COMFIT COMPOSITE KNIT LTD. 822/2, ROKEYA SARANI 1216 DHAKA Bangladesh'),
(5, 84791, 'IMPRESS-NEWTEX COMPOSITE TEXTILES LIMITED', 'BDREX00216', 'Impress-Newtex composite Textiles Limited Fac:-Gorai I/A Mirzapur Tangail,BD.H/O: 260/B(6th Fl.) Tejgaon I/A   1208 DHAKA Bangladesh'),
(6, 77507, 'PACIFIC JEANS LTD', 'BDREX00232', 'PACIFIC JEANS LTD PLOT#14-19, SECTOR# 05, EXPORT PROCESSING ZONE, 4223 CHATTOGRAM  Bangladesh'),
(7, 84854, 'DIVINE INTIMATES LTD.', 'BDREX00028', 'Divine Intimates Ltd. Khowaz Nagar, P.O. Azimpara, Karnafully,    4370   Chittagong   Bangladesh'),
(8, 77505, 'JEANS 2000 LTD', 'BDREX00233', 'PLOT# 67, SECTOR# 07, EXPORT PROCESSING ZONE,  4223 CHATTOGRAM  Bangladesh'),
(9, 73127, 'BANDO DESIGN LTD/ INFINITY FASHION CO., LIMITED', 'BDREX00442', 'Bando design ltd   Purbo Narshinghapur,Earpur Union Parishad Road,Ashulia,Dhaka 1349 Dhaka  Bangladesh'),
(10, 84833, 'FLAMINGO FASHIONS LIMITED', 'BDREX01054', 'FLAMINGO FASHIONS LIMITED SARDAGANJ, KASHIMPUR, 1700 GAZIPUR  Bangladesh'),
(11, 84803, 'TASNIAH FABRICS LTD', 'BDREX00438', 'TASNIAH FABRICS LTD Nayapara, Kashimpur   1704   Gazipur Bangladesh'),
(12, 77516, 'DEKKO KNITWEARS LIMITED', 'BDREX00286', 'DEKKO KNITWEARS LIMITED   PLOT# I/5, I/7,I/9,I/11,I/13, ROAD#06, SEC#07, MIRPUR I/A,1216  Dhaka  Bangladesh'),
(13, 84722, 'DESIGNTEX SWEATERS LTD', 'BDREX00115', 'DESIGNTEX SWEATERS LTD PLOT NO 255, KONABARI 1346 GAZIPUR Bangladesh'),
(14, 84766, 'PIONEER KNITWEARS (BD) LTD.', 'BDREX00400', 'PIONEER KNITWEARS (BD) LTD. Jamirdia Habirbari, Valuka 2240 Mymensingh Bangladesh'),
(15, 77534, 'NORBAN COMTEX LIMITED.', 'BDREX00847', 'NORBAN COMTEX LIMITED. Mouza- Sarabo, Kashimpur 1346 Gazipur Bangladesh'),
(16, 77539, 'FAKIR APPARELS LTD', 'BDREX00174', 'Fakir Apparels Ltd A-127-131,135-138,142-145 B-501-503 BSCIC Hosiery Shilpa Nagari 1400 Narayanganj Bangladesh'),
(17, 84802, 'A ONE POLAR LTD.', 'BDREX00146', 'A ONE POLAR LTD. VULTA, RUPGONJ 1462 NARAYANGONJ   Bangladesh'),
(18, 84812, 'SOORTY TEXTILES (BD) LTD.', 'BDREX00598', 'SOORTY TEXTILES (BD) LTD. PLOT NO.# 220-227, CUMILLA EPZ 3500 CUMILLA Bangladesh'),
(19, 77525, 'S. F. FASHION WEARS LTD.', 'BDREX00181', 'S. F. FASHION WEARS LTD. NAYABARI, KANCHPUR, SONARGAON 1430 NARAYANGONJ  Bangladesh'),
(20, 84837, 'T-DESIGN KNITWEAR LTD.', 'BDREX00114', 'T-DESIGN KNITWEAR LTD. BOHERARCHALA, SHREEPUR 1740 GAZIPUR Bangladesh'),
(21, 84799, 'AL-ISLAM TEXTILES LTD', 'BDREX00618', 'AL-ISLAM TEXTILES LTD 9, Karnapara, Savar, Dhaka. 1340 DHAKA Bangladesh'),
(22, 77580, 'MIDLAND KNITWEAR LTD.', 'BDREX00147', 'MIDLAND KNITWEAR LTD. RAMARBAGH, KUTUBPUR, FATULLAH 1420 NARAYANGONJ Bangladesh'),
(23, 84827, 'JAY JAY MILLS (BANGLADESH) PRIVATE LIMITED', 'BDREX01750', 'Jay Jay Mills (Bangladesh) Private Limited Plot Nos: 2-4 & 9-11, Sector 7/A, CEPZ, South Halishahar 4223  Chittagong Bangladesh'),
(24, 77591, 'PACIFIC BLUE (JEANS WEAR) LTD', 'BDREX00774', 'PACIFIC BLUE (JEANS WEAR) LTD 14 Gedda Karnapara Ulail, Savar-1340, Dhaka, Bangladesh'),
(25, 77545, 'DEBONAIR LIMITED', 'BDREX00412', 'DEBONAIR LIMITED GORAT, ASHULIA SAVAR-1341 DHAKA BANGLADESH');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `form_supplier_details`
--
ALTER TABLE `form_supplier_details`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `form_supplier_details`
--
ALTER TABLE `form_supplier_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
