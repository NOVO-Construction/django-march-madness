# ************************************************************
# Sequel Pro SQL dump
# Version 4096
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: 127.0.0.1 (MySQL 5.6.19)
# Database: djagno-march-madness
# Generation Time: 2015-03-16 18:52:35 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table madness_bracket
# ------------------------------------------------------------

DROP TABLE IF EXISTS `madness_bracket`;

CREATE TABLE `madness_bracket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` int(11) NOT NULL,
  `seed` int(11) NOT NULL,
  `region_id` int(11) NOT NULL,
  `team_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `madness_bracket_0f442f96` (`region_id`),
  KEY `madness_bracket_f6a7ca40` (`team_id`),
  CONSTRAINT `madness_bracket_team_id_34b2de533f5c900_fk_madness_team_id` FOREIGN KEY (`team_id`) REFERENCES `madness_team` (`id`),
  CONSTRAINT `madness_bracket_region_id_69167dc08aa13961_fk_madness_region_id` FOREIGN KEY (`region_id`) REFERENCES `madness_region` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `madness_bracket` WRITE;
/*!40000 ALTER TABLE `madness_bracket` DISABLE KEYS */;

INSERT INTO `madness_bracket` (`id`, `year`, `seed`, `region_id`, `team_id`)
VALUES
	(1,2015,1,1,1),
	(2,2015,16,1,2),
	(3,2015,8,1,3),
	(4,2015,9,1,4),
	(5,2015,5,1,5),
	(6,2015,12,1,6),
	(7,2015,4,1,7),
	(8,2015,13,1,8),
	(9,2015,6,1,9),
	(10,2015,11,1,10),
	(11,2015,3,1,11),
	(12,2015,14,1,12),
	(13,2015,7,1,13),
	(14,2015,10,1,14),
	(15,2015,2,1,15),
	(16,2015,15,1,16),
	(17,2015,1,2,17),
	(18,2015,16,2,18),
	(19,2015,8,2,19),
	(20,2015,9,2,20),
	(21,2015,5,2,21),
	(22,2015,12,2,22),
	(23,2015,4,2,23),
	(24,2015,12,2,24),
	(25,2015,6,2,25),
	(26,2015,11,2,26),
	(27,2015,3,2,27),
	(28,2015,14,2,28),
	(29,2015,7,2,29),
	(30,2015,10,2,30),
	(31,2015,2,2,31),
	(32,2015,15,2,32),
	(33,2015,1,3,33),
	(34,2015,16,3,34),
	(35,2015,8,3,35),
	(36,2015,9,3,36),
	(37,2015,5,3,37),
	(38,2015,12,3,38),
	(39,2015,4,3,39),
	(40,2015,13,3,40),
	(41,2015,6,3,41),
	(42,2015,11,3,42),
	(43,2015,3,3,43),
	(44,2015,14,3,44),
	(45,2015,7,3,45),
	(46,2015,10,3,46),
	(47,2015,2,3,47),
	(48,2015,15,3,48),
	(49,2015,1,4,49),
	(50,2015,16,4,50),
	(51,2015,8,4,51),
	(52,2015,9,4,52),
	(53,2015,5,4,53),
	(54,2015,12,4,54),
	(55,2015,4,4,55),
	(56,2015,13,4,56),
	(57,2015,6,4,57),
	(58,2015,11,4,58),
	(59,2015,3,4,59),
	(60,2015,14,4,60),
	(61,2015,7,4,61),
	(62,2015,10,4,62),
	(63,2015,2,4,63),
	(64,2015,15,4,64);

/*!40000 ALTER TABLE `madness_bracket` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table madness_region
# ------------------------------------------------------------

DROP TABLE IF EXISTS `madness_region`;

CREATE TABLE `madness_region` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `grid` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `madness_region` WRITE;
/*!40000 ALTER TABLE `madness_region` DISABLE KEYS */;

INSERT INTO `madness_region` (`id`, `name`, `grid`)
VALUES
	(1,'Midwest',1),
	(2,'West',2),
	(3,'East',3),
	(4,'South',4);

/*!40000 ALTER TABLE `madness_region` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table madness_team
# ------------------------------------------------------------

DROP TABLE IF EXISTS `madness_team`;

CREATE TABLE `madness_team` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `mascot` varchar(100) NOT NULL,
  `abbreviation` varchar(4) NOT NULL,
  `score_link_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `madness_team_bc2289b2` (`score_link_id`),
  CONSTRAINT `madness_t_score_link_id_77e78ab6eb886e30_fk_madness_scorelink_id` FOREIGN KEY (`score_link_id`) REFERENCES `madness_scorelink` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `madness_team` WRITE;
/*!40000 ALTER TABLE `madness_team` DISABLE KEYS */;

INSERT INTO `madness_team` (`id`, `name`, `mascot`, `abbreviation`, `score_link_id`)
VALUES
	(1,'Kentucky','Wildcats','UK',NULL),
	(2,'Play-in #16 Midwest','Yeah','PIM',NULL),
	(3,'Cincinatti','Bearcats','CIN',NULL),
	(4,'Purdue','Boilermakers','PUR',NULL),
	(5,'West Virginia','Mountaineers','WVU',NULL),
	(6,'Buffalo','Bulls','BUFF',NULL),
	(7,'Maryland','Terrapins','MARY',NULL),
	(8,'Valparaiso','Crusaders','VAL',NULL),
	(9,'Butler','Bulldogs','BUTL',NULL),
	(10,'Texas','Longhorns','UT',NULL),
	(11,'Notre Dame','Fighting Irish','ND',NULL),
	(12,'Northeastern','Huskies','NEU',NULL),
	(13,'Wichita State','Shockers','WSU',NULL),
	(14,'Indiana','Hoosiers','IU',NULL),
	(15,'Kansas','Jayhawks','KU',NULL),
	(16,'New Mexico State','Aggies','NMSU',NULL),
	(17,'Wisconsin','Badgers','WISC',NULL),
	(18,'Coastal Carolina','Chanticleers','CCU',NULL),
	(19,'Oregon','Ducks','ORE',NULL),
	(20,'Oklahoma State','Cowboys','OSU',NULL),
	(21,'Arkansas','Razorbacks','ARK',NULL),
	(22,'Wofford','Terriers','WOFF',NULL),
	(23,'North Carolina','Tarheels','UNC',NULL),
	(24,'Harvard','Crimson','HARV',NULL),
	(25,'Xavier','Musketeers','XAV',NULL),
	(26,'Play-in #11 West','Yeah','PIW',NULL),
	(27,'Baylor','Bears','BAY',NULL),
	(28,'Georgia State','Panthers','GSU',NULL),
	(29,'Virgina Commonwealth','Rams','VCU',NULL),
	(30,'Ohio State','Buckeyes','OSU',NULL),
	(31,'Arizona','Wildcats','ARIZ',NULL),
	(32,'Texas Southern','Tigers','TSU',NULL),
	(33,'Villanova','Wildcats','NOVA',NULL),
	(34,'Lafayette','Leopards','LAF',NULL),
	(35,'North Carolina State','Wolfpack','NCSU',NULL),
	(36,'Louisiana State','Tigers','LSU',NULL),
	(37,'Northern Iowa','Panthers','UNI',NULL),
	(38,'Wyoming','Cowboys','WYO',NULL),
	(39,'Louisville','Cardinals','LOU',NULL),
	(40,'UC Irvine','Anteaters','UCI',NULL),
	(41,'Providence','Friars','PROV',NULL),
	(42,'Play-in #11 East','Yeah','PIE',NULL),
	(43,'Oklahoma','Sooners','OKLA',NULL),
	(44,'Albany','Great Danes','ALB',NULL),
	(45,'Michigan State','Spartans','MSU',NULL),
	(46,'Georgia','Bulldogs','UGA',NULL),
	(47,'Virgina','Cavaliers','UVA',NULL),
	(48,'Belmont','Bears','BEL',NULL),
	(49,'Duke','Blue Devils','DUKE',NULL),
	(50,'Play-in #16 South','Yeah','PIS',NULL),
	(51,'San Diego State','Aztecs','SDSU',NULL),
	(52,'St. John\'s','Red Storm','SJU',NULL),
	(53,'Utah','Utes','UTAH',NULL),
	(54,'Stephen F. Austin','Lumberjacks','SFU',NULL),
	(55,'Georgetown','Hoyas','GEO',NULL),
	(56,'Eastern Washington','Eagles','EWU',NULL),
	(57,'Southern Methodist','Mustangs','SMU',NULL),
	(58,'UCLA','Bruins','UCLA',NULL),
	(59,'Iowa St','Cyclones','ISU',NULL),
	(60,'UAB','Blazers','UAB',NULL),
	(61,'Iowa','Hawkeyes','IOWA',NULL),
	(62,'Davidson','Wildcats','DAV',NULL),
	(63,'Gonzaga','Bulldogs','ZAGS',NULL),
	(64,'North Dakota State','Bison','NDSU',NULL);

/*!40000 ALTER TABLE `madness_team` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
