-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: mysql-3a79300a-legosumo-e2db.a.aivencloud.com    Database: legosumo_db
-- ------------------------------------------------------
-- Server version	8.0.30

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '8628e6ce-7145-11ee-96a7-06defcd25d78:1-878';


--
-- Table structure for table `Competition`
--

DROP TABLE IF EXISTS `Competition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Competition` (
  `Competition_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `games_per_team` int DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`Competition_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `Division`
--

DROP TABLE IF EXISTS `Division`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Division` (
  `Division_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Division_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Division`
--

LOCK TABLES `Division` WRITE;
/*!40000 ALTER TABLE `Division` DISABLE KEYS */;
INSERT INTO `Division` VALUES (1,'Science'),(2,'Technology'),(3,'Engineering'),(4,'Math');
/*!40000 ALTER TABLE `Division` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Table structure for table `School`
--

DROP TABLE IF EXISTS `School`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `School` (
  `School_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `street_address_line_1` varchar(45) DEFAULT NULL,
  `street_address_line_2` varchar(45) DEFAULT NULL,
  `suburb` varchar(60) DEFAULT NULL,
  `state` varchar(3) DEFAULT NULL,
  `postcode` varchar(4) DEFAULT NULL,
  `contact_name` varchar(100) DEFAULT NULL,
  `contact_number` varchar(15) DEFAULT NULL,
  `email_address` varchar(60) DEFAULT NULL,
  `paid` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`School_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;



--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `User_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `surname` varchar(45) DEFAULT NULL,
  `email_address` varchar(60) DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `password` varchar(256) DEFAULT NULL,
  `role` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'','','','Science 1','EF4095BA96E4950581A6CC5F9DE4092A20901A2CFAF9D2A3B02891AFCEAE6E34','Judge'),(2,'','','','Science 2','EF4095BA96E4950581A6CC5F9DE4092A20901A2CFAF9D2A3B02891AFCEAE6E34','Judge'),(3,'','','','Science 3','EF4095BA96E4950581A6CC5F9DE4092A20901A2CFAF9D2A3B02891AFCEAE6E34','Judge'),(4,'','','','Science 4','EF4095BA96E4950581A6CC5F9DE4092A20901A2CFAF9D2A3B02891AFCEAE6E34','Judge'),(5,'','','','Science 5','EF4095BA96E4950581A6CC5F9DE4092A20901A2CFAF9D2A3B02891AFCEAE6E34','Judge'),(6,'','','','Technology 1','EF4095BA96E4950581A6CC5F9DE4092A20901A2CFAF9D2A3B02891AFCEAE6E34','Judge'),(7,'','','','Technology 2','EF4095BA96E4950581A6CC5F9DE4092A20901A2CFAF9D2A3B02891AFCEAE6E34','Judge'),(8,'','','','Technology 3','EF4095BA96E4950581A6CC5F9DE4092A20901A2CFAF9D2A3B02891AFCEAE6E34','Judge'),(9,'','','','Technology 4','EF4095BA96E4950581A6CC5F9DE4092A20901A2CFAF9D2A3B02891AFCEAE6E34','Judge'),(10,'','','','Technology 5','EF4095BA96E4950581A6CC5F9DE4092A20901A2CFAF9D2A3B02891AFCEAE6E34','Judge'),(11,'','','','Engineering 1','EF4095BA96E4950581A6CC5F9DE4092A20901A2CFAF9D2A3B02891AFCEAE6E34','Judge'),(12,'','','','Engineering 2','EF4095BA96E4950581A6CC5F9DE4092A20901A2CFAF9D2A3B02891AFCEAE6E34','Judge'),(13,'','','','Engineering 3','EF4095BA96E4950581A6CC5F9DE4092A20901A2CFAF9D2A3B02891AFCEAE6E34','Judge'),(14,'','','','Engineering 4','EF4095BA96E4950581A6CC5F9DE4092A20901A2CFAF9D2A3B02891AFCEAE6E34','Judge'),(15,'','','','Engineering 5','EF4095BA96E4950581A6CC5F9DE4092A20901A2CFAF9D2A3B02891AFCEAE6E34','Judge'),(16,'','','','Math 1','EF4095BA96E4950581A6CC5F9DE4092A20901A2CFAF9D2A3B02891AFCEAE6E34','Judge'),(17,'','','','Math 2','EF4095BA96E4950581A6CC5F9DE4092A20901A2CFAF9D2A3B02891AFCEAE6E34','Judge'),(18,'','','','Math 3','EF4095BA96E4950581A6CC5F9DE4092A20901A2CFAF9D2A3B02891AFCEAE6E34','Judge'),(19,'','','','Math 4','EF4095BA96E4950581A6CC5F9DE4092A20901A2CFAF9D2A3B02891AFCEAE6E34','Judge'),(20,'','','','Math 5','EF4095BA96E4950581A6CC5F9DE4092A20901A2CFAF9D2A3B02891AFCEAE6E34','Judge'),(21,'Daniel','Ricardo','drica5@eq.edu.au','RicardoD','A8335B39E3B25B7F331247280F2EE65CCED0DED67EFFBAF27B2E60E33B59AB5E','Admin');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Table structure for table `Field`
--

DROP TABLE IF EXISTS `Field`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Field` (
  `Field_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `judge` int DEFAULT NULL,
  PRIMARY KEY (`Field_id`),
  KEY `fk_judge_idx` (`judge`),
  CONSTRAINT `fk_judge` FOREIGN KEY (`judge`) REFERENCES `User` (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Field`
--

LOCK TABLES `Field` WRITE;
/*!40000 ALTER TABLE `Field` DISABLE KEYS */;
INSERT INTO `Field` VALUES (1,'Science 1',1),(2,'Science 2',2),(3,'Science 3',3),(4,'Science 4',4),(5,'Science 5',5),(6,'Technology 1',6),(7,'Technology 2',7),(8,'Technology 3',8),(9,'Technology 4',9),(10,'Technology 5',10),(11,'Engineering 1',11),(12,'Engineering 2',12),(13,'Engineering 3',13),(14,'Engineering 4',14),(15,'Engineering 5',15),(16,'Math 1',16),(17,'Math 2',17),(18,'Math 3',18),(19,'Math 4',19),(20,'Math 5',20);
/*!40000 ALTER TABLE `Field` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Table structure for table `Team`
--

DROP TABLE IF EXISTS `Team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Team` (
  `Team_id` int NOT NULL AUTO_INCREMENT,
  `School_id` int NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Team_id`),
  KEY `fk_Team_School1_idx` (`School_id`),
  CONSTRAINT `fk_Team_School1` FOREIGN KEY (`School_id`) REFERENCES `School` (`School_id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;



--
-- Table structure for table `Division_has_Competition`
--

DROP TABLE IF EXISTS `Division_has_Competition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Division_has_Competition` (
  `DivisionhasCompetition_id` int NOT NULL AUTO_INCREMENT,
  `Division_id` int NOT NULL,
  `Competition_id` int NOT NULL,
  `nbr_of_fields` int DEFAULT NULL,
  PRIMARY KEY (`DivisionhasCompetition_id`),
  KEY `fk_Division_has_Competition_Competition1_idx` (`Competition_id`),
  KEY `fk_Division_has_Competition_Division1_idx` (`Division_id`),
  CONSTRAINT `fk_Division_has_Competition_Competition1` FOREIGN KEY (`Competition_id`) REFERENCES `Competition` (`Competition_id`),
  CONSTRAINT `fk_Division_has_Competition_Division1` FOREIGN KEY (`Division_id`) REFERENCES `Division` (`Division_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;



--
-- Table structure for table `Division_has_Field`
--

DROP TABLE IF EXISTS `Division_has_Field`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Division_has_Field` (
  `DivisionhasField_id` int NOT NULL AUTO_INCREMENT,
  `Division_id` int NOT NULL,
  `Field_id` int NOT NULL,
  PRIMARY KEY (`DivisionhasField_id`),
  KEY `fk_Division_has_Field_Field1_idx` (`Field_id`),
  KEY `fk_Division_has_Field_Division1_idx` (`Division_id`),
  CONSTRAINT `fk_Division_has_Field_Division1` FOREIGN KEY (`Division_id`) REFERENCES `Division` (`Division_id`),
  CONSTRAINT `fk_Division_has_Field_Field1` FOREIGN KEY (`Field_id`) REFERENCES `Field` (`Field_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Division_has_Field`
--

LOCK TABLES `Division_has_Field` WRITE;
/*!40000 ALTER TABLE `Division_has_Field` DISABLE KEYS */;
INSERT INTO `Division_has_Field` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,2,6),(7,2,7),(8,2,8),(9,2,9),(10,2,10),(11,3,11),(12,3,12),(13,3,13),(14,3,14),(15,3,15),(16,4,16),(17,4,17),(18,4,18),(19,4,19),(20,4,20);
/*!40000 ALTER TABLE `Division_has_Field` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Division_has_Team`
--

DROP TABLE IF EXISTS `Division_has_Team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Division_has_Team` (
  `DivisionhasTeam_id` int NOT NULL AUTO_INCREMENT,
  `Division_id` int NOT NULL,
  `Team_id` int NOT NULL,
  PRIMARY KEY (`DivisionhasTeam_id`),
  KEY `fk_Division_has_Team_Team1_idx` (`Team_id`),
  KEY `fk_Division_has_Team_Division1_idx` (`Division_id`),
  CONSTRAINT `fk_Division_has_Team_Division1` FOREIGN KEY (`Division_id`) REFERENCES `Division` (`Division_id`),
  CONSTRAINT `fk_Division_has_Team_Team1` FOREIGN KEY (`Team_id`) REFERENCES `Team` (`Team_id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;



--
-- Table structure for table `Checked_In`
--

DROP TABLE IF EXISTS `Checked_In`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Checked_In` (
  `Checked_In_id` int NOT NULL AUTO_INCREMENT,
  `Competition_id` int NOT NULL,
  `Division_id` int NOT NULL,
  `Team_id` int NOT NULL,
  `checked_in` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`Checked_In_id`),
  KEY `fk_Checked_In_Team1_idx` (`Team_id`),
  KEY `fk_Checked_In_Division1_idx` (`Division_id`),
  KEY `fk_Checked_In_Competition1_idx` (`Competition_id`),
  CONSTRAINT `fk_Checked_In_Competition1` FOREIGN KEY (`Competition_id`) REFERENCES `Competition` (`Competition_id`),
  CONSTRAINT `fk_Checked_In_Division1` FOREIGN KEY (`Division_id`) REFERENCES `Division` (`Division_id`),
  CONSTRAINT `fk_Checked_In_Team1` FOREIGN KEY (`Team_id`) REFERENCES `Team` (`Team_id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;



--
-- Table structure for table `Game_Result`
--

DROP TABLE IF EXISTS `Game_Result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Game_Result` (
  `Game_id` int NOT NULL AUTO_INCREMENT,
  `Competition_id` int NOT NULL,
  `Division_id` int NOT NULL,
  `round` int DEFAULT NULL,
  `team1` int DEFAULT NULL,
  `team2` int DEFAULT NULL,
  `field` int DEFAULT NULL,
  `team1_points` int DEFAULT NULL,
  `team2_points` int DEFAULT NULL,
  `start_time` time DEFAULT NULL,
  PRIMARY KEY (`Game_id`),
  KEY `field_idx` (`field`),
  KEY `team1_idx` (`team1`),
  KEY `team2_idx` (`team2`),
  KEY `fk_Game_Result_Division1_idx` (`Division_id`),
  KEY `fk_Game_Result_Competition1_idx` (`Competition_id`),
  CONSTRAINT `field` FOREIGN KEY (`field`) REFERENCES `Field` (`Field_id`),
  CONSTRAINT `fk_Game_Result_Competition1` FOREIGN KEY (`Competition_id`) REFERENCES `Competition` (`Competition_id`),
  CONSTRAINT `fk_Game_Result_Division1` FOREIGN KEY (`Division_id`) REFERENCES `Division` (`Division_id`),
  CONSTRAINT `team1` FOREIGN KEY (`team1`) REFERENCES `Team` (`Team_id`),
  CONSTRAINT `team2` FOREIGN KEY (`team2`) REFERENCES `Team` (`Team_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;



--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-10-30 03:28:43.929950'),(2,'auth','0001_initial','2023-10-30 03:28:53.933733'),(3,'admin','0001_initial','2023-10-30 03:28:56.646283'),(4,'admin','0002_logentry_remove_auto_add','2023-10-30 03:28:57.351496'),(5,'admin','0003_logentry_add_action_flag_choices','2023-10-30 03:28:58.161898'),(6,'contenttypes','0002_remove_content_type_name','2023-10-30 03:29:00.729631'),(7,'auth','0002_alter_permission_name_max_length','2023-10-30 03:29:02.010321'),(8,'auth','0003_alter_user_email_max_length','2023-10-30 03:29:03.208411'),(9,'auth','0004_alter_user_username_opts','2023-10-30 03:29:04.009770'),(10,'auth','0005_alter_user_last_login_null','2023-10-30 03:29:05.213081'),(11,'auth','0006_require_contenttypes_0002','2023-10-30 03:29:06.022021'),(12,'auth','0007_alter_validators_add_error_messages','2023-10-30 03:29:06.809140'),(13,'auth','0008_alter_user_username_max_length','2023-10-30 03:29:08.009650'),(14,'auth','0009_alter_user_last_name_max_length','2023-10-30 03:29:09.259919'),(15,'auth','0010_alter_group_name_max_length','2023-10-30 03:29:10.409341'),(16,'auth','0011_update_proxy_permissions','2023-10-30 03:29:12.259749'),(17,'auth','0012_alter_user_first_name_max_length','2023-10-30 03:29:13.378478'),(18,'sessions','0001_initial','2023-10-30 03:29:15.528326');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-30 13:43:47
