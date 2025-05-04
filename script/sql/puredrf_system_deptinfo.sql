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
-- Table structure for table `system_deptinfo`
--

DROP TABLE IF EXISTS `system_deptinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_deptinfo` (
  `id` char(32) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `name` varchar(128) NOT NULL,
  `code` varchar(128) NOT NULL,
  `rank` int NOT NULL,
  `auto_bind` tinyint(1) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `parent_id` char(32) DEFAULT NULL,
  `type` smallint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`),
  KEY `system_deptinfo_parent_id_86e73520_fk_system_deptinfo_id` (`parent_id`),
  CONSTRAINT `system_deptinfo_parent_id_86e73520_fk_system_deptinfo_id` FOREIGN KEY (`parent_id`) REFERENCES `system_deptinfo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_deptinfo`
--

LOCK TABLES `system_deptinfo` WRITE;
/*!40000 ALTER TABLE `system_deptinfo` DISABLE KEYS */;
INSERT INTO `system_deptinfo` VALUES ('4c76aef77c654505a614e7b2b2c5b2af','2024-09-08 15:16:41.289000','2024-10-25 02:56:44.534000','管理部门','management',0,0,1,'9975ede0ab2a488b9464e7ac7823e7d5',3),('87bf3be7d0484121a5926d50c985008a','2024-11-10 07:43:45.728500','2024-11-27 09:56:33.513223','游客','anonymous',2,0,1,NULL,4),('9975ede0ab2a488b9464e7ac7823e7d5','2024-09-08 15:15:30.860000','2024-10-25 02:55:36.454000','总部','base',0,0,1,NULL,1);
/*!40000 ALTER TABLE `system_deptinfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-02 13:45:46
