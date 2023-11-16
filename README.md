# ProyectoFinal
Proyecto final telematica, que consiste en un chat grupal para carpooling.
Se realiza mediante el lanzamiento de una instancia en aws, la cual contendrá 2 servicios corriendo en 2 contenedores.Esta instancia se despliega como código, por medio de terraform, y hay que especificarle el grupo de seguridad y la subred que queremos usar para la instancia.
Un servicio (guardar los mensajes del chat) corre por el puerto 5555, mientras que el otro ( mostrar los mensajes del chat) corre en el puerto 5556, por lo que hay que abrir estos puertos en el grupo de seguridad. 
En la aplicación .aia, que se puede abrir en app inventor se deben modificar las IPs según la IP de la instancia, para que se conecte correctamente
