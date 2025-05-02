-- MySQL dump 10.13  Distrib 8.0.40, for macos14 (arm64)
--
-- Host: 47.243.254.174    Database: puredrf
-- ------------------------------------------------------
-- Server version	8.0.41-0ubuntu0.22.04.1

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
-- Table structure for table `monitor_loginlog`
--

DROP TABLE IF EXISTS `monitor_loginlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `monitor_loginlog` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `username` varchar(32) DEFAULT NULL,
  `ip` varchar(32) DEFAULT NULL,
  `agent` varchar(1500) DEFAULT NULL,
  `browser` varchar(200) DEFAULT NULL,
  `os` varchar(150) DEFAULT NULL,
  `login_type` int NOT NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=169 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monitor_loginlog`
--

LOCK TABLES `monitor_loginlog` WRITE;
/*!40000 ALTER TABLE `monitor_loginlog` DISABLE KEYS */;
INSERT INTO `monitor_loginlog` VALUES (163,'2025-05-01 12:54:35.293087','2025-05-01 12:54:35.293131','admin','111.18.3.59','PC / Mac OS X 10.15.7 / Chrome 135.0.0','Chrome 135.0.0','Mac OS X 10.15.7',1,1),(164,'2025-05-01 13:16:14.356000','2025-05-01 13:16:14.356037','admin','111.18.3.59','PC / Mac OS X 10.15.7 / Chrome 135.0.0','Chrome 135.0.0','Mac OS X 10.15.7',1,1),(165,'2025-05-01 13:17:23.726221','2025-05-01 13:17:23.726267','admin','111.18.3.59','PC / Mac OS X 10.15.7 / Chrome 135.0.0','Chrome 135.0.0','Mac OS X 10.15.7',1,1),(166,'2025-05-01 13:50:52.331635','2025-05-01 13:50:52.331672','admin','111.18.3.59','PC / Mac OS X 10.15.7 / Chrome 135.0.0','Chrome 135.0.0','Mac OS X 10.15.7',1,1),(167,'2025-05-01 13:53:36.869877','2025-05-01 13:53:36.869914','admin','111.18.3.59','PC / Mac OS X 10.15.7 / Chrome 135.0.0','Chrome 135.0.0','Mac OS X 10.15.7',1,1),(168,'2025-05-02 05:44:08.921938','2025-05-02 05:44:08.921995','admin','111.19.33.175','PC / Mac OS X 10.15.7 / Chrome 135.0.0','Chrome 135.0.0','Mac OS X 10.15.7',1,1);
/*!40000 ALTER TABLE `monitor_loginlog` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-02 13:45:48
