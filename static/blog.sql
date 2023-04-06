-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 06, 2023 at 04:52 AM
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
-- Database: `blog`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `message` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`sno`, `name`, `email`, `phone`, `message`, `date`) VALUES
(2, 'ldksja;lkasf', 'lkds@gmail.com', '987484873', ';djflksadlksmd;kmas;m', '2023-04-01 21:19:12'),
(3, 'Munakala partha saradhi', 'parthasaradhimunakala@gmail.com', '06304595197', 'This is a test to check email sending', '2023-04-01 22:55:07'),
(4, 'Munakala partha saradhi', 'parthasaradhimunakala@gmail.com', '06304595197', 'This is a test to check email sending', '2023-04-01 22:55:46'),
(5, 'Munakala partha saradhi', 'parthasaradhimunakala@gmail.com', '06304595197', 'this is a test', '2023-04-01 22:56:17'),
(6, 'Vinay gundam ', 'vinay@gmail.com', '06304595197', 'I am testing this page', '2023-04-02 12:16:33');

-- --------------------------------------------------------

--
-- Table structure for table `post`
--

CREATE TABLE `post` (
  `sno` int(50) NOT NULL,
  `title` text NOT NULL,
  `content` text NOT NULL,
  `slug` varchar(20) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `img_file` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `post`
--

INSERT INTO `post` (`sno`, `title`, `content`, `slug`, `date`, `img_file`) VALUES
(1, 'this is the first post on the blog ', 'lkfmlssmfldsaknf', 'first-post', '2023-04-04 12:18:14', 'about-bg.jpg'),
(2, 'This is my second post in this blog I hope you like it', '                        Let\'s GO!!!!!!!!!\r\n      \r\n      \r\n      ', 'second-pos', '2023-04-04 12:31:49', 'home-bg.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `post`
--
ALTER TABLE `post`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
