CREATE TABLE `paula`.`schulz` (
     `id` INT NOT NULL ,
 `nombre` VARCHAR(12) NOT NULL ,
  `apellido` VARCHAR(12) NOT NULL , 
  `covid` BOOLEAN NOT NULL DEFAULT FALSE , 
  PRIMARY KEY (`id`)) ENGINE = InnoDB CHARSET=utf8 COLLATE utf8_spanish_ci;