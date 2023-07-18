-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 18, 2023 at 08:26 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rms`
--

-- --------------------------------------------------------

--
-- Table structure for table `bill`
--

CREATE TABLE `bill` (
  `id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `total_amount` int(11) NOT NULL,
  `payment_status` varchar(50) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bill`
--

INSERT INTO `bill` (`id`, `order_id`, `total_amount`, `payment_status`, `created_at`, `updated_at`) VALUES
(1, 301, 4500, 'Paid', '2023-07-17 22:09:35', '2023-07-17 22:09:35'),
(3, 303, 6500, 'Paid', '2023-07-17 22:09:35', '2023-07-17 18:56:59'),
(4, 304, 3200, 'Paid', '2023-07-17 22:09:35', '2023-07-17 22:09:35'),
(6, 306, 2456, 'pending', '2023-07-17 19:08:55', '2023-07-17 19:08:55');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `address` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`id`, `user_id`, `phone`, `address`, `created_at`, `updated_at`) VALUES
(1, 5, 3453637531, 'Korangi DHA', '2023-07-17 08:54:19', '2023-07-17 06:08:47'),
(2, 5, 9876543210, '456 Elm Avenue', '2023-07-17 08:54:19', '2023-07-17 06:06:51'),
(3, 7, 5555555555, '789 Oak ', '2023-07-17 08:54:19', '2023-07-17 17:53:19'),
(4, 5, 1111111111, '321 Pine Lane, Hamlet', '2023-07-17 08:54:19', '2023-07-17 08:54:19'),
(8, 7, 3527846824, 'DHA MAlir', '2023-07-17 14:14:39', '2023-07-17 14:14:39'),
(12, 7, 3527846824, 'DHA MAlir', '2023-07-17 14:19:03', '2023-07-17 14:19:03'),
(13, 7, 3527846824, 'DHA MAlir', '2023-07-17 14:20:59', '2023-07-17 14:20:59'),
(14, 7, 3527846824, 'DHA MAlir', '2023-07-17 14:21:54', '2023-07-17 14:21:54'),
(28, 7, 3527846824, 'DHA SEA VIew', '2023-07-17 14:39:58', '2023-07-17 14:39:58'),
(29, 7, 3527846824, 'DHA SEA VIew Side', '2023-07-17 14:40:14', '2023-07-17 14:40:14'),
(32, 6, 3527846824, 'Karachi', '2023-07-17 14:41:45', '2023-07-17 14:41:45'),
(33, 6, 3527846824, 'Hussainabad', '2023-07-17 14:42:01', '2023-07-17 14:42:01'),
(34, 6, 3527846824, 'Hussainabad', '2023-07-17 14:46:19', '2023-07-17 14:46:19'),
(35, 6, 3527846824, 'Karachi', '2023-07-17 14:47:03', '2023-07-17 14:47:03'),
(36, 7, 3527846824, 'DHA MAlir', '2023-07-17 14:52:30', '2023-07-17 14:52:30');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `category` varchar(255) NOT NULL,
  `salary` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`id`, `user_id`, `category`, `salary`, `created_at`, `updated_at`) VALUES
(4, 204, 'Accountant', 55000, '2023-07-17 20:44:05', '2023-07-17 20:44:05'),
(6, 7, 'waiter', 25000, '2023-07-17 17:35:16', '2023-07-17 17:35:16'),
(7, 201, 'chef', 25000, '2023-07-17 18:03:54', '2023-07-17 18:03:54');

-- --------------------------------------------------------

--
-- Table structure for table `menu`
--

CREATE TABLE `menu` (
  `id` int(11) NOT NULL,
  `item_name` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `description` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `menu`
--

INSERT INTO `menu` (`id`, `item_name`, `price`, `description`, `created_at`, `updated_at`) VALUES
(3, 'Veggie Burger', '7.49', 'Plant-based patty with fresh veggies and vegan mayo.', '2023-07-16 08:03:19', '2023-07-16 08:03:19'),
(4, 'Spicy Chicken Burger', '8.75', 'Crispy chicken fillet with spicy sauce and coleslaw.', '2023-07-16 08:03:19', '2023-07-16 08:03:19'),
(5, 'Mushroom Swiss', '10.20', 'Beef patty topped with sautéed mushrooms and Swiss cheese.', '2023-07-16 08:03:19', '2023-07-16 16:29:43'),
(8, 'Double Cheeseburger', '12.99', 'Two beef patties with double cheese and all the fixings.', '2023-07-16 08:03:19', '2023-07-16 08:03:19'),
(9, 'Hawaiian Teriyaki Burger', '10.75', 'Grilled pineapple, teriyaki sauce, and ham on a beef patty.', '2023-07-16 08:03:19', '2023-07-16 08:03:19'),
(10, 'Zinger burger', '8.80', 'hello', '2023-07-16 08:03:19', '2023-07-16 16:26:36'),
(13, 'Double Zinger', '8.99', 'very baad', '2023-07-16 14:55:31', '2023-07-17 13:31:17'),
(15, 'Veggie Burger', '7.00', 'Plant-based patty with fresh veggies and vegan mayo.', '2023-07-16 15:48:49', '2023-07-16 15:48:49'),
(16, 'Veggie Burger', '7.00', 'Plant-based patty with fresh veggies and vegan mayo.', '2023-07-16 15:51:10', '2023-07-16 15:51:10'),
(17, 'Veggie Burger', '7.00', 'Plant-based patty with fresh veggies and vegan mayo.', '2023-07-16 15:51:16', '2023-07-16 15:51:16'),
(18, 'Veggie Burger', '7.00', 'Plant-based patty with fresh veggies and vegan mayo.', '2023-07-16 15:52:58', '2023-07-16 15:52:58'),
(19, 'Double Zinger', '8.99', 'normal', '2023-07-17 05:02:03', '2023-07-17 06:48:08'),
(22, 'Veggie Burger', '12.90', 'Plant-based patty with fresh veggies and vegan mayo.', '2023-07-17 13:31:32', '2023-07-17 13:31:32'),
(23, 'Veggie Burger', '12.90', 'Plant-based patty with fresh veggies and vegan mayo.', '2023-07-17 14:02:44', '2023-07-17 14:02:44');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `id` int(11) NOT NULL,
  `emp_id` int(11) NOT NULL,
  `cust_id` int(11) NOT NULL,
  `order_date` date NOT NULL,
  `order_item` varchar(255) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `description` varchar(255) NOT NULL,
  `order_status` varchar(50) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`id`, `emp_id`, `cust_id`, `order_date`, `order_item`, `quantity`, `price`, `description`, `order_status`, `created_at`, `updated_at`) VALUES
(1, 401, 201, '2023-05-10', 'Classic Burger', 2, 18, 'No pickles, extra cheese', 'Pending', '2023-07-18 11:51:11', '2023-07-18 11:52:02'),
(2, 4, 2000, '2023-08-18', 'ZInger', 3, 45, 'no ketup', 'pending', '2023-07-18 11:51:11', '2023-07-18 11:48:37'),
(3, 403, 203, '2023-07-18', 'Veggie Burger', 1, 7, 'No onions', 'Delivered', '2023-07-18 11:51:11', '2023-07-18 11:49:38'),
(4, 404, 201, '2023-07-15', 'Spicy Chicken Burger', 1, 9, 'Extra spicy', 'Delivered', '2023-07-18 11:51:11', '2023-07-18 11:51:11'),
(6, 4, 2000, '2023-08-18', 'ZInger', 3, 45, 'no ketup', 'pending', '2023-07-18 12:19:34', '2023-07-18 12:19:34'),
(7, 12, 45, '2023-08-23', 'Double ANde Wala Burger', 3, 8, 'no ketchup', 'Delivered', '2023-07-18 12:28:02', '2023-07-18 12:28:02'),
(8, 12, 45, '2023-08-23', 'Double ANde Wala Burger', 3, 8, 'no ketchup', 'Delivered', '2023-07-18 12:28:02', '2023-07-18 12:28:02'),
(9, 12, 34, '2023-08-22', 'Double ANde Wala Burger', 3, 8, 'Plant-based patty with fresh veggies and vegan mayo.', 'Delivered', '2023-07-18 12:28:39', '2023-07-18 12:28:39');

-- --------------------------------------------------------

--
-- Table structure for table `stock`
--

CREATE TABLE `stock` (
  `id` int(11) NOT NULL,
  `menu_item` varchar(255) NOT NULL,
  `quantity` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `stock`
--

INSERT INTO `stock` (`id`, `menu_item`, `quantity`, `created_at`, `updated_at`) VALUES
(2, 'Cheeseburger Deluxe', 85, '2023-07-18 16:33:00', '2023-07-18 13:14:35'),
(4, 'Spicy Chicken Burger', 70, '2023-07-18 16:33:00', '2023-07-18 16:33:00'),
(5, 'Mushroom Swiss Burger', 60, '2023-07-18 16:33:00', '2023-07-18 16:33:00'),
(6, 'BBQ Bacon Burger', 90, '2023-07-18 16:33:00', '2023-07-18 16:33:00'),
(8, 'Double Cheeseburger', 75, '2023-07-18 16:33:00', '2023-07-18 16:33:00'),
(9, 'Hawaiian Teriyaki Burger', 40, '2023-07-18 16:33:00', '2023-07-18 16:33:00'),
(10, 'Jalapeno Popper Burger', 55, '2023-07-18 16:33:00', '2023-07-18 16:33:00'),
(11, 'ketup', 30, '2023-07-18 13:25:41', '2023-07-18 13:25:41');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `role` enum('customer','employee') NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `role`, `created_at`, `updated_at`) VALUES
(3, 'Michael Johnson', 'customer', '2023-07-16 22:14:48', '2023-07-17 04:35:38'),
(4, 'Emily Davis', 'customer', '2023-07-16 22:14:48', '2023-07-16 22:14:48'),
(5, 'Robert Lee', 'employee', '2023-07-16 22:14:48', '2023-07-16 22:14:48'),
(7, 'Abbas Rizvi', 'employee', '2023-07-17 04:47:14', '2023-07-17 04:47:14');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bill`
--
ALTER TABLE `bill`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `stock`
--
ALTER TABLE `stock`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bill`
--
ALTER TABLE `bill`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `menu`
--
ALTER TABLE `menu`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `stock`
--
ALTER TABLE `stock`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
