# RESERVAS-APP
Aplicación para reservas de ambiente

*****************************************************************************************

1- Dockerfile
  Se utiliza la imagen Python:3.11-slim
  Se crea el direcorio de la aplicación en el contenedor
  Se copia el archivo local requeriments.txt en el directorio del contenedor para poder ser utilizado
  Se utiliza el archivo requeriments.txt en donde se define lo necesario para que la app en python funcione.
  Se realiza la instalacion del contenido del archivo requerimentes.txt
  se copia la aplicación en el directorio del contenedor para poder ser ejecutada
  ese expone en el puerto 5000
  Se ejecuta python y la aplicación

*****************************************************************************************

2- Requeriments.txy
  Contiene lo necesario para la aplicación python

*****************************************************************************************

4- .env
  Archivo de variables de entorno

*****************************************************************************************

5- docker-compose.yml
  Se debife el servicio: reservas-app
  Se indica el biuld, el cual en este caso se tomara el Dockerfile del directorio actual.
  Se indica que el mapeo de los puertos en donde 500 es el puerto del contenedor y 500 es el puerto local
  Se definen los volumenes, el primero es para la persistencia de la base y el segundo es para la visualización de los cambios locales en tiempo real.
  Se indica el archivo que contendra las variables de entorno a utilizar en el contenedor
  Se indica la red: reservas-app

*****************************************************************************************

6- Index.html
  Contiene el diseño del formulario

*****************************************************************************************

7- reservas-app.py
  Diseño de la aplicación en python

*****************************************************************************************

INSTRUCCIONES
Para levantar la aplicación:
1. Clonar el repositorio.
2. Una vez clonado el repositorio, ingresar a la carpeta clonada
3. ejecutar: docker-compose up --build
4. Probar la aplicación en http://localhost:5000/

*****************************************************************************************
