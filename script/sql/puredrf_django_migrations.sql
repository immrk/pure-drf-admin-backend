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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'system','0001_initial','2024-11-01 04:04:16.828993'),(2,'contenttypes','0001_initial','2024-11-01 04:04:17.087552'),(3,'contenttypes','0002_remove_content_type_name','2024-11-01 04:04:17.653078'),(4,'auth','0001_initial','2024-11-01 04:04:18.912671'),(5,'auth','0002_alter_permission_name_max_length','2024-11-01 04:04:19.133916'),(6,'auth','0003_alter_user_email_max_length','2024-11-01 04:04:19.200496'),(7,'auth','0004_alter_user_username_opts','2024-11-01 04:04:19.345261'),(8,'auth','0005_alter_user_last_login_null','2024-11-01 04:04:19.461649'),(9,'auth','0006_require_contenttypes_0002','2024-11-01 04:04:19.528264'),(10,'auth','0007_alter_validators_add_error_messages','2024-11-01 04:04:19.619754'),(11,'auth','0008_alter_user_username_max_length','2024-11-01 04:04:19.723551'),(12,'auth','0009_alter_user_last_name_max_length','2024-11-01 04:04:19.819717'),(13,'auth','0010_alter_group_name_max_length','2024-11-01 04:04:20.048319'),(14,'auth','0011_update_proxy_permissions','2024-11-01 04:04:20.419600'),(15,'auth','0012_alter_user_first_name_max_length','2024-11-01 04:04:20.512517'),(16,'user','0001_initial','2024-11-01 04:04:23.006694'),(17,'admin','0001_initial','2024-11-01 04:04:23.726432'),(18,'admin','0002_logentry_remove_auto_add','2024-11-01 04:04:23.802741'),(19,'admin','0003_logentry_add_action_flag_choices','2024-11-01 04:04:23.944013'),(20,'monitor','0001_initial','2024-11-01 04:04:24.269070'),(21,'monitor','0002_loginlog_status','2024-11-01 04:04:24.544996'),(22,'monitor','0003_operationlog_creator','2024-11-01 04:04:25.000405'),(23,'monitor','0004_alter_operationlog_json_result_and_more','2024-11-01 04:04:25.388649'),(24,'sessions','0001_initial','2024-11-01 04:04:25.723918'),(25,'system','0002_role_parent','2024-11-01 04:04:26.079785'),(26,'system','0003_deptinfo_type_alter_role_menu','2024-11-01 04:04:26.409858'),(27,'system','0004_rename_is_active_deptinfo_status_and_more','2024-11-01 04:04:26.838440'),(28,'system','0005_alter_menu_name_alter_menu_path','2024-11-01 04:04:27.078304'),(29,'system','0006_alter_menu_meta','2024-11-01 04:04:28.042114'),(30,'system','0007_alter_menu_name','2024-11-01 04:04:28.755320'),(31,'system','0008_menu_code','2024-11-01 04:04:28.998388'),(32,'system','0009_remove_menu_rank_menumeta_rank_alter_menu_name','2024-11-01 04:04:29.414725'),(33,'system','0010_menu_redirect','2024-11-01 04:04:29.588492'),(34,'system','0011_alter_deptinfo_options_alter_menu_options','2024-11-01 04:04:29.679766'),(35,'user','0002_user_create_time','2024-11-01 04:04:29.981649'),(36,'user','0003_rename_is_active_user_status','2024-11-01 04:04:30.196383'),(37,'user','0004_alter_user_options','2024-11-01 04:04:30.271015');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-02 13:45:58
