-- MySQL dump 10.13  Distrib 5.5.62, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: smartTrainingDB
-- ------------------------------------------------------
-- Server version	5.5.62-0+deb8u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `country`
--

DROP TABLE IF EXISTS `country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `country` (
  `idcountry` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `createdCountry` datetime NOT NULL,
  `modifiedCountry` datetime NOT NULL,
  PRIMARY KEY (`idcountry`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `country`
--

LOCK TABLES `country` WRITE;
/*!40000 ALTER TABLE `country` DISABLE KEYS */;
INSERT INTO `country` VALUES (1,'CHILE','2018-12-16 23:08:44','2018-12-16 23:08:44'),(2,'EEUU','2018-12-16 23:09:00','2018-12-16 23:09:00');
/*!40000 ALTER TABLE `country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dataSet`
--

DROP TABLE IF EXISTS `dataSet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dataSet` (
  `iddataSet` int(11) NOT NULL AUTO_INCREMENT,
  `nameDataSet` varchar(45) NOT NULL,
  `createdDataSet` datetime NOT NULL,
  `modifiedDataSet` datetime NOT NULL,
  `user` int(11) NOT NULL,
  `tipoDataSet` varchar(45) NOT NULL,
  `job` int(11) NOT NULL,
  PRIMARY KEY (`iddataSet`),
  KEY `fk_dataSet_user_idx` (`user`),
  CONSTRAINT `fk_dataSet_user` FOREIGN KEY (`user`) REFERENCES `user` (`iduser`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1549921665 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dataSet`
--

LOCK TABLES `dataSet` WRITE;
/*!40000 ALTER TABLE `dataSet` DISABLE KEYS */;
INSERT INTO `dataSet` VALUES (1549818458,'irisCluster.csv','2019-02-10 12:07:38','2019-02-10 12:07:38',1547293936,'queue-PREDICTION',1549818458),(1549819411,'iris.csv','2019-02-10 12:23:31','2019-02-10 12:23:31',1547293936,'queue-CLASSIFICATION',1549819411),(1549825830,'dataCSV.csv','2019-02-10 14:10:30','2019-02-10 14:10:30',1549825107,'STATISTICAL',1549825830),(1549826058,'iris.csv','2019-02-10 14:14:18','2019-02-10 14:14:18',1549825107,'STATISTICAL',1549826058),(1549826428,'irisCluster.csv','2019-02-10 14:20:28','2019-02-10 14:20:28',1549825107,'KERNEL-PCA',1549826428),(1549826594,'irisCluster.csv','2019-02-10 14:23:14','2019-02-10 14:23:14',1549825107,'PCA-INCREMENTAL',1549826594),(1549826662,'irisCluster.csv','2019-02-10 14:24:22','2019-02-10 14:24:22',1549825107,'MUTUAL-INFORMATION',1549826662),(1549826841,'irisCluster.csv','2019-02-10 14:27:21','2019-02-10 14:27:21',1549825107,'CLUSTERING-FULL',1549826841),(1549827055,'iris.csv','2019-02-10 14:30:55','2019-02-10 14:30:55',1549825107,'CLASSIFICATION',1549827055),(1549827332,'irisCluster.csv','2019-02-10 14:35:32','2019-02-10 14:35:32',1549825107,'PREDICTION',1549827332),(1549906626,'dataSetFrequence.csv','2019-02-11 12:37:06','2019-02-11 12:37:06',1547293936,'CLUSTERING-FULL',1549906626),(1549906981,'dataSetFrequence.csv','2019-02-11 12:43:01','2019-02-11 12:43:01',1547293936,'CLUSTERING',1549906981),(1549907015,'dataSetFrequence.csv','2019-02-11 12:43:35','2019-02-11 12:43:35',1547293936,'CLUSTERING',1549907015),(1549907228,'dataSetFrequence.csv','2019-02-11 12:47:08','2019-02-11 12:47:08',1547293936,'CLUSTERING',1549907228),(1549907259,'dataSetFrequence.csv','2019-02-11 12:47:39','2019-02-11 12:47:39',1547293936,'CLUSTERING',1549907259),(1549907355,'dataSetFrequence.csv','2019-02-11 12:49:15','2019-02-11 12:49:15',1547293936,'CLUSTERING',1549907355),(1549907413,'dataSetFrequence.csv','2019-02-11 12:50:13','2019-02-11 12:50:13',1547293936,'CLUSTERING-FULL',1549907413),(1549921062,'1BNI.csv','2019-02-11 16:37:42','2019-02-11 16:37:42',1547293936,'STATISTICAL',1549921062),(1549921315,'1STN.csv','2019-02-11 16:41:55','2019-02-11 16:41:55',1547293936,'STATISTICAL',1549921315),(1549921371,'1STN.csv','2019-02-11 16:42:51','2019-02-11 16:42:51',1547293936,'STATISTICAL',1549921371),(1549921495,'2LZM.csv','2019-02-11 16:44:55','2019-02-11 16:44:55',1547293936,'STATISTICAL',1549921495),(1549921563,'2RN2.csv','2019-02-11 16:46:03','2019-02-11 16:46:03',1547293936,'STATISTICAL',1549921563),(1549921664,'2RN2.csv','2019-02-11 16:47:44','2019-02-11 16:47:44',1547293936,'STATISTICAL',1549921664);
/*!40000 ALTER TABLE `dataSet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feature`
--

DROP TABLE IF EXISTS `feature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feature` (
  `idfeature` int(11) NOT NULL AUTO_INCREMENT,
  `nameFeature` varchar(45) NOT NULL,
  `kind` varchar(45) NOT NULL,
  `dataSet` int(11) NOT NULL,
  PRIMARY KEY (`idfeature`),
  KEY `fk_feature_dataSet1_idx` (`dataSet`),
  CONSTRAINT `fk_feature_dataSet1` FOREIGN KEY (`dataSet`) REFERENCES `dataSet` (`iddataSet`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3468 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feature`
--

LOCK TABLES `feature` WRITE;
/*!40000 ALTER TABLE `feature` DISABLE KEYS */;
INSERT INTO `feature` VALUES (3408,'AAWt','DISCRETA',1549825830),(3409,'AAMt','DISCRETA',1549825830),(3410,'Sstruct','DISCRETA',1549825830),(3411,'SaccW','CONTINUA',1549825830),(3412,'ShbondsW','DISCRETA',1549825830),(3413,'SaccM','CONTINUA',1549825830),(3414,'ShbondsM','DISCRETA',1549825830),(3415,'yDDG','CONTINUA',1549825830),(3416,'Result','DISCRETA',1549825830),(3417,'Positiontype','DISCRETA',1549825830),(3418,'ProteinPropens','CONTINUA',1549825830),(3419,'Positionaccept','CONTINUA',1549825830),(3420,'MOSST','CONTINUA',1549825830),(3421,'SectorSuperficie','DISCRETA',1549825830),(3422,'Functionalrelevancefunction','CONTINUA',1549825830),(3423,'Clinical','DISCRETA',1549825830),(3424,'sepal.length','CONTINUA',1549826058),(3425,'sepal.width','CONTINUA',1549826058),(3426,'petal.length','CONTINUA',1549826058),(3427,'petal.width','CONTINUA',1549826058),(3428,'variety','DISCRETA',1549826058),(3429,'sepal.length','CONTINUA',1549827055),(3430,'sepal.width','CONTINUA',1549827055),(3431,'petal.length','CONTINUA',1549827055),(3432,'petal.width','CONTINUA',1549827055),(3433,'variety','DISCRETA',1549827055),(3434,'sepal.length','CONTINUA',1549827332),(3435,'sepal.width','CONTINUA',1549827332),(3436,'petal.length','CONTINUA',1549827332),(3437,'petal.width','CONTINUA',1549827332),(3438,'PDB_code','DISCRETA',1549921062),(3439,'AAWt','DISCRETA',1549921062),(3440,'Position','CONTINUA',1549921062),(3441,'AAMt','DISCRETA',1549921062),(3442,'Class','DISCRETA',1549921062),(3443,'PDB_code','DISCRETA',1549921315),(3444,'AAWt','DISCRETA',1549921315),(3445,'Position','CONTINUA',1549921315),(3446,'AAMt','DISCRETA',1549921315),(3447,'Class','DISCRETA',1549921315),(3448,'PDB_code','DISCRETA',1549921371),(3449,'AAWt','DISCRETA',1549921371),(3450,'Position','CONTINUA',1549921371),(3451,'AAMt','DISCRETA',1549921371),(3452,'Class','DISCRETA',1549921371),(3453,'PDB_code','DISCRETA',1549921495),(3454,'AAWt','DISCRETA',1549921495),(3455,'Position','CONTINUA',1549921495),(3456,'AAMt','DISCRETA',1549921495),(3457,'Class','DISCRETA',1549921495),(3458,'PDB_code','DISCRETA',1549921563),(3459,'AAWt','DISCRETA',1549921563),(3460,'Position','CONTINUA',1549921563),(3461,'AAMt','DISCRETA',1549921563),(3462,'Class','DISCRETA',1549921563),(3463,'PDB_code','DISCRETA',1549921664),(3464,'AAWt','DISCRETA',1549921664),(3465,'Position','CONTINUA',1549921664),(3466,'AAMt','DISCRETA',1549921664),(3467,'Class','DISCRETA',1549921664);
/*!40000 ALTER TABLE `feature` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institution`
--

DROP TABLE IF EXISTS `institution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `institution` (
  `idinstitution` int(11) NOT NULL,
  `nameInstitution` varchar(45) NOT NULL,
  `createdInstitution` datetime NOT NULL,
  `modifiedInstitution` datetime NOT NULL,
  `country` int(11) NOT NULL,
  PRIMARY KEY (`idinstitution`),
  KEY `fk_institution_country_idx` (`country`),
  CONSTRAINT `fk_institution_country` FOREIGN KEY (`country`) REFERENCES `country` (`idcountry`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institution`
--

LOCK TABLES `institution` WRITE;
/*!40000 ALTER TABLE `institution` DISABLE KEYS */;
INSERT INTO `institution` VALUES (1,'UNIVERSIDAD DE CHILE','2018-12-16 23:12:01','2018-12-16 23:12:01',1),(2,'UNIVERSIDAD DE SANTIAGO','2018-12-16 23:12:10','2018-12-16 23:12:10',1),(3,'UNIVERSIDAD DE CONCEPCION','2018-12-16 23:12:21','2018-12-16 23:12:21',1),(1547294173,'Universidad AndrÃ©s Bello','2019-01-12 08:56:13','2019-01-12 08:56:13',1),(1549825107,'Universidad de los Andes','2019-02-10 13:58:27','2019-02-10 13:58:27',1);
/*!40000 ALTER TABLE `institution` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job`
--

DROP TABLE IF EXISTS `job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `job` (
  `idjob` int(11) NOT NULL AUTO_INCREMENT,
  `nameJob` varchar(45) NOT NULL,
  `descriptionJob` varchar(450) NOT NULL,
  `createdJob` datetime NOT NULL,
  `modifiedJob` datetime NOT NULL,
  `user` int(11) NOT NULL,
  `nameDataset` varchar(450) NOT NULL,
  `statusJob` varchar(45) NOT NULL,
  `tipo_job` varchar(45) NOT NULL,
  `algorithms` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idjob`),
  KEY `fk_job_user1_idx` (`user`),
  CONSTRAINT `fk_job_user1` FOREIGN KEY (`user`) REFERENCES `user` (`iduser`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1549921665 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job`
--

LOCK TABLES `job` WRITE;
/*!40000 ALTER TABLE `job` DISABLE KEYS */;
INSERT INTO `job` VALUES (1549818458,'Testing queue prediction','Testing queue prediction','2019-02-10 12:07:38','2019-02-10 12:22:18',1547293936,'irisCluster.csv','PROCESSING','queue-PREDICTION','-'),(1549819411,'Testing class queue system','Testing class queue','2019-02-10 12:23:31','2019-02-10 14:41:15',1547293936,'iris.csv','FINISH','queue-CLASSIFICATION','-'),(1549825830,'trabajo1','primer intento','2019-02-10 14:10:30','2019-02-10 14:10:30',1549825107,'dataCSV.csv','FINISH','DISTRIBUTION','-'),(1549826058,'trab2','nuevo','2019-02-10 14:14:18','2019-02-10 14:14:18',1549825107,'iris.csv','FINISH','SPLOM','-'),(1549826428,'trab3','int','2019-02-10 14:20:28','2019-02-10 14:20:29',1549825107,'irisCluster.csv','FINISH','KERNEL-PCA','-'),(1549826594,'6','7','2019-02-10 14:23:14','2019-02-10 14:23:14',1549825107,'irisCluster.csv','FINISH','PCA-INCREMENTAL','-'),(1549826662,'7','6','2019-02-10 14:24:22','2019-02-10 14:24:23',1549825107,'irisCluster.csv','FINISH','MUTUAL-INFORMATION','-'),(1549826841,'8','88','2019-02-10 14:27:21','2019-02-10 14:28:48',1549825107,'irisCluster.csv','FINISH','CLUSTERING-FULL','-'),(1549827055,'9','99','2019-02-10 14:30:55','2019-02-10 14:32:53',1549825107,'iris.csv','FINISH','CLASSIFICATION','-'),(1549827332,'22','224','2019-02-10 14:35:32','2019-02-10 14:35:55',1549825107,'irisCluster.csv','FINISH','PREDICTION','-'),(1549906626,'Create clustering antigen by frequence','Create clustering frequence','2019-02-11 12:37:06','2019-02-11 12:42:20',1547293936,'dataSetFrequence.csv','ERROR','CLUSTERING-FULL','-'),(1549906981,'Testing K-Means','Testing','2019-02-11 12:43:01','2019-02-11 12:43:02',1547293936,'dataSetFrequence.csv','FINISH','CLUSTERING K-MEANS','-'),(1549907015,'123','123','2019-02-11 12:43:35','2019-02-11 12:44:19',1547293936,'dataSetFrequence.csv','FINISH','CLUSTERING AFFINITY PROPAGATION','-'),(1549907228,'123','123','2019-02-11 12:47:08','2019-02-11 12:47:13',1547293936,'dataSetFrequence.csv','FINISH','CLUSTERING MEAN-SHIFT','-'),(1549907259,'123','123','2019-02-11 12:47:39','2019-02-11 12:47:41',1547293936,'dataSetFrequence.csv','FINISH','CLUSTERING DBScan','-'),(1549907355,'123','123','2019-02-11 12:49:15','2019-02-11 12:49:19',1547293936,'dataSetFrequence.csv','FINISH','CLUSTERING K-MEANS','-'),(1549907413,'123','123','2019-02-11 12:50:13','2019-02-11 13:14:02',1547293936,'dataSetFrequence.csv','FINISH','CLUSTERING-FULL','-'),(1549921062,'1BNI','1BNI','2019-02-11 16:37:42','2019-02-11 16:37:42',1547293936,'1BNI.csv','FINISH','FREQUENCE','-'),(1549921315,'1STN','1STN','2019-02-11 16:41:55','2019-02-11 16:41:55',1547293936,'1STN.csv','FINISH','FREQUENCE','-'),(1549921371,'1STN','1STN','2019-02-11 16:42:51','2019-02-11 16:42:51',1547293936,'1STN.csv','FINISH','FREQUENCE','-'),(1549921495,'2LZM','2LZM','2019-02-11 16:44:55','2019-02-11 16:44:55',1547293936,'2LZM.csv','FINISH','FREQUENCE','-'),(1549921563,'2RN2','2RN2','2019-02-11 16:46:03','2019-02-11 16:46:03',1547293936,'2RN2.csv','FINISH','FREQUENCE','-'),(1549921664,'2RN2','2RN2','2019-02-11 16:47:44','2019-02-11 16:47:44',1547293936,'2RN2.csv','FINISH','FREQUENCE','-');
/*!40000 ALTER TABLE `job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobUsedataSet`
--

DROP TABLE IF EXISTS `jobUsedataSet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobUsedataSet` (
  `job` int(11) NOT NULL,
  `dataSet` int(11) NOT NULL,
  PRIMARY KEY (`job`,`dataSet`),
  KEY `fk_job_has_dataSet_dataSet1_idx` (`dataSet`),
  KEY `fk_job_has_dataSet_job1_idx` (`job`),
  CONSTRAINT `fk_job_has_dataSet_dataSet1` FOREIGN KEY (`dataSet`) REFERENCES `dataSet` (`iddataSet`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_job_has_dataSet_job1` FOREIGN KEY (`job`) REFERENCES `job` (`idjob`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobUsedataSet`
--

LOCK TABLES `jobUsedataSet` WRITE;
/*!40000 ALTER TABLE `jobUsedataSet` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobUsedataSet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `iduser` int(11) NOT NULL AUTO_INCREMENT,
  `nameUser` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `emailUser` varchar(45) NOT NULL,
  `statusUser` varchar(45) NOT NULL,
  `createdUser` datetime NOT NULL,
  `modifiedUser` datetime NOT NULL,
  `institution` int(11) NOT NULL,
  `fullName` varchar(450) NOT NULL,
  PRIMARY KEY (`iduser`)
) ENGINE=InnoDB AUTO_INCREMENT=1549825108 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'demoUser','demo','david.medina@cebib.cl','ACCEPTED','2018-11-11 12:24:01','2019-02-10 00:26:25',1,'Full Name Demo'),(1547293936,'dmedina','123ewq','david.medina@cebib.cl','ACCEPTED','2019-01-12 08:52:16','2019-02-10 10:52:45',1,'David Medina'),(1547294173,'dinostroza','12367895','diego.inos@hotmail.com','WAITING','2019-01-12 08:56:13','2019-01-12 08:56:13',1547294173,'Diego Inostroza'),(1549825107,'jose1','intruso','josemedinaortiz@hotmail.com','ACCEPTED','2019-02-10 13:58:27','2019-02-10 13:59:02',1549825107,'jose miguel medina ortiz');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-02-11 17:30:40
