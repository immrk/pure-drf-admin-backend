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
-- Table structure for table `system_menu`
--

DROP TABLE IF EXISTS `system_menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_menu` (
  `id` char(32) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `menu_type` smallint NOT NULL,
  `name` varchar(128) NOT NULL,
  `path` varchar(255) DEFAULT NULL,
  `component` varchar(255) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `method` varchar(10) DEFAULT NULL,
  `meta_id` char(32) DEFAULT NULL,
  `parent_id` char(32) DEFAULT NULL,
  `code` varchar(128) DEFAULT NULL,
  `redirect` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `meta_id` (`meta_id`),
  UNIQUE KEY `code` (`code`),
  KEY `system_menu_parent_id_c715739f_fk_system_menu_id` (`parent_id`),
  CONSTRAINT `system_menu_meta_id_3c0f37de_fk_system_menumeta_id` FOREIGN KEY (`meta_id`) REFERENCES `system_menumeta` (`id`),
  CONSTRAINT `system_menu_parent_id_c715739f_fk_system_menu_id` FOREIGN KEY (`parent_id`) REFERENCES `system_menu` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_menu`
--

LOCK TABLES `system_menu` WRITE;
/*!40000 ALTER TABLE `system_menu` DISABLE KEYS */;
INSERT INTO `system_menu` VALUES ('07ad99e6eae44b0aaa717673d8641238','2024-10-25 02:30:52.099000','2024-10-25 02:30:52.099000',2,'新增','/api/system/menu/',NULL,1,NULL,'242704c7b5eb4b3e958123da9ede5c7e','d5fbdf9f37054fbab91cf931dcdbe123','/api/system/menu/:add',NULL),('0be68109bf3446e9913fb44135b9efa1','2024-10-25 02:48:18.936000','2024-10-25 02:48:18.936000',2,'删除','/api/system/dept/',NULL,1,NULL,'2298b1d71eba445a8a4c0a25a9e96056','aee2c869be1c4ab2b3210c3e77c04160','/api/system/dept/:delete',NULL),('16e24578c16249289cc465596d8cb94a','2024-10-14 09:21:34.349000','2024-10-14 13:30:40.431000',1,'权限测试','/test/permission','/test/permission/index',1,NULL,'bd4b1268db6b4cafbf7ea8c2a697ed0c','a17cb82910be43008ddce5b365d3ef38',NULL,NULL),('1c5e1b60ff5e4aa4b8b33fcab50340c7','2024-10-24 07:47:47.529000','2024-10-24 07:55:17.086000',2,'查看','/api/test/permission/',NULL,1,NULL,'9435b8e00e01445f906049537df8161f','16e24578c16249289cc465596d8cb94a','/api/test/permission/:read',NULL),('1ddacfcac8e04971812d57338800e278','2024-10-25 02:47:56.316000','2024-10-25 02:47:56.316000',2,'删除','/api/user/',NULL,1,NULL,'d6638fb69a8e40639230ec260cbf705b','5eb483bd76e346c4b60c323a8b876fe4','/api/user/:delete',NULL),('2570af26944c47ddaf41a211d3ef02f2','2024-10-30 07:43:30.634000','2024-10-31 02:22:31.816000',1,'登录日志','/monitor/loginlog','/monitor/loginlog/index',1,NULL,'6adc30be629d4410b5b06476d2564298','dc368aa0c7fd4ec4b17f176ba2e3be73',NULL,NULL),('3c2c9a414aaf4afd8cda4c3b91be7c30','2024-10-24 07:48:34.380000','2024-10-24 08:28:08.511000',2,'查看2','/api/test/permission2/',NULL,1,NULL,'ee3ae72513764d39900a61c81a77d496','16e24578c16249289cc465596d8cb94a','/api/test/permission2/:read',NULL),('436077d976544d569f18895d44bf2b6b','2024-10-25 02:42:04.452000','2024-10-25 02:42:04.452000',2,'查看','/api/system/role/',NULL,1,NULL,'0ca55276c54d4d61a8171ca4037ed2c7','dcbdeec09e594c87ab4b6a362a27bd84','/api/system/role/:read',NULL),('44d7669a87a2430c9fe895757d6f8e01','2024-10-25 02:48:18.914000','2024-10-25 02:48:18.914000',2,'新增','/api/system/dept/',NULL,1,NULL,'3cfdb18a3ed441938753004d790843fd','aee2c869be1c4ab2b3210c3e77c04160','/api/system/dept/:add',NULL),('53f9a426389e45eca491b632c7c27518','2024-12-02 07:29:03.582762','2024-12-02 07:30:23.406294',2,'清空登录日志','/api/monitor/clearloginlog/',NULL,1,NULL,'6a8feb7c652d47f9ad7621a2749ad1ff','2570af26944c47ddaf41a211d3ef02f2','/api/monitor/clearloginlog/:delete',NULL),('5e54be04b0e84befbf21a11df0677285','2024-10-25 02:30:52.121000','2024-10-25 02:30:52.121000',2,'删除','/api/system/menu/',NULL,1,NULL,'fded4dba8f384fc3b13b74d11b9d6823','d5fbdf9f37054fbab91cf931dcdbe123','/api/system/menu/:delete',NULL),('5eb483bd76e346c4b60c323a8b876fe4','2024-10-14 14:04:37.888000','2024-12-16 06:11:56.664845',1,'用户管理','/system/user','/user/index',1,NULL,'4e161fb16f664e9ba1d21231869890e0','e3b423d38ad042b0a612516c93208fa8',NULL,NULL),('653c5f9aa5e7490fb4acd9158ceeb975','2024-12-02 07:30:13.193703','2024-12-02 07:30:13.193735',2,'修改','/api/monitor/loginlog/',NULL,1,NULL,'57a3a41dc6084553a46871f3d47298e2','2570af26944c47ddaf41a211d3ef02f2','/api/monitor/loginlog/:change',NULL),('7649afd0d7aa4b7a80048b7bfd63b735','2024-12-02 07:30:13.169044','2024-12-02 07:30:13.169078',2,'查看','/api/monitor/loginlog/',NULL,1,NULL,'bb0f12fb9d4d4753b59bc25fc53ba6ce','2570af26944c47ddaf41a211d3ef02f2','/api/monitor/loginlog/:read',NULL),('7c4a94ae862f4b9595b8b07ec5290ba3','2024-12-02 07:32:12.827655','2024-12-02 07:32:12.827680',2,'删除','/api/monitor/operationlog/',NULL,1,NULL,'bef57f9e28b441c49956100645894887','93134e5ab4be4f59a5c329547d4809ab','/api/monitor/operationlog/:delete',NULL),('7ee765a0136543c59cc43af8920bd775','2024-12-02 07:30:13.204690','2024-12-02 07:30:13.204721',2,'删除','/api/monitor/loginlog/',NULL,1,NULL,'6c199049ded043c5a154d9336ddb102f','2570af26944c47ddaf41a211d3ef02f2','/api/monitor/loginlog/:delete',NULL),('82b02bc107fc4e4ab48c1906069bc931','2024-10-25 02:30:52.088000','2024-10-25 02:30:52.088000',2,'查看','/api/system/menu/',NULL,1,NULL,'6bff4051e2054de1b3435e09dad6ea59','d5fbdf9f37054fbab91cf931dcdbe123','/api/system/menu/:read',NULL),('90a7dd2015b64792ab246293081293d5','2024-10-25 02:48:18.900000','2024-10-25 02:48:18.900000',2,'查看','/api/system/dept/',NULL,1,NULL,'bf93cd77d279457798456d52c71de464','aee2c869be1c4ab2b3210c3e77c04160','/api/system/dept/:read',NULL),('93134e5ab4be4f59a5c329547d4809ab','2024-10-30 09:32:31.361000','2024-10-30 09:32:31.361000',1,'操作日志','/monitor/operationlog','/monitor/operationlog/index',1,NULL,'bfcd1b2a597b419c8b154d38d58ef8c9','dc368aa0c7fd4ec4b17f176ba2e3be73',NULL,NULL),('9db4963fa84e419fbbdf3d2ef794af6f','2024-10-25 02:42:04.482000','2024-10-25 02:42:04.482000',2,'删除','/api/system/role/',NULL,1,NULL,'43a996b815f0496f933b93bed0a887f2','dcbdeec09e594c87ab4b6a362a27bd84','/api/system/role/:delete',NULL),('a17cb82910be43008ddce5b365d3ef38','2024-09-15 14:22:23.832000','2024-10-14 13:55:08.497000',1,'功能测试','/test',NULL,1,NULL,'d19b1c05a9624923b9394471b52cdd60',NULL,NULL,NULL),('a20fd5c091e046d287298debe16d97c4','2024-12-02 07:32:12.817270','2024-12-02 07:32:12.817297',2,'修改','/api/monitor/operationlog/',NULL,1,NULL,'ffaa5a304c0a4bb19f3777b8affb51ef','93134e5ab4be4f59a5c329547d4809ab','/api/monitor/operationlog/:change',NULL),('a75c5a78f5ff43669dfb4c27d703dbf9','2024-10-25 02:47:56.291000','2024-10-25 02:47:56.291000',2,'新增','/api/user/',NULL,1,NULL,'c26066adcb554c49ae275a74b5dc4361','5eb483bd76e346c4b60c323a8b876fe4','/api/user/:add',NULL),('aaee57f8620848eda3c6196e2ab24932','2024-12-02 07:32:12.806742','2024-12-02 07:32:12.806768',2,'新增','/api/monitor/operationlog/',NULL,1,NULL,'b9dacb7896644a208264d2f56238b083','93134e5ab4be4f59a5c329547d4809ab','/api/monitor/operationlog/:add',NULL),('aee2c869be1c4ab2b3210c3e77c04160','2024-10-14 13:59:11.676000','2024-10-16 09:40:23.503000',1,'部门管理','/system/department','/department/index',1,NULL,'af4c154e21ad4216b236ae0da15a1fa1','e3b423d38ad042b0a612516c93208fa8',NULL,NULL),('b331ac354e154204ba945f1b81e40054','2024-12-02 07:32:56.969059','2024-12-02 07:33:06.045546',2,'清空操作日志','/api/monitor/clearoperationlog/',NULL,1,NULL,'7470bab6f81648be9c2a18a49f9c51c5','93134e5ab4be4f59a5c329547d4809ab','/api/monitor/clearoperationlog/:delete',NULL),('c855293d4f35490eb4e6ea79eb4678ce','2024-10-25 02:42:04.463000','2024-10-25 02:42:04.463000',2,'新增','/api/system/role/',NULL,1,NULL,'823ae329bef947a4a4ede56f0d19b584','dcbdeec09e594c87ab4b6a362a27bd84','/api/system/role/:add',NULL),('cd6d7efd010f497b8f84fc40ed4931b2','2024-10-25 02:47:56.271000','2024-10-25 02:47:56.271000',2,'查看','/api/user/',NULL,1,NULL,'58b9dacfedb9477ba625c89a806f1af6','5eb483bd76e346c4b60c323a8b876fe4','/api/user/:read',NULL),('cfa4406786994e5bb40dd3cd726c05c5','2024-10-25 02:30:52.108000','2024-10-25 02:30:52.108000',2,'修改','/api/system/menu/',NULL,1,NULL,'d0a38a0d611d469e8741f07f3c84e910','d5fbdf9f37054fbab91cf931dcdbe123','/api/system/menu/:change',NULL),('d5fbdf9f37054fbab91cf931dcdbe123','2024-10-14 13:52:42.273000','2024-10-16 09:38:15.818000',1,'菜单权限','/system/permission','/system/permission/index',1,NULL,'79c28ca959014d80802fe80b8fe88f54','e3b423d38ad042b0a612516c93208fa8',NULL,NULL),('d6cb60987ad34d7bab5aa03fbeaa414b','2024-12-02 07:32:12.792292','2024-12-02 07:32:12.792315',2,'查看','/api/monitor/operationlog/',NULL,1,NULL,'b845642772fc49d48cc8442b7f5366f2','93134e5ab4be4f59a5c329547d4809ab','/api/monitor/operationlog/:read',NULL),('dc368aa0c7fd4ec4b17f176ba2e3be73','2024-10-30 07:42:22.305000','2024-12-16 03:39:31.286205',1,'系统监控','/monitor',NULL,1,NULL,'7c9e740400a140418af8a590a070bc26',NULL,NULL,NULL),('dcbdeec09e594c87ab4b6a362a27bd84','2024-10-14 14:00:01.203000','2024-10-16 09:39:14.253000',1,'角色管理','/system/role','/role/index',1,NULL,'7710f9d307d14fc49072115089b0ccdb','e3b423d38ad042b0a612516c93208fa8',NULL,NULL),('de834396885e4c1ca53ca378a6875390','2024-10-25 02:48:18.929000','2024-10-25 02:48:18.929000',2,'修改','/api/system/dept/',NULL,1,NULL,'8d042eb5249b4c95a8a2ffa76b41eaf0','aee2c869be1c4ab2b3210c3e77c04160','/api/system/dept/:change',NULL),('e3b423d38ad042b0a612516c93208fa8','2024-10-14 13:49:39.867000','2024-12-16 03:39:27.300147',1,'系统管理','/system',NULL,1,NULL,'eafcd30db2624ea8ad1a1a63ffd27609',NULL,NULL,NULL),('fb258ac15d3c4519955d316c2acaf7c0','2024-12-02 07:30:13.182131','2024-12-02 07:30:13.182163',2,'新增','/api/monitor/loginlog/',NULL,1,NULL,'fbca519adc33434bb244a56319fda7ab','2570af26944c47ddaf41a211d3ef02f2','/api/monitor/loginlog/:add',NULL),('fbf4bfce5f5344fc86041a3f3bcf3b56','2024-10-25 02:42:04.477000','2024-10-25 02:42:04.477000',2,'修改','/api/system/role/',NULL,1,NULL,'fcd52d1fbdd8474fa78079df801427a5','dcbdeec09e594c87ab4b6a362a27bd84','/api/system/role/:change',NULL),('fd445ccbf5ec4dbcb94b2cdef097a3bd','2024-10-25 02:47:56.305000','2024-10-25 02:47:56.305000',2,'修改','/api/user/',NULL,1,NULL,'2a489016147a4687a6f6ae7d73df672f','5eb483bd76e346c4b60c323a8b876fe4','/api/user/:change',NULL);
/*!40000 ALTER TABLE `system_menu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-02 13:46:01
