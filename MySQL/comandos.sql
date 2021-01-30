--para inicializar mysql en shell de xampp
mysql -u root -p

MariaDb[(none)]

--mostrar las  bases de datos de mi pc
show databases;

--seleccionar una base de datos se pone use y el nombre de la base de datos
use amigos;

--dentro de la based, mostramos las tablas,
show tables;

--crear nueva base de datos
create database zzzzz;

--crear tabla dentro de base de datos
create table nombretabla1(
    id int,
    nombre varchar(255),
    edad int
);

--saber tipo y columnas de una tabla
describe nombretabla1;

--insercion en la tabla
insert into nombretabla1(id, nombre, edad) values(1, "paula", 28);

