#PRIMERA PARTE DE LA TAREA
#Crea una base de datos llamada "amigos" y luego importe friends.sql. Esto creará dos nuevas tablas: usuarios y amistades.

#Usando el siguiente ERD como referencia, escribe una consulta SQL que devuelva una lista de usuarios junto con los nombres de sus amigos.

SELECT users.first_name, users.last_name, user2.first_name as friend_first_name, user2.last_name as friend_last_name FROM friendships
LEFT JOIN users ON users.id = friendships.user_id
LEFT JOIN users as user2 ON user2.id = friendships.friend_id
