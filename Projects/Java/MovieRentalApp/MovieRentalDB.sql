-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: movierentaldb
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `movies`
--

DROP TABLE IF EXISTS `movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movies` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `genre` varchar(50) DEFAULT NULL,
  `price_per_day` decimal(5,2) DEFAULT NULL,
  `poster_path` varchar(255) DEFAULT NULL,
  `director` varchar(100) DEFAULT NULL,
  `writers` varchar(255) DEFAULT NULL,
  `release_date` date DEFAULT NULL,
  `duration` varchar(50) DEFAULT NULL,
  `rating` varchar(10) DEFAULT NULL,
  `cast` text,
  `dvd_units` int DEFAULT '0',
  `blu_ray_units` int DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies`
--

LOCK TABLES `movies` WRITE;
/*!40000 ALTER TABLE `movies` DISABLE KEYS */;
INSERT INTO `movies` VALUES (1,'Interstellar','Sci-Fi',3.99,'poster_Interstellar.jpg','Christopher Nolan','Christopher Nolan, Jonathan Nolan','2014-11-07','2h 49m','PG-13','Matthew McConaughey, Anne Hathaway, Jessica Chastain',0,4),(2,'Gantz:O','Sci-Fi',3.99,'poster_GantzO.jpg','Yusushi Kawamura','Hiroya Oku, Tsutomu Kuroiwa','2016-10-14','1h 35m','NC-17','Daisuke Ono, Mao Ichimichi, Tomohiro Kaku, Saori Hayami, Shushi Ikeda',6,5),(4,'Suzume','Fantasy',6.99,'poster_Suzume.jpg','Makoto Shinkai','Makoto Shinkai','2023-01-14','2h 2m','PG-13','Nanoka Hara, Hokuto Matsumura, Eri Fukatsu',5,5),(5,'Bullet Train','Action',5.99,'poster_BulletTrain.jpeg','David Leitch','Zak Olkewicz, Kotaro Isaka','2022-08-05','2h 7m','R','Brad Pitt, Joey King, Aaron Taylor-Johnson',5,5),(11,'Inu-Oh','Fantasy',6.99,'poster_Inu-Oh.jpg','Masaaki Yuasa','Hideo Furukawa, Akiko Nogi','2022-08-12','1h 38m','PG-13','Avu-chan, Mirai Moriyama, Tasuku Emoto',5,5);
/*!40000 ALTER TABLE `movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rentals`
--

DROP TABLE IF EXISTS `rentals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rentals` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `movie_id` int DEFAULT NULL,
  `customer_id` int DEFAULT NULL,
  `rent_date` date DEFAULT NULL,
  `return_date` date DEFAULT NULL,
  `additional_fees` decimal(5,2) DEFAULT NULL,
  `total_cost` decimal(10,2) DEFAULT NULL,
  `format` varchar(20) DEFAULT NULL,
  `price_per_day` decimal(5,2) DEFAULT NULL,
  `status` varchar(20) DEFAULT 'Normal',
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `movie_id` (`movie_id`),
  CONSTRAINT `rentals_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `rentals_ibfk_2` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rentals`
--

LOCK TABLES `rentals` WRITE;
/*!40000 ALTER TABLE `rentals` DISABLE KEYS */;
INSERT INTO `rentals` VALUES (1,NULL,5,5,'2025-04-22','2025-04-23',NULL,17.97,'DVD',5.99,'Returned'),(2,NULL,11,8,'2025-04-22','2025-04-23',NULL,20.97,'BLU-RAY',6.99,'Returned'),(3,NULL,4,2,'2025-04-22','2025-04-25',NULL,20.97,'DVD',6.99,'Normal'),(4,NULL,2,10,'2025-04-22','2025-04-24',NULL,11.97,'DVD',3.99,'Returned'),(5,NULL,2,10,'2025-04-22','2025-04-24',NULL,11.97,'DVD',3.99,'Returned'),(6,NULL,2,10,'2025-04-22','2025-04-24',NULL,11.97,'DVD',3.99,'Returned'),(7,NULL,2,10,'2025-04-22','2025-04-24',NULL,11.97,'BLU-RAY',3.99,'Returned'),(8,NULL,5,5,'2025-04-23','2025-04-23',NULL,17.97,'DVD',5.99,'Returned'),(9,NULL,5,5,'2025-04-23','2025-04-26',NULL,17.97,'DVD',5.99,'Normal'),(11,NULL,5,2,'2025-04-24','2025-04-24',NULL,17.97,'DVD',5.99,'Returned'),(12,NULL,5,2,'2025-04-24','2025-04-24',NULL,17.97,'DVD',5.99,'Returned'),(13,NULL,2,2,'2025-04-24','2025-04-24',NULL,11.97,'DVD',3.99,'Returned'),(14,NULL,1,2,'2025-04-24','2025-04-27',NULL,11.97,'DVD',3.99,'Normal'),(15,NULL,2,2,'2025-04-24','2025-04-24',NULL,11.97,'DVD',3.99,'Returned'),(16,NULL,2,2,'2025-04-24','2025-04-24',NULL,11.97,'DVD',3.99,'Returned'),(17,NULL,2,2,'2025-04-24','2025-04-24',NULL,11.97,'DVD',3.99,'Returned'),(18,NULL,2,2,'2025-04-24','2025-04-24',NULL,11.97,'DVD',3.99,'Returned'),(19,NULL,2,2,'2025-04-24','2025-04-24',NULL,11.97,'DVD',3.99,'Returned'),(20,NULL,2,2,'2025-04-24','2025-04-27',NULL,11.97,'DVD',3.99,'Normal'),(21,NULL,1,2,'2025-04-24','2025-04-27',NULL,11.97,'BLU-RAY',3.99,'Normal');
/*!40000 ALTER TABLE `rentals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservations`
--

DROP TABLE IF EXISTS `reservations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `movie_id` int DEFAULT NULL,
  `reservation_date` date DEFAULT NULL,
  `format` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `movie_id` (`movie_id`),
  CONSTRAINT `reservations_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `reservations_ibfk_2` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservations`
--

LOCK TABLES `reservations` WRITE;
/*!40000 ALTER TABLE `reservations` DISABLE KEYS */;
INSERT INTO `reservations` VALUES (1,1,2,'2025-04-18','BLU-RAY'),(2,1,2,'2025-04-18','DVD'),(4,2,5,'2025-04-18','DVD'),(5,2,2,'2025-04-18','BLU-RAY'),(6,2,1,'2025-04-18','DVD'),(7,2,2,'2025-04-18','BLU-RAY'),(8,2,2,'2025-04-18','DVD'),(14,2,5,'2025-05-08','DVD');
/*!40000 ALTER TABLE `reservations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(100) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `middle_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `role` varchar(20) DEFAULT 'client',
  `address` varchar(255) DEFAULT NULL,
  `zip_code` varchar(10) DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'test01','Hector','R','Ramirez','Brooklyn','1992-12-12','tester','client',NULL,NULL,NULL),(2,'test','Hector','M','Rios','Brooklyn','1992-12-12','test','client',NULL,NULL,NULL),(5,'rusty','Maria','Del Carmen','Rios','Arecibo','1992-12-12','mrios','client','128 Sector Monroig','11213','7547796276'),(6,NULL,'Marlo','','Verte','Arecibo','1992-12-12',NULL,'client','Avenida Caracoles 8','00616',''),(7,NULL,'Jesus','M','Delgado','Brooklyn','1992-12-12',NULL,'client','1280 Atlantic Ave','11213','5646658959'),(8,NULL,'Jerry','S','Cope','Brooklyn','1992-12-12',NULL,'client','123 Atlantic','11213','6468947988'),(9,NULL,'Maria','L','Marte','Brooklyn','1992-12-12',NULL,'client','133 Burough','11213','4658549989'),(10,NULL,'Dereck','','Dole','Brooklyn','1992-12-12',NULL,'client','123 Atlantic','11213','4549781236'),(11,NULL,'Eric','M','Adams','Brooklyn','1992-12-12',NULL,'client','335 Erlo St Apt 2','11213','6468975468'),(13,'admin','Admin','','','','1992-12-12','admin','admin','','','');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-08 22:06:52
