-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 19, 2023 at 08:02 AM
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
  `payment_status` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bill`
--

INSERT INTO `bill` (`id`, `order_id`, `total_amount`, `payment_status`, `created_at`, `updated_at`) VALUES
(6, 11, 22, 'Paid', '2023-07-19 05:36:09', '2023-07-19 05:36:09'),
(7, 12, 13, 'Paid', '2023-07-19 05:36:09', '2023-07-19 05:36:09'),
(8, 13, 10, 'Pending', '2023-07-19 05:36:09', '2023-07-19 05:36:09'),
(9, 14, 23, 'Pending', '2023-07-19 05:36:09', '2023-07-19 05:36:09'),
(10, 15, 12, 'Paid', '2023-07-19 05:36:09', '2023-07-19 05:36:09'),
(11, 16, 22, 'pending', '2023-07-19 01:53:18', '2023-07-19 01:53:18');

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
(1, 1, 1234567890, '123 Main Street, City', '2023-07-19 05:23:03', '2023-07-19 05:23:03'),
(2, 2, 9876543210, '456 Elm Avenue, Town', '2023-07-19 05:23:03', '2023-07-19 05:23:03'),
(3, 4, 1111111111, '789 Oak Lane, Village', '2023-07-19 05:23:03', '2023-07-19 05:23:03'),
(4, 6, 5555555555, '101 Maple Road, Suburb', '2023-07-19 05:23:03', '2023-07-19 05:23:03'),
(5, 8, 7777777777, '303 Cedar Street, Countryside', '2023-07-19 05:23:03', '2023-07-19 05:23:03');

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
(1, 3, 'Manager', 60000, '2023-07-19 05:25:04', '2023-07-19 05:25:04'),
(2, 5, 'Waiter', 30000, '2023-07-19 05:25:04', '2023-07-19 05:25:04'),
(3, 7, 'Waiter', 35000, '2023-07-19 05:25:04', '2023-07-19 05:25:04');

-- --------------------------------------------------------

--
-- Table structure for table `menu`
--

CREATE TABLE `menu` (
  `id` int(11) NOT NULL,
  `item_name` varchar(255) NOT NULL,
  `price` float NOT NULL,
  `description` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `menu`
--

INSERT INTO `menu` (`id`, `item_name`, `price`, `description`, `created_at`, `updated_at`) VALUES
(1, 'Classic Burger', 11, 'Juicy beef patty with lettuce, tomato, and pickles on a toasted bun.', '2023-07-19 05:25:58', '2023-07-19 01:49:09'),
(2, 'Cheeseburger Deluxe', 12.99, 'Classic burger with melted cheese, bacon, and special sauce.', '2023-07-19 05:25:58', '2023-07-19 05:25:58'),
(3, 'Veggie Burger', 9.99, 'Delicious plant-based patty with fresh veggies and vegan mayo.', '2023-07-19 05:25:58', '2023-07-19 05:25:58'),
(4, 'Spicy Chicken Burger', 11.49, 'Crispy chicken fillet with spicy mayo and lettuce.', '2023-07-19 05:25:58', '2023-07-19 05:25:58'),
(5, 'Mushroom Swiss Burger', 11.99, 'Beef patty topped with sautéed mushrooms and Swiss cheese.', '2023-07-19 05:25:58', '2023-07-19 05:25:58'),
(6, 'BBQ Bacon Burger', 12.49, 'Tasty burger with smoky BBQ sauce and crispy bacon.', '2023-07-19 05:25:58', '2023-07-19 05:25:58'),
(7, 'California Burger', 12.99, 'Avocado, sprouts, and chipotle mayo on a juicy beef patty.', '2023-07-19 05:25:58', '2023-07-19 05:25:58'),
(8, 'Double Cheeseburger', 14.99, 'Two beef patties, double cheese, and all the fixings.', '2023-07-19 05:25:58', '2023-07-19 05:25:58'),
(9, 'Hawaiian Teriyaki Burger', 13.49, 'Grilled pineapple, teriyaki sauce, and grilled chicken.', '2023-07-19 05:25:58', '2023-07-19 05:25:58'),
(10, 'Jalapeno Popper Burger', 13.49, 'Cream cheese, jalapenos, and crispy onion rings on a beef patty.', '2023-07-19 05:25:58', '2023-07-19 05:25:58');

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
  `price` float NOT NULL,
  `description` varchar(255) NOT NULL,
  `order_status` varchar(50) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`id`, `emp_id`, `cust_id`, `order_date`, `order_item`, `quantity`, `price`, `description`, `order_status`, `created_at`, `updated_at`) VALUES
(11, 3, 1, '2023-07-19', 'Classic Burger', 2, 10.99, 'Two Classic Burgers', 'Completed', '2023-07-19 05:31:15', '2023-07-19 05:31:15'),
(12, 2, 2, '2023-07-19', 'Cheeseburger Deluxe', 1, 12.99, 'One Cheeseburger Deluxe', 'Completed', '2023-07-19 05:31:15', '2023-07-19 05:31:15'),
(13, 3, 4, '2023-07-19', 'Veggie Burger', 1, 9.99, 'One Veggie Burger', 'In Progress', '2023-07-19 05:31:15', '2023-07-19 05:31:15'),
(14, 3, 3, '2023-07-19', 'Spicy Chicken Burger', 2, 11.49, 'Two Spicy Chicken Burgers', 'In Progress', '2023-07-19 05:31:15', '2023-07-19 05:31:15'),
(15, 2, 5, '2023-07-19', 'Mushroom Swiss Burger', 1, 11.99, 'One Mushroom Swiss Burger', 'Completed', '2023-07-19 05:31:15', '2023-07-19 05:31:15'),
(16, 2, 3, '2023-06-15', 'Classic Burger', 2, 11, 'no ketchup', 'Delivered', '2023-07-19 01:52:47', '2023-07-19 01:52:47');

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
(1, 'Ketchup', 100, '2023-07-19 05:38:13', '2023-07-19 05:38:13'),
(2, 'Chicken', 80, '2023-07-19 05:38:13', '2023-07-19 05:38:13'),
(3, 'Bun', 150, '2023-07-19 05:38:13', '2023-07-19 05:38:13'),
(4, 'Salad', 120, '2023-07-19 05:38:13', '2023-07-19 05:38:13'),
(5, 'Mayonnaise', 200, '2023-07-19 05:38:13', '2023-07-19 05:38:13');

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
(1, 'Sarah Johnson', 'customer', '2023-07-19 05:21:56', '2023-07-19 05:21:56'),
(2, 'David Williams', 'customer', '2023-07-19 05:21:56', '2023-07-19 05:21:56'),
(3, 'Emma Brown', 'employee', '2023-07-19 05:21:56', '2023-07-19 05:21:56'),
(4, 'James Miller', 'customer', '2023-07-19 05:21:56', '2023-07-19 05:21:56'),
(5, 'Olivia Taylor', 'employee', '2023-07-19 05:21:56', '2023-07-19 05:21:56'),
(6, 'Sophia Wilson', 'customer', '2023-07-19 05:21:56', '2023-07-19 05:21:56'),
(7, 'William Anderson', 'employee', '2023-07-19 05:21:56', '2023-07-19 05:21:56'),
(8, 'Ava Martinez', 'customer', '2023-07-19 05:21:56', '2023-07-19 05:21:56');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bill`
--
ALTER TABLE `bill`
  ADD PRIMARY KEY (`id`),
  ADD KEY `order_id` (`order_id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`),
  ADD KEY `emp_id` (`emp_id`),
  ADD KEY `cust_id` (`cust_id`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `menu`
--
ALTER TABLE `menu`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `stock`
--
ALTER TABLE `stock`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bill`
--
ALTER TABLE `bill`
  ADD CONSTRAINT `bill_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`);

--
-- Constraints for table `customer`
--
ALTER TABLE `customer`
  ADD CONSTRAINT `customer_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `employee`
--
ALTER TABLE `employee`
  ADD CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `employee` (`id`),
  ADD CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`cust_id`) REFERENCES `customer` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
