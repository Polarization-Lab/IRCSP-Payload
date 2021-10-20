/*
*********************************************************************
*********************************************************************
Name: IRCSP Balloon Data 
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`SalterFlight` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `SalterFlight`;

/*Table structure for table `customers` */

DROP TABLE IF EXISTS `log`;

CREATE TABLE `log` (
  `measurementID` int(11) NOT NULL,
  `housingTemp` decimal(10,2) NOT NULL,
  `camera1Temp` decimal(10,2) NOT NULL,
  `camera2Temp` decimal(10,2) NOT NULL,
  `pressure` decimal(10,2) NOT NULL,
  `altitude` decimal(10,2) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `humidity` decimal(10,2) NOT NULL,
  `acceleration` decimal(10,2) NOT NULL,
  
  
  PRIMARY KEY (`measurementID`),
  KEY `salesRepEmployeeNumber` (`salesRepEmployeeNumber`),
  CONSTRAINT `log_ibfk_1` FOREIGN KEY (`salesRepEmployeeNumber`) REFERENCES `employees` (`employeeNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;