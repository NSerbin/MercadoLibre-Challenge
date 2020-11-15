# MELI-Script

## Motivacion
Me llegó la posibilidad de demostrar mis conocimientos en Python para una empresa tan prestigiosa como Mercadolibre. Por eso, intenté aplicar todo lo aprendido en este año, utilizando modulos (os y requests), funciones, try/except, ciclos for, condicionales (IF), manejo de archivos con su respectiva validacion de existencia.

## Para qué sirve ??
Meli-Script es un script realizado en Python el cual puede buscar y listar los Items en venta por uno o múltiples USER_ID conectandose a la API de Mercadolibre.

## Cómo está diseñado?
El script se desarrolló en 3 funciones, `menu()` `usuario()` y `multiUsuario()` respectivamente.


## Cómo funciona?
La Función `menu()` llama al menu interactivo el cual cuenta de 3 opciones.
La Opción 1, es para buscar por 1 unico USER_ID los items que posee para vender en el SITE.
La Opción 2, es para buscar múltiples usuarios por sus USER_ID y listar los items que poseen para vender en el SITE.
La Opción 3, para salir.

La Función `usuario()` solicita al usuario el ID que desea buscar, luego es anexada a la URL de la API de Mercadolibre. Luego, gracias al módulo requests, hace un pedido a la API para recibir la información solicitada y es guardada en memoria.
A continuación se hace un recorrido basado en la cantidad de líneas obtenidas por el modulo requests y se filtra las categorías "ID", "TITLE", "CATEGORY_ID" y "NAME" de la categoría. Luego se las agrega a una lista y procedemos a guardar la informacion obtenida en un archivo con el nombre del USER ID y la extensión .log. Utilizando el módulo OS, importamos la funcion Path para averiguar si el archivo existe, en caso de ser afirmativo, la información es anexada al archivo en cuestión, caso contrario, crea el archivo y le agrega toda la información.

La Función `multiUsuario()` solicita al usuario la cantidad de usuarios que desea buscar, luego realiza un bucle for solicitando los USER_IDs necesarios para posteriormente ser anexados a la URL de la API de Mercadolibre. Luego, gracias al módulo requests, hace un pedido a la API para recibir la información solicitada y es guardada en memoria.
A continuación se hace un recorrido basado en la cantidad de líneas obtenidas por el modulo requests y se filtra las categorías "ID", "TITLE", "CATEGORY_ID" y "NAME" de la categoría. Luego se las agrega a una lista y procedemos a guardar la informacion obtenida en un archivo con el nombre del USER ID y la extensión .log. Utilizando el módulo OS, importamos la funcion Path para averiguar si el archivo existe, en caso de ser afirmativo, la información es anexada al archivo en cuestión, caso contrario, crea el archivo y le agrega toda la información.

## ToDo

Lamentablemente, al no tener el tiempo suficiente para poder indagar en cómo obtener el Access_Token para poder hacer los tests al Multiget de la API de mercadolibre, la funcion de MultiUsuario no fue testeada correctamente....

## Contribuciones
Pull requests son bienvenidos. Para modificaciones importantes del código, por favor abrir un issue asi podemos discutir al respecto.
