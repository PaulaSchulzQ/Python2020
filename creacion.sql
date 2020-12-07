CREATE TABLE `paula`.`schulz` (
     `id` INT NOT NULL ,
 `nombre` VARCHAR(12) NOT NULL ,
  `apellido` VARCHAR(12) NOT NULL , 
  `covid` BOOLEAN NOT NULL DEFAULT FALSE , 
  PRIMARY KEY (`id`)) ENGINE = InnoDB CHARSET=utf8 COLLATE utf8_spanish_ci;

  -- insercion de registro
  INSERT INTO `schulz` (`id`, `nombre`, `apellido`, `covid`) VALUES ('', 'vicente', 'puentes', '0');

  INSERT INTO `schulz` (`id`, `nombre`, `apellido`, `covid`) VALUES ('', 'gato', 'perro', '1');

  /*!INSERCION DE ATRIBUTOS*/;
INSERT INTO `guillon` (`id`, `nombre`, `apellido`, `covid`) VALUES (NULL, 'Cecilia', 'Garces', '0');
INSERT INTO `guillon` (`id`, `nombre`, `apellido`, `covid`) VALUES (NULL, 'Andres', 'Toro', '1');
INSERT INTO `guillon` (`id`, `nombre`, `apellido`, `covid`) VALUES (NULL, 'Alonso', 'Toro', '0');

/*!SE PUEDE OMITIR VALOR AUTOINCREMENTAL*/;
INSERT INTO `guillon` (`nombre`, `apellido`, `covid`) VALUES ('Elsa', 'Zapata', '0');

/*!MODIFICAR UN REGISTRO*/;
UPDATE `guillon` SET `id` = '6' WHERE `guillon`.`id` = 55;

/*!ELIMINAR UN REGISTRO*/;
DELETE FROM `guillon` WHERE `guillon`.`id` = 4

/*!CONSULTAR REGISTRO POR SU CLAVE PRIMARIA*/;
SELECT * FROM `guillon` WHERE `id`=2

