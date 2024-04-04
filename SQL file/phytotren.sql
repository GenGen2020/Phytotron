/*
Navicat MySQL Data Transfer

Source Server         : test
Source Server Version : 50726
Source Host           : 127.0.0.1:3306
Source Database       : phytotren

Target Server Type    : MYSQL
Target Server Version : 50726
File Encoding         : 65001

Date: 2024-03-30 15:13:09
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('5', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can view permission', '2', 'view_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can view group', '3', 'view_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '4', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '4', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '4', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can view content type', '4', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('17', 'Can add session', '5', 'add_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can change session', '5', 'change_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete session', '5', 'delete_session');
INSERT INTO `auth_permission` VALUES ('20', 'Can view session', '5', 'view_session');
INSERT INTO `auth_permission` VALUES ('21', 'Can add account management', '6', 'add_customuser');
INSERT INTO `auth_permission` VALUES ('22', 'Can change account management', '6', 'change_customuser');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete account management', '6', 'delete_customuser');
INSERT INTO `auth_permission` VALUES ('24', 'Can view account management', '6', 'view_customuser');
INSERT INTO `auth_permission` VALUES ('25', 'Can add research request', '7', 'add_researchrequest');
INSERT INTO `auth_permission` VALUES ('26', 'Can change research request', '7', 'change_researchrequest');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete research request', '7', 'delete_researchrequest');
INSERT INTO `auth_permission` VALUES ('28', 'Can view research request', '7', 'view_researchrequest');
INSERT INTO `auth_permission` VALUES ('29', 'Can add bill', '8', 'add_bill');
INSERT INTO `auth_permission` VALUES ('30', 'Can change bill', '8', 'change_bill');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete bill', '8', 'delete_bill');
INSERT INTO `auth_permission` VALUES ('32', 'Can view bill', '8', 'view_bill');
INSERT INTO `auth_permission` VALUES ('33', 'Can add price', '9', 'add_price');
INSERT INTO `auth_permission` VALUES ('34', 'Can change price', '9', 'change_price');
INSERT INTO `auth_permission` VALUES ('35', 'Can delete price', '9', 'delete_price');
INSERT INTO `auth_permission` VALUES ('36', 'Can view price', '9', 'view_price');
INSERT INTO `auth_permission` VALUES ('37', 'Can add bill detail', '10', 'add_billdetail');
INSERT INTO `auth_permission` VALUES ('38', 'Can change bill detail', '10', 'change_billdetail');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete bill detail', '10', 'delete_billdetail');
INSERT INTO `auth_permission` VALUES ('40', 'Can view bill detail', '10', 'view_billdetail');
INSERT INTO `auth_permission` VALUES ('41', 'Can add order', '11', 'add_order');
INSERT INTO `auth_permission` VALUES ('42', 'Can change order', '11', 'change_order');
INSERT INTO `auth_permission` VALUES ('43', 'Can delete order', '11', 'delete_order');
INSERT INTO `auth_permission` VALUES ('44', 'Can view order', '11', 'view_order');
INSERT INTO `auth_permission` VALUES ('45', 'Can add order detail', '12', 'add_orderdetail');
INSERT INTO `auth_permission` VALUES ('46', 'Can change order detail', '12', 'change_orderdetail');
INSERT INTO `auth_permission` VALUES ('47', 'Can delete order detail', '12', 'delete_orderdetail');
INSERT INTO `auth_permission` VALUES ('48', 'Can view order detail', '12', 'view_orderdetail');

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=47 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('8', '2024-03-14 02:55:39.087852', '2', 'zhangsan', '2', '[]', '6', '3');
INSERT INTO `django_admin_log` VALUES ('13', '2024-03-28 15:45:30.530469', '5', '11111111111', '3', '', '7', '3');
INSERT INTO `django_admin_log` VALUES ('11', '2024-03-28 13:42:30.632939', '1', '1', '3', '', '7', '3');
INSERT INTO `django_admin_log` VALUES ('12', '2024-03-28 15:45:30.529451', '6', '11111111', '3', '', '7', '3');
INSERT INTO `django_admin_log` VALUES ('10', '2024-03-28 13:37:40.364437', '4', '1', '3', '', '7', '3');
INSERT INTO `django_admin_log` VALUES ('9', '2024-03-18 01:47:11.170751', '2', 'zhangsan', '3', '', '6', '3');
INSERT INTO `django_admin_log` VALUES ('14', '2024-03-28 15:45:30.531461', '3', '1', '3', '', '7', '3');
INSERT INTO `django_admin_log` VALUES ('15', '2024-03-28 15:45:30.532460', '2', '1', '3', '', '7', '3');
INSERT INTO `django_admin_log` VALUES ('16', '2024-03-29 01:51:41.883503', '1', 'Price: 11, Type: Greenhouse2', '1', '[{\"added\": {}}]', '9', '3');
INSERT INTO `django_admin_log` VALUES ('17', '2024-03-29 02:01:27.806772', '2147483647', 'Order Number: 2147483647, Date: 2024-03-29, Total Amount: 143.00', '2', '[{\"added\": {\"name\": \"order detail\", \"object\": \"Detail Number: 1, Price: 11.00, Type: None\"}}, {\"added\": {\"name\": \"order detail\", \"object\": \"Detail Number: 2, Price: 11.00, Type: None\"}}]', '11', '3');
INSERT INTO `django_admin_log` VALUES ('18', '2024-03-29 02:02:02.393074', '2147483647', 'Order Number: 2147483647, Date: 2024-03-29, Total Amount: 143.00', '3', '', '11', '3');
INSERT INTO `django_admin_log` VALUES ('19', '2024-03-29 02:07:03.642040', '11', '11111111111111111111111111', '2', '[{\"changed\": {\"fields\": [\"Email\", \"Approve status\"]}}]', '7', '3');
INSERT INTO `django_admin_log` VALUES ('20', '2024-03-29 02:08:44.418035', '28258352', 'Order Number: 28258352, Date: 2024-03-29, Total Amount: 11.00', '2', '[{\"added\": {\"name\": \"order detail\", \"object\": \"Detail Number: 3, Price: 11.00, Type: None\"}}]', '11', '3');
INSERT INTO `django_admin_log` VALUES ('21', '2024-03-29 02:08:53.403378', '28258352', 'Order Number: 28258352, Date: 2024-03-29, Total Amount: 11.00', '2', '[{\"added\": {\"name\": \"order detail\", \"object\": \"Detail Number: 4, Price: 11.00, Type: None\"}}]', '11', '3');
INSERT INTO `django_admin_log` VALUES ('22', '2024-03-29 02:10:11.998768', '28258352', 'Order Number: 28258352, Date: 2024-03-29, Total Amount: 11.00', '2', '[{\"deleted\": {\"name\": \"order detail\", \"object\": \"Detail Number: 3, Price: 11.00, Type: None\"}}]', '11', '3');
INSERT INTO `django_admin_log` VALUES ('23', '2024-03-29 02:10:40.746653', '28258352', 'Order Number: 28258352, Date: 2024-03-29, Total Amount: 11.00', '2', '[{\"deleted\": {\"name\": \"order detail\", \"object\": \"Detail Number: 3, Price: 11.00, Type: None\"}}, {\"deleted\": {\"name\": \"order detail\", \"object\": \"Detail Number: 4, Price: 11.00, Type: None\"}}]', '11', '3');
INSERT INTO `django_admin_log` VALUES ('24', '2024-03-29 02:10:49.592662', '28258352', 'Order Number: 28258352, Date: 2024-03-29, Total Amount: 33.00', '2', '[{\"added\": {\"name\": \"order detail\", \"object\": \"Detail Number: 5, Price: 11.00, Type: None\"}}, {\"added\": {\"name\": \"order detail\", \"object\": \"Detail Number: 6, Price: 11.00, Type: None\"}}]', '11', '3');
INSERT INTO `django_admin_log` VALUES ('25', '2024-03-29 02:11:21.244428', '28258352', 'Order Number: 28258352, Date: 2024-03-29, Total Amount: 33.00', '3', '', '11', '3');
INSERT INTO `django_admin_log` VALUES ('26', '2024-03-29 02:11:42.516251', '28258352', 'Order Number: 28258352, Date: 2024-03-29, Total Amount: 33.00', '3', '', '11', '3');
INSERT INTO `django_admin_log` VALUES ('27', '2024-03-29 02:14:46.870674', '11', '11111111111111111111111111', '2', '[{\"changed\": {\"fields\": [\"Approve status\"]}}]', '7', '3');
INSERT INTO `django_admin_log` VALUES ('28', '2024-03-29 02:15:02.889127', '90261326', 'Order Number: 90261326, Date: 2024-03-29, Total Amount: 165.00', '2', '[{\"added\": {\"name\": \"order detail\", \"object\": \"Detail Number: 7, Price: 11.00, Type: None\"}}, {\"added\": {\"name\": \"order detail\", \"object\": \"Detail Number: 8, Price: 11.00, Type: None\"}}]', '11', '3');
INSERT INTO `django_admin_log` VALUES ('29', '2024-03-29 02:15:47.524013', '1', 'Price: 11.00, Type: Greenhouse2', '3', '', '9', '3');
INSERT INTO `django_admin_log` VALUES ('30', '2024-03-29 02:16:52.118514', '11', '11111111111111111111111111', '2', '[{\"changed\": {\"fields\": [\"Approve status\"]}}]', '7', '3');
INSERT INTO `django_admin_log` VALUES ('31', '2024-03-29 02:17:31.389462', '2', 'Price: 11, Type: Greenhouse2', '1', '[{\"added\": {}}]', '9', '3');
INSERT INTO `django_admin_log` VALUES ('32', '2024-03-29 02:17:43.232332', '90261326', 'Order Number: 90261326, Date: 2024-03-29, Total Amount: 176.00', '2', '[{\"added\": {\"name\": \"order detail\", \"object\": \"Detail Number: 9, Price: 11.00, Type: None\"}}]', '11', '3');
INSERT INTO `django_admin_log` VALUES ('33', '2024-03-29 02:17:53.995263', '90261326', 'Order Number: 90261326, Date: 2024-03-29, Total Amount: 176.00', '2', '[{\"deleted\": {\"name\": \"order detail\", \"object\": \"Detail Number: 9, Price: 11.00, Type: None\"}}]', '11', '3');
INSERT INTO `django_admin_log` VALUES ('34', '2024-03-29 02:18:18.827743', '90261326', 'Order Number: 90261326, Date: 2024-03-29, Total Amount: 176.00', '2', '[{\"deleted\": {\"name\": \"order detail\", \"object\": \"Detail Number: 9, Price: 11.00, Type: None\"}}]', '11', '3');
INSERT INTO `django_admin_log` VALUES ('35', '2024-03-29 02:34:45.554367', '90261326', 'Order Number: 90261326, Date: 2024-03-29, Total Amount: 165.00', '2', '[{\"deleted\": {\"name\": \"order detail\", \"object\": \"Detail Number: None, Price: 11.00, Type: None\"}}]', '11', '3');
INSERT INTO `django_admin_log` VALUES ('36', '2024-03-29 02:34:58.353395', '90261326', 'Order Number: 90261326, Date: 2024-03-29, Total Amount: 176.00', '2', '[{\"added\": {\"name\": \"order detail\", \"object\": \"Detail Number: 10, Price: 11.00, Type: None\"}}]', '11', '3');
INSERT INTO `django_admin_log` VALUES ('37', '2024-03-29 02:35:03.964694', '90261326', 'Order Number: 90261326, Date: 2024-03-29, Total Amount: 165.00', '2', '[{\"deleted\": {\"name\": \"order detail\", \"object\": \"Detail Number: None, Price: 11.00, Type: None\"}}]', '11', '3');
INSERT INTO `django_admin_log` VALUES ('38', '2024-03-29 02:35:09.630924', '90261326', 'Order Number: 90261326, Date: 2024-03-29, Total Amount: 176.00', '2', '[{\"added\": {\"name\": \"order detail\", \"object\": \"Detail Number: 11, Price: 11.00, Type: None\"}}]', '11', '3');
INSERT INTO `django_admin_log` VALUES ('39', '2024-03-29 02:35:14.629745', '90261326', 'Order Number: 90261326, Date: 2024-03-29, Total Amount: 165.00', '2', '[{\"deleted\": {\"name\": \"order detail\", \"object\": \"Detail Number: None, Price: 11.00, Type: None\"}}]', '11', '3');
INSERT INTO `django_admin_log` VALUES ('40', '2024-03-29 06:58:29.032268', '2', 'Price: 11.00, External Price: 13.00, Type: Greenhouse2', '2', '[{\"changed\": {\"fields\": [\"External price\"]}}]', '9', '3');
INSERT INTO `django_admin_log` VALUES ('41', '2024-03-29 07:03:17.331422', '11', '11111111111111111111111111', '2', '[{\"changed\": {\"fields\": [\"Approve status\"]}}]', '7', '3');
INSERT INTO `django_admin_log` VALUES ('42', '2024-03-29 07:05:12.671921', '90261326', 'Order Number: 90261326, Date: 2024-03-29, Total Amount: 165.00', '3', '', '11', '3');
INSERT INTO `django_admin_log` VALUES ('43', '2024-03-29 07:05:21.633172', '11', '11111111111111111111111111', '2', '[{\"changed\": {\"fields\": [\"Approve status\"]}}]', '7', '3');
INSERT INTO `django_admin_log` VALUES ('44', '2024-03-29 07:07:24.195807', '462843', 'Order Number: 462843, Date: 2024-03-29, Total Amount: 169.00', '3', '', '11', '3');
INSERT INTO `django_admin_log` VALUES ('45', '2024-03-29 07:08:38.718283', '94581504', 'Order Number: 94581504, Date: 2024-03-29, Total Amount: 169.00', '3', '', '11', '3');
INSERT INTO `django_admin_log` VALUES ('46', '2024-03-29 07:08:38.719282', '25931626', 'Order Number: 25931626, Date: 2024-03-29, Total Amount: 169.00', '3', '', '11', '3');

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('4', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('5', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('6', 'users', 'customuser');
INSERT INTO `django_content_type` VALUES ('7', 'users', 'researchrequest');
INSERT INTO `django_content_type` VALUES ('8', 'users', 'bill');
INSERT INTO `django_content_type` VALUES ('9', 'users', 'price');
INSERT INTO `django_content_type` VALUES ('10', 'users', 'billdetail');
INSERT INTO `django_content_type` VALUES ('11', 'users', 'order');
INSERT INTO `django_content_type` VALUES ('12', 'users', 'orderdetail');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2024-03-13 06:16:00.208244');
INSERT INTO `django_migrations` VALUES ('2', 'contenttypes', '0002_remove_content_type_name', '2024-03-13 06:16:00.256844');
INSERT INTO `django_migrations` VALUES ('3', 'auth', '0001_initial', '2024-03-13 06:16:00.496845');
INSERT INTO `django_migrations` VALUES ('4', 'auth', '0002_alter_permission_name_max_length', '2024-03-13 06:16:00.531120');
INSERT INTO `django_migrations` VALUES ('5', 'auth', '0003_alter_user_email_max_length', '2024-03-13 06:16:00.538960');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0004_alter_user_username_opts', '2024-03-13 06:16:00.545540');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0005_alter_user_last_login_null', '2024-03-13 06:16:00.556015');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0006_require_contenttypes_0002', '2024-03-13 06:16:00.558011');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0007_alter_validators_add_error_messages', '2024-03-13 06:16:00.564366');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0008_alter_user_username_max_length', '2024-03-13 06:16:00.569100');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0009_alter_user_last_name_max_length', '2024-03-13 06:16:00.576045');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0010_alter_group_name_max_length', '2024-03-13 06:16:00.617603');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0011_update_proxy_permissions', '2024-03-13 06:16:00.626191');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0012_alter_user_first_name_max_length', '2024-03-13 06:16:00.636163');
INSERT INTO `django_migrations` VALUES ('15', 'users', '0001_initial', '2024-03-13 06:16:00.938930');
INSERT INTO `django_migrations` VALUES ('16', 'admin', '0001_initial', '2024-03-13 06:16:01.065459');
INSERT INTO `django_migrations` VALUES ('17', 'admin', '0002_logentry_remove_auto_add', '2024-03-13 06:16:01.075519');
INSERT INTO `django_migrations` VALUES ('18', 'admin', '0003_logentry_add_action_flag_choices', '2024-03-13 06:16:01.084800');
INSERT INTO `django_migrations` VALUES ('19', 'sessions', '0001_initial', '2024-03-13 06:16:01.110968');
INSERT INTO `django_migrations` VALUES ('20', 'users', '0002_alter_customuser_options_customuser_approved_and_more', '2024-03-13 06:16:02.489215');
INSERT INTO `django_migrations` VALUES ('21', 'users', '0003_researchrequest', '2024-03-13 07:51:31.865928');
INSERT INTO `django_migrations` VALUES ('22', 'users', '0004_alter_customuser_role_and_more', '2024-03-13 09:16:25.721793');
INSERT INTO `django_migrations` VALUES ('23', 'users', '0005_customuser_avatar', '2024-03-14 01:27:19.075513');
INSERT INTO `django_migrations` VALUES ('24', 'users', '0006_customuser_personal_signature', '2024-03-14 01:51:06.603659');
INSERT INTO `django_migrations` VALUES ('25', 'users', '0007_customuser_telephone', '2024-03-14 01:54:10.347731');
INSERT INTO `django_migrations` VALUES ('26', 'users', '0008_alter_customuser_avatar', '2024-03-14 02:13:14.078717');
INSERT INTO `django_migrations` VALUES ('27', 'users', '0009_researchrequest_approved_alter_customuser_avatar', '2024-03-14 03:47:06.086268');
INSERT INTO `django_migrations` VALUES ('28', 'users', '0010_researchrequest_price_alter_customuser_avatar', '2024-03-28 09:38:52.865262');
INSERT INTO `django_migrations` VALUES ('29', 'users', '0011_researchrequest_bench', '2024-03-28 14:00:39.470447');
INSERT INTO `django_migrations` VALUES ('30', 'users', '0012_researchrequest_is_active', '2024-03-28 14:17:19.975100');
INSERT INTO `django_migrations` VALUES ('31', 'users', '0013_customuser_supervisor', '2024-03-28 15:00:07.734197');
INSERT INTO `django_migrations` VALUES ('32', 'users', '0014_customuser_queen', '2024-03-28 15:04:28.614163');
INSERT INTO `django_migrations` VALUES ('33', 'users', '0015_bill_price_billdetail', '2024-03-29 01:10:59.823466');
INSERT INTO `django_migrations` VALUES ('34', 'users', '0016_remove_billdetail_bill_remove_billdetail_price_order_and_more', '2024-03-29 01:15:53.767048');
INSERT INTO `django_migrations` VALUES ('35', 'users', '0017_remove_researchrequest_price', '2024-03-29 01:27:18.800742');
INSERT INTO `django_migrations` VALUES ('36', 'users', '0018_order_basic_billing_fee', '2024-03-29 03:50:05.256382');
INSERT INTO `django_migrations` VALUES ('37', 'users', '0019_price_external_price', '2024-03-29 06:57:34.820266');
INSERT INTO `django_migrations` VALUES ('38', 'users', '0020_order_attachment_order_is_completed', '2024-03-29 09:00:36.618394');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('h57vh27h5jqcqbbkerk0hqx23dkoog9c', '.eJytkjtzgzAQhP8Ko9oG8TAGd06TKqWr4PGcHgYlIGUk0cTDfw9nXMQkzjiZdJrdT4v2jhM5QO-bQ--kPShBNiQhi88aA_4qNRriBXRtQm60t4qFiIQX14VPRsj24cJeBTTgGrzNaAF5WfAjFHJNGRMyoyJfpWVSZBkrJayZTBlb50laUk7pKs4SiEWc8BwykWFoJ3XvxqznU0U0dLIim6Ai2_FTUnvFwSujA9AiQMlY9X5WKrIYKcXxhPwRXHCEpWuUbMUSWj8BHTZwiFzHP1rTv7kbIdjQLbmpJ7-37WRHIDqlI5xCVGNANAEgxO42M7oXjlkJgtu-Y9-86B8KD4vgTyWHPRJSCQRiSpO5EM-Td3j5a7DFYK4sb-XP499ybnrtgw401HL8A_wdYfM9nBtEvHfedHi-vY0v5J07uafmfDS_rjYfdjYX0mFPhg8bcjyj:1rkaTS:a-da1fJCXLNk_8i-lTEByjLyDkuGSB9pP9vX50oXvHs', '2024-03-28 02:05:38.850122');
INSERT INTO `django_session` VALUES ('ognk0thd4553x603txv2y25ap6zs2ahf', '.eJytkjtzgzAQhP8Ko9oG8TAGd06TKqWr4PGcHgYlIGUk0cTDfw9nXMQkzjiZdJrdT4v2jhM5QO-bQ--kPShBNiQhi88aA_4qNRriBXRtQm60t4qFiIQX14VPRsj24cJeBTTgGrzNaAF5WfAjFHJNGRMyoyJfpWVSZBkrJayZTBlb50laUk7pKs4SiEWc8BwykWFoJ3XvxqznU0U0dLIim6Ai2_FTUnvFwSujA9AiQMlY9X5WKrIYKcXxhPwRXHCEpWuUbMUSWj8BHTZwiFzHP1rTv7kbIdjQLbmpJ7-37WRHIDqlI5xCVGNANAEgxO42M7oXjlkJgtu-Y9-86B8KD4vgTyWHPRJSCQRiSpO5EM-Td3j5a7DFYK4sb-XP499ybnrtgw401HL8A_wdYfM9nBtEvHfedHi-vY0v5J07uafmfDS_rjYfdjYX0mFPhg8bcjyj:1rkbAl:_xrf4fDoL1fYTbrblVrShw8irpj3EmuleS_cp4PyEEc', '2024-03-28 02:50:23.113385');
INSERT INTO `django_session` VALUES ('hlj4p3tg3gktaxq0eijku8kies1ld3j4', '.eJytkjtvgzAUhf8K8pyAY4dHsqVLp46ZShRdbANuwa78WBrx34tDhoY2VVp1wjrn84FzLyd0BO_ao7fCHCVHW0TR4rNWAXsVKhj8BVSjY6aVM7KKAxJfXBs_aS66hwt7FdCCbcfbmOSC0mydFyQlFcUUINtkdVplNCcwPmqaplnKsOAEEy6KTZEJQaoiZ6TAGQ6hvVDejlnPpxIp6EWJtlGJduOrhHKSgZNaRaB4FCRt5PtZKdFipCQLp8DXYKMalraVouNL6NwE9KGBDch1_KPR_s3eCAkN7ZLpZvK96SY7Ad5LlYQpJE0ISCYAON_fZkb3wlVGAGfG99U3X_QPhYdF9KeSwyEQQvIArDAmc2E1T96Hy1-DTQhm0rBO_Dz-HWPaKxf1oKAR4x_g7gib7-HcIGHeOt2H8-1tfCHv3Mk9Neej-XW1-bDXc4EOBzR8APvfO2s:1rkbGU:WTOQ0tPQFjFMJR6TWu_zTmc5H40StpHzP6kLToh4Ho8', '2024-03-28 02:56:18.072265');
INSERT INTO `django_session` VALUES ('79s8xbdv5cycnx1cidwq55v7e34gudt9', '.eJy1ks1ygjAURl-FyVoFgyC6s5uuuumMq-o4l-QqaSFp87Op47uXKIsaa4uddgVz7-HA94U92YCz1cYZ1BvByZykZPB5VgJ7QekX_BnkTo2YklaLcuSRUbc1owfFsb7r2DNBBaZqn07oFNM0n0wLmtEyTVKAfJZvszJPpxTayzbNsjxjCXKaUI7FrMgRaVlMGS2SPPHSBqUzretpvyISGlyRebQii_ZVKK1gYIWSEUge-ZHS4v04WZFBSwnm7zy_BRNtYWgqgTUfQm1PQOMTGI-c6--1cq_misQnNEOmdqe90_VpHQNvhIx9C_HOC-ITAJwvrzPttuNKjcCZdk35xRf9QeDDIPpVyMPaEyi4B8ZJQsPBODQv_cOXYu3FTGhW4_f1LxhTTtqoAQk7bP8A20MWnsMxQcycsarx99dP44LseSZ9YobV3BwtLHsSGh_RIGhWRRrfHBrbp_ivu9KdqRP9VFiI_2Nrt2YMS8vCQXpYk8MHLxCg1Q:1rm3P8:BGWEaHpJrrkpVexRZY2Pj8vLlCmtnZegB-j08FD2sX0', '2024-04-01 03:11:14.349194');
INSERT INTO `django_session` VALUES ('jc5384hmz49o4wolrcsm6rme09wmpky9', '.eJy1ks1ygjAURl-FyVoFgyC6s5uuuumMq-o4l-QqaSFp87Op47uXKIsaa4uddgVz7-HA94U92YCz1cYZ1BvByZykZPB5VgJ7QekX_BnkTo2YklaLcuSRUbc1owfFsb7r2DNBBaZqn07oFNM0n0wLmtEyTVKAfJZvszJPpxTayzbNsjxjCXKaUI7FrMgRaVlMGS2SPPHSBqUzretpvyISGlyRebQii_ZVKK1gYIWSEUge-ZHS4v04WZFBSwnm7zy_BRNtYWgqgTUfQm1PQOMTGI-c6--1cq_misQnNEOmdqe90_VpHQNvhIx9C_HOC-ITAJwvrzPttuNKjcCZdk35xRf9QeDDIPpVyMPaEyi4B8ZJQsPBODQv_cOXYu3FTGhW4_f1LxhTTtqoAQk7bP8A20MWnsMxQcycsarx99dP44LseSZ9YobV3BwtLHsSGh_RIGhWRRrfHBrbp_ivu9KdqRP9VFiI_2Nrt2YMS8vCQXpYk8MHLxCg1Q:1rmPSP:0saINvfFd4mu7eACp4CthjvXU8yPxUVHfxBZr3Oq6fo', '2024-04-02 02:44:05.394342');
INSERT INTO `django_session` VALUES ('1948n2jqhfvx9z325sql7xnupwle8bhy', '.eJy1ks1ygjAURl-FyVoFgyC6s5uuuumMq-o4l-QqaSFp87Op47uXKIsaa4uddgVz7-HA94U92YCz1cYZ1BvByZykZPB5VgJ7QekX_BnkTo2YklaLcuSRUbc1owfFsb7r2DNBBaZqn07oFNM0n0wLmtEyTVKAfJZvszJPpxTayzbNsjxjCXKaUI7FrMgRaVlMGS2SPPHSBqUzretpvyISGlyRebQii_ZVKK1gYIWSEUge-ZHS4v04WZFBSwnm7zy_BRNtYWgqgTUfQm1PQOMTGI-c6--1cq_misQnNEOmdqe90_VpHQNvhIx9C_HOC-ITAJwvrzPttuNKjcCZdk35xRf9QeDDIPpVyMPaEyi4B8ZJQsPBODQv_cOXYu3FTGhW4_f1LxhTTtqoAQk7bP8A20MWnsMxQcycsarx99dP44LseSZ9YobV3BwtLHsSGh_RIGhWRRrfHBrbp_ivu9KdqRP9VFiI_2Nrt2YMS8vCQXpYk8MHLxCg1Q:1rnCP3:sIk4r3N7FZmGh5HwFybgJGD5lv9tZsAe73aL1BdZYB4', '2024-04-04 06:59:53.190007');
INSERT INTO `django_session` VALUES ('j0w5t2awdzeazwdx8u40e8tz9mpkvo7k', '.eJy1kk1T2zAQhv-KR-ckNjL-gBu99NSBYYZTw2TW0iZWa0ugj0uZ_Pd6sQ9FEGIyzcme3VdP8j7yC9tA8O0mOLQbJdk1y9ni31kD4jdqWshfoHdmJYz2VjUriqymrVv9MBK7b1P2DaAF1w6nM15hnpeXVc0L3uRZDlBelduiKfOKw_DY5kVRFiJDyTMusb6qS0Te1JXgdVZmBO1RBzewfr6smYYe1-w6WbOb4adQeyXAK6MT0DKhkbHqz-tkzRZDSgl6o_wWXLKFpWsVdnIJnR8DPTVwFHmL_25NeHIHINTQLYXZjftgu3GdguyVTslCuiNAOgZAyofDmWE75RqLIIUNffPBP_oPhfeL5KSS-0dKoJIUuMgyHg8uYvIDHX4PtgQWyooOP9d_I4QJ2ic9aNjh8AX4GbD4Hl4bpCI4b3p6P3wb75Iz72ROzVjNl6vFsi9j4q2V82x_LMjQ8WNuxtAZtcwqEasoYsqdVQJPV_FEx4-pGENnVDGrRKyijCn36BCsaBOLzwGdP92KnUgT6JifOH5GU1_tGEur4kG-f2T7v8zqSUc:1rqQ3n:aooHdOPlZae2URqoFm7OuV29UiuZOnqfHC4Na3BJMKI', '2024-04-13 04:11:15.683000');
INSERT INTO `django_session` VALUES ('88j80hcxysi2h0dwpgqujc6sejfqikda', '.eJy1kk1T2zAQhv-KR-ckNjL-gBu99NSBYYZTw2TW0iZWa0ugj0uZ_Pd6sQ9FEGIyzcme3VdP8j7yC9tA8O0mOLQbJdk1y9ni31kD4jdqWshfoHdmJYz2VjUriqymrVv9MBK7b1P2DaAF1w6nM15hnpeXVc0L3uRZDlBelduiKfOKw_DY5kVRFiJDyTMusb6qS0Te1JXgdVZmBO1RBzewfr6smYYe1-w6WbOb4adQeyXAK6MT0DKhkbHqz-tkzRZDSgl6o_wWXLKFpWsVdnIJnR8DPTVwFHmL_25NeHIHINTQLYXZjftgu3GdguyVTslCuiNAOgZAyofDmWE75RqLIIUNffPBP_oPhfeL5KSS-0dKoJIUuMgyHg8uYvIDHX4PtgQWyooOP9d_I4QJ2ic9aNjh8AX4GbD4Hl4bpCI4b3p6P3wb75Iz72ROzVjNl6vFsi9j4q2V82x_LMjQ8WNuxtAZtcwqEasoYsqdVQJPV_FEx4-pGENnVDGrRKyijCn36BCsaBOLzwGdP92KnUgT6JifOH5GU1_tGEur4kG-f2T7v8zqSUc:1rqQas:-W_xAGjKFl-u_SQesGRIzDNePuzESP15lp62q1emb6I', '2024-04-13 04:45:26.048509');

-- ----------------------------
-- Table structure for users_customuser
-- ----------------------------
DROP TABLE IF EXISTS `users_customuser`;
CREATE TABLE `users_customuser` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `approved` int(11) NOT NULL,
  `role` int(11) NOT NULL,
  `avatar` varchar(100) DEFAULT NULL,
  `personal_signature` varchar(255) DEFAULT NULL,
  `telephone` varchar(20) DEFAULT NULL,
  `supervisor` varchar(255) NOT NULL,
  `queen` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_customuser_email_6445acef_uniq` (`email`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_customuser
-- ----------------------------
INSERT INTO `users_customuser` VALUES ('5', 'pbkdf2_sha256$720000$MVx0kUmXgg7nfklx1ZQcdA$Bh4Ypy/opvSjjJsvcbLynNK9qe9CtztK54BD9j6/wVc=', null, '0', 'lisi91a9', 'lisi', 'lisi', '563722648@qq.com', '0', '0', '2024-03-18 03:17:47.771023', '0', '0', 'users/static/avatars/photo-1587822463356-cd0b11a919ae.jpg', null, null, '', '0');
INSERT INTO `users_customuser` VALUES ('3', 'pbkdf2_sha256$720000$MhXWNq11DrVOmeIaNLAIOU$fSiP6YOTMMS1WNL5wYYB+QBMqIk/RlU7Cl8Niwvw9uE=', '2024-03-28 14:42:20.699154', '1', 'admin', '', '', 'zhangsan@126.com', '1', '1', '2024-03-14 02:54:29.622299', '0', '3', 'users/static/avatars/photo-1587822463356-cd0b11a919ae.jpg', 'be myself', '15621391234', 'wangwu', '0');
INSERT INTO `users_customuser` VALUES ('6', 'pbkdf2_sha256$720000$FmfNBhzWXwhv6ZeKzdv9HA$oAImjxkMHmWJBiZ6rjJrx/yO4DF9/Cff01pDMkWLN4k=', null, '0', 'zhangsanlisi5398', 'zhangsanlisi', 'wang', 'hdcyyg1@126.com', '0', '0', '2024-03-28 15:10:30.363209', '0', '1', 'users/static/avatars/photo-1587822463356-cd0b11a919ae.jpg', null, null, 'wangwu', '1');

-- ----------------------------
-- Table structure for users_customuser_groups
-- ----------------------------
DROP TABLE IF EXISTS `users_customuser_groups`;
CREATE TABLE `users_customuser_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_customuser_groups_customuser_id_group_id_76b619e3_uniq` (`customuser_id`,`group_id`),
  KEY `users_customuser_groups_customuser_id_958147bf` (`customuser_id`),
  KEY `users_customuser_groups_group_id_01390b14` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_customuser_groups
-- ----------------------------

-- ----------------------------
-- Table structure for users_customuser_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `users_customuser_user_permissions`;
CREATE TABLE `users_customuser_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_customuser_user_pe_customuser_id_permission_7a7debf6_uniq` (`customuser_id`,`permission_id`),
  KEY `users_customuser_user_permissions_customuser_id_5771478b` (`customuser_id`),
  KEY `users_customuser_user_permissions_permission_id_baaa2f74` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_customuser_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for users_order
-- ----------------------------
DROP TABLE IF EXISTS `users_order`;
CREATE TABLE `users_order` (
  `order_number` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `total_amount` decimal(10,2) NOT NULL,
  `research_request_id` bigint(20) NOT NULL,
  `basic_billing_fee` decimal(10,2) NOT NULL,
  `attachment` varchar(100) DEFAULT NULL,
  `is_completed` tinyint(1) NOT NULL,
  PRIMARY KEY (`order_number`),
  KEY `users_order_research_request_id_90b77867` (`research_request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2147483648 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_order
-- ----------------------------
INSERT INTO `users_order` VALUES ('2147483647', '2024-03-29', '169.00', '11', '169.00', 'users/static/pdfs/order_2147483647_cl2pInv.pdf', '0');

-- ----------------------------
-- Table structure for users_orderdetail
-- ----------------------------
DROP TABLE IF EXISTS `users_orderdetail`;
CREATE TABLE `users_orderdetail` (
  `detail_number` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(100) DEFAULT NULL,
  `order_id` int(11) NOT NULL,
  `price_id` bigint(20) NOT NULL,
  PRIMARY KEY (`detail_number`),
  KEY `users_orderdetail_order_id_406d58dd` (`order_id`),
  KEY `users_orderdetail_price_id_d010a074` (`price_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_orderdetail
-- ----------------------------

-- ----------------------------
-- Table structure for users_price
-- ----------------------------
DROP TABLE IF EXISTS `users_price`;
CREATE TABLE `users_price` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `price` decimal(10,2) NOT NULL,
  `type` varchar(100) NOT NULL,
  `external_price` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_price
-- ----------------------------
INSERT INTO `users_price` VALUES ('2', '11.00', 'Greenhouse2', '13.00');

-- ----------------------------
-- Table structure for users_researchrequest
-- ----------------------------
DROP TABLE IF EXISTS `users_researchrequest`;
CREATE TABLE `users_researchrequest` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `primary_investigator` varchar(255) NOT NULL,
  `primary_contact` varchar(255) NOT NULL,
  `department` varchar(255) NOT NULL,
  `lab_room_number` varchar(255) NOT NULL,
  `contact_phone` varchar(255) NOT NULL,
  `contact_after_hours` varchar(255) NOT NULL,
  `email` varchar(254) NOT NULL,
  `request_category` varchar(255) NOT NULL,
  `grant_code` varchar(255) NOT NULL,
  `project_title` varchar(255) NOT NULL,
  `plant_species` varchar(255) NOT NULL,
  `safety_concern` tinyint(1) NOT NULL,
  `current_date` date NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `zone_number` varchar(255) NOT NULL,
  `number_of_tables` int(11) NOT NULL,
  `photoperiod` int(11) NOT NULL,
  `min_temperature` decimal(5,2) NOT NULL,
  `requirements_clarification` longtext NOT NULL,
  `applicant_account_id` bigint(20) NOT NULL,
  `approved` int(11) NOT NULL,
  `bench` varchar(255) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `users_researchrequest_applicant_account_id_4568802b` (`applicant_account_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_researchrequest
-- ----------------------------
INSERT INTO `users_researchrequest` VALUES ('7', '1', '1111', '11111', 'Greenhouse2', '15621391234', '111111111', 'zhangsan@126.com', '1', '111111111111', '111111111', '11111111', '0', '2024-03-28', '2024-03-01', '2024-03-02', '11111111111111', '2147483647', '2147483647', '999.99', '111111111111111111111', '3', '0', '0', '1');
INSERT INTO `users_researchrequest` VALUES ('8', '1111111', '11111111111111', '11111111111111', 'Greenhouse2', '15621391234', '111111', 'zhangsan@126.com', '1', '111111111', '11111111111', '11111111111111', '0', '2024-03-28', '2024-03-29', '2024-03-31', '1111111', '2147483647', '2147483647', '111.00', '111111111', '3', '0', '0', '1');
INSERT INTO `users_researchrequest` VALUES ('9', '111111111', '11111111111111111111', '11111111111111111', 'Greenhouse2', '15621391234', '11111111111111111', '', '1', '111111111111111111111', '111111111111111111111', '1111111111111', '0', '2024-03-28', '2024-04-02', '2024-04-04', '1111111111111111', '0', '0', '0.00', '11111111111111111', '3', '0', '0', '1');
INSERT INTO `users_researchrequest` VALUES ('10', '111', '111', '1111', 'Greenhouse2', '15621391234', '11111111111', '', '1', '11111111111111111111', '11111111111111', '11111111111111', '0', '2024-03-28', '2024-02-06', '2024-02-21', '111111111111111111111111111111', '0', '0', '0.00', '11111111111111', '3', '0', '0', '1');
INSERT INTO `users_researchrequest` VALUES ('11', '11111', '111', '111111111', 'Greenhouse2', '15621391234', '1111111111111111111111111111111', 'zhangsan@126.com', '1', '111111111111111111111111111111111', '11111111111111111111111111', '1111111111111111111111', '0', '2024-03-28', '2024-04-11', '2024-04-24', '11111111111111', '0', '0', '0.00', '1111111111111', '3', '1', 'bench 1,bench 2,bench 3', '1');
