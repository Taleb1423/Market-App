-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: db_pro
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `custumer`
--

DROP TABLE IF EXISTS `custumer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `custumer` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `adress` varchar(45) NOT NULL,
  `phone` int NOT NULL,
  `date_of_birth` date NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `custumer`
--

LOCK TABLES `custumer` WRITE;
/*!40000 ALTER TABLE `custumer` DISABLE KEYS */;
INSERT INTO `custumer` VALUES (6,'souheilmoussa','souh','asdfghjkl','souheil2.moussa@gmail.com','asdf',123456,'0033-11-22');
/*!40000 ALTER TABLE `custumer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `online_info`
--

DROP TABLE IF EXISTS `online_info`;
/*!50001 DROP VIEW IF EXISTS `online_info`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `online_info` AS SELECT 
 1 AS `product_name`,
 1 AS `qty`,
 1 AS `sell_price`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order` (
  `order_id` int NOT NULL,
  `delivery_status` varchar(10) NOT NULL,
  `time_and_date_placed` datetime NOT NULL,
  `time_and_date_delivered` datetime NOT NULL,
  `ord_user_id` int NOT NULL,
  `ord_staff_id` int NOT NULL,
  `order_price` int NOT NULL,
  `delivery_price` int NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `ord_staff_id_idx` (`ord_staff_id`),
  KEY `ord_user_id_idx` (`ord_user_id`),
  CONSTRAINT `ord_staff_id` FOREIGN KEY (`ord_staff_id`) REFERENCES `staff` (`staff_id`),
  CONSTRAINT `ord_user_id` FOREIGN KEY (`ord_user_id`) REFERENCES `custumer` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `product_name` varchar(45) NOT NULL,
  `product_type` varchar(45) NOT NULL,
  `sell_price` int NOT NULL,
  `buy_price` int NOT NULL,
  `amount_in_stock` int NOT NULL,
  PRIMARY KEY (`product_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES ('test1','elect',650,600,9),('test2','elect',50,20,8),('test3','elect',7780,400,8);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shipment`
--

DROP TABLE IF EXISTS `shipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shipment` (
  `shipment_id` int NOT NULL AUTO_INCREMENT,
  `date_ordered` date NOT NULL,
  `staff_id` int NOT NULL,
  `shipment_price` int NOT NULL,
  `shipment_suplier` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`shipment_id`),
  KEY `staff_id_idx` (`staff_id`),
  KEY `supplier_name_idx` (`shipment_suplier`),
  CONSTRAINT `staff_id` FOREIGN KEY (`staff_id`) REFERENCES `staff` (`staff_id`),
  CONSTRAINT `supplier_name` FOREIGN KEY (`shipment_suplier`) REFERENCES `suplier` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shipment`
--

LOCK TABLES `shipment` WRITE;
/*!40000 ALTER TABLE `shipment` DISABLE KEYS */;
INSERT INTO `shipment` VALUES (3,'2022-12-17',1,3000,'intel');
/*!40000 ALTER TABLE `shipment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff` (
  `staff_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `phone` int NOT NULL,
  `adress` varchar(45) NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `role` varchar(45) NOT NULL,
  `salary` int NOT NULL,
  `number_of_orders` int DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES (1,'souheil','souheils','123456','s.m@gmail.com',123456,'wsft',NULL,'2022-12-17','0000-00-00','admin',5600,NULL);
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suplier`
--

DROP TABLE IF EXISTS `suplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suplier` (
  `name` varchar(45) NOT NULL,
  `email` varchar(45) DEFAULT NULL,
  `adress` varchar(45) NOT NULL,
  `phone` int NOT NULL,
  PRIMARY KEY (`name`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suplier`
--

LOCK TABLES `suplier` WRITE;
/*!40000 ALTER TABLE `suplier` DISABLE KEYS */;
INSERT INTO `suplier` VALUES ('intel','in.tel@gmail.com','ab,ba',11122244);
/*!40000 ALTER TABLE `suplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unit`
--

DROP TABLE IF EXISTS `unit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `unit` (
  `serial_number` int NOT NULL AUTO_INCREMENT,
  `production_date` date DEFAULT NULL,
  `unit_order_id` int DEFAULT NULL,
  `unit_product_name` varchar(45) DEFAULT NULL,
  `unit_shippment` int DEFAULT NULL,
  PRIMARY KEY (`serial_number`),
  KEY `unit_order_id_idx` (`unit_order_id`),
  KEY `unit_product_name` (`unit_product_name`),
  KEY `unit_shipment_idx` (`unit_shippment`),
  CONSTRAINT `unit_ibfk_1` FOREIGN KEY (`unit_product_name`) REFERENCES `product` (`product_name`),
  CONSTRAINT `unit_order_id` FOREIGN KEY (`unit_order_id`) REFERENCES `order` (`order_id`),
  CONSTRAINT `unit_shipment` FOREIGN KEY (`unit_shippment`) REFERENCES `shipment` (`shipment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=410 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unit`
--

LOCK TABLES `unit` WRITE;
/*!40000 ALTER TABLE `unit` DISABLE KEYS */;
INSERT INTO `unit` VALUES (19,NULL,NULL,'test3',NULL),(123,NULL,NULL,'test2',NULL),(167,NULL,NULL,'test2',NULL),(189,NULL,NULL,'test2',NULL),(400,NULL,NULL,'test1',NULL),(403,NULL,NULL,'test1',NULL),(404,NULL,NULL,'test1',NULL),(405,NULL,NULL,'test1',NULL),(406,NULL,NULL,'test1',NULL),(407,NULL,NULL,'test1',NULL),(408,NULL,NULL,'test1',NULL),(409,NULL,NULL,'test1',NULL);
/*!40000 ALTER TABLE `unit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `online_info`
--

/*!50001 DROP VIEW IF EXISTS `online_info`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `online_info` AS select `p`.`product_name` AS `product_name`,count(`u`.`serial_number`) AS `qty`,`p`.`sell_price` AS `sell_price` from (`product` `p` join `unit` `u`) where (`p`.`product_name` = `u`.`unit_product_name`) group by `p`.`product_name` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-19  1:27:25
