Entrega final CoderHouse.

Este es un proyecto de sitio web destinado a negocios (en este caso, cafeterías) que permite el registro e inicio de sesión de usuarios, para poder visualizar productos, promociones y personal, y hacer reservaciones. Además, si se inicia sesión como administrador, se pueden agregar, modificar, visualizar y eliminar productos, promociones y personal.

Requisitos previos
Para ejecutar este proyecto en una máquina local, necesitarás tener instalados los siguientes programas y paquetes:

Python
Django
Willow

Instalación y configuración

Clona el repositorio en tu máquina local.
Crea un entorno virtual de Python y actívalo.
Ejecuta el siguiente comando en la terminal para instalar todas las dependencias del proyecto:

pip install -r requirements.txt

Configura la base de datos y migra las tablas necesarias utilizando los siguientes comandos:

python manage.py makemigrations
python manage.py migrate

Inicia el servidor local con el siguiente comando:

python manage.py runserver
Abre tu navegador web y accede al servidor local en la dirección http://127.0.0.1:8000/.
Uso del proyecto

Una vez que hayas iniciado sesión como usuario registrado, podrás acceder a las diferentes secciones del sitio web, incluyendo la visualización de productos, promociones, personal y la realización de reservaciones.

Si has iniciado sesión como administrador, tendrás acceso a opciones adicionales que te permitirán agregar, modificar, visualizar y eliminar productos, promociones y personal.


Información adicional

Este proyecto es una solución completa y personalizable para cafeterías que buscan mejorar su presencia en línea y ofrecer una experiencia de usuario optimizada a sus clientes.
    
Este proyecto fue diseñado teniendo en cuenta la escalabilidad, la seguridad y la facilidad de uso, y está listo para ser personalizado y adaptado para diferentes tipos de negocios. Espero que disfrutes explorando sus características y funcionalidades. ¡Gracias por utilizar este proyecto!