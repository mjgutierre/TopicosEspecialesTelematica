# MICROSERVICIOS COMUNICADOS CON GRPC

## Información de la asignatura.
Topicos Especiales en Telematica.

## Datos del estudiante (s).
Maria José Gutiérrez Estrada. ***mjgutierre@eafit.edu.co***

## Tabla de contenido 
1. [Descripción y alcance del proyecto](https://github.com/mjgutierre/TopicosEspecialesTelematica/edit/master/Reto1/README.md#descripción-y-alcance-del-proyecto)
2. [Estructura del proyecto](https://github.com/mjgutierre/TopicosEspecialesTelematica/edit/master/Reto1/README.md#estructura-del-proyecto)
3. [Arquitectura del proyecto](https://github.com/mjgutierre/TopicosEspecialesTelematica/edit/master/Reto1/README.md#arquitectura-de-la-solución-planteadao)
4. [Resultados logrados](https://github.com/mjgutierre/TopicosEspecialesTelematica/edit/master/Reto1/README.md#resultados-logrados)
5. [Descripción técnica / Guía de uso](https://github.com/mjgutierre/TopicosEspecialesTelematica/edit/master/Reto1/README.md#descripción-técnica-de-la-solución-implementada)
6. [Referencias](https://github.com/mjgutierre/TopicosEspecialesTelematica/edit/master/Reto1/README.md#referencias)


## Descripción y alcance del proyecto.
El objetivo de este proyecto principalmente es desarrollar habilidades de programación en la implementacion de un prototipo de aplicacion web para comercio electronico, utilizando como estilo arquitectonico los microservicios. 
La comunicacion entre los procesos debe ser a traves de un middleware, en este caso, a traves de RPC (llamadas a a procedimientos remotos)

Se tuvieron en cuenta ciertas restricciones y caracteristicas para el desarrollo correcto del proyecto. Algunas de estas fueron:
- Se crearon dos microservicios en diferentes lenguajes
    - Catalogo en Nodejs
    - Orden en Python
    
Estos tienen sus propias funcionalidades y a traves de una red de datos se comunican entre ellos por medio de gRPC. Estos debian evitar compartir bases de datos entre ellos y se debia implementar un API para distribuir las peticiones tipo HTTP a la logica de negocio desde un cliente que en este caso seria Postman o Insomnia.

La definicion del servicio para la comunicacion se debia realizar con Protocolo Buffers, es por esto que en los diferentes microservicios hay una carpeta llamada Protobufs que almacenan los archivos con la syntaxis correspondiente. 

Para el despliegue de esta aplicacion se requeria una extensa lectura de documentacion para entender el protocolo que se esperaba utilizar y sus herramientas. Es importante para garantizar un sistema escalable que esta primera version funcione de manera confiable para luego en un entorno de producción seguir considerando nuevas funcionalidades para la correcta integracion entre llamados.

## Estructura del Proyecto. 
> Detalle cómo se encuentra la estructura del proyecto en el repositorio.

## Arquitectura de la solución planteada. 
> En este punto describir que patrones se implementaron.

<p align="center">
  <img src="https://user-images.githubusercontent.com/68908889/223600284-11ab0ab8-3f4a-4b87-8735-63cb12b0d3ad.png" alt="ArquitecturagRPC" width="600" height="400" style="display: block; margin: auto;">
</p>

Esta es la arquitectura del proyecto. Para esta aplicacion se realizo un comercio electronico con API Gateway que gestiona las peticiones HTTP entrantres y las reenvía a los microservicios. 

- El primer servicio como se ve en el diagram es el de Catalogo, en donde los usuarios podran ver el producto, en este caso es un Tour, que contiene los campos de titulo y precio. 
- El segundo servicio es el de ordenes, en donde el usuario podra añadir el producto y la orden se gestionara. 

Para termminos del proyecto se utilizó gRPC, un framework que puede conectar de forma eficiente servicios en y entre centros de datos con soporte conectable para el equilibrio de carga, el rastreo, la comprobación del estado y la autenticación.

Tambien utilizamos en terminos de patrones una pasarela API para centralizar el acceso a los servicios de backend y exponer una API pública para los clientes. Esto ayuda a reducir la complejidad y a proporcionar una mayor seguridad.

## Resultados logrados: 
> Por favor describa claramente en puntos de lo solicitado logró alcanzar los objetivos propuestos. De igual forma, indique cuales objetivos no alcanzo a desarrollar.

Para el cliente, utilizamos una herramienta llamada Insomnia, es muy parecida a Postman y nos ayudo con las peticiones HTTP. Las pruebas que se hicieron fueron las siguientes: 

- Para el servicio de ProductOrder, se envio un JSON con los siguientes campos y estas fueron las respuestas recibidas en el servidor y el API respectivamente.
<p align="center">
  <img src="https://user-images.githubusercontent.com/68908889/223601360-456f26ea-1896-4b39-a21d-e12448a3ddc4.jpeg" alt="PRUEBAORDENInsomnia" width="694" height="130" style="display: block; margin: auto;">
</p>
<p align="center">
  <img src="https://user-images.githubusercontent.com/68908889/223601364-2c3ae6a5-9148-4e67-a43e-73b267cefb00.jpeg" alt="PRUEBAORDERConsola" width="500" height="80" style="display: block; margin: auto;">
</p>
<p align="center">
  <img src="https://user-images.githubusercontent.com/68908889/223601366-b6f08bfd-1362-465f-ba0f-7f2a848c27a2.jpeg" alt="PRUEBAOrden" width="500" height="50" style="display: block; margin: auto;">
</p>

- Para el servicio de ProductCatalog, se envio un JSON con los siguientes campos y estas fueron las respuestas recibidas en el servidor y el API respectivamente.

<p align="center">
  <img src="https://user-images.githubusercontent.com/68908889/223605133-32cf21a3-d7be-4302-9810-ea7013c84812.png" alt="PRUEBASCATALOGOServidor" width="694" height="130" style="display: block; margin: auto;">
</p>
<p align="center">
  <img src="https://user-images.githubusercontent.com/68908889/223607394-2a2d5f3f-c045-4c5b-bd1e-f177b9759df3.png" alt="PRUEBASCATALOGOAPI" width="350" height="40" style="display: block; margin: auto;">
</p>
<p align="center">
  <img src="https://user-images.githubusercontent.com/68908889/223603428-bb28852a-463a-4b05-901d-d4cd12bc4c82.jpeg" alt="PRUEBASCATALOGOInsomnia" width="500" height="694" style="display: block; margin: auto;">
</p>


## Descripción técnica de la solución implementada / Guía de uso:
> Por favor ilustre de manera clara, precisa y breve como se utiliza su solución Iindique todos los aspectos técnicos de la solución (librerías, como se debe compilar, etc, con las versiones de cada elemento que utilice). Igualmente, todos los aspectos de parametrización que se requiere, direcciones IPs, puertos, conexión a bases de datos, etc.


- **Gateway**

Al estar dentro de la carpeta procedemos a crear un entorno virtual o instalar los requerimientos desde nuestra consola en la maquina local.
Para activar el entorno virtual podemos ejecutar en la carpeta de Gateway el siguiente comando:

        .\Scripts\activate 

Para instalar los requerimientos del txt podemos correr el siguiente comando:

        pip install requirements.txt

Luego para correr nuestro Server.py (PUERTO 5000), debemos estar en la siguiente ruta  
        
        Reto1\Back\Gateway\env\src 

y podemos ejecutar el comando:
        
        py server1.py
        
        
- **ProductCatalog**

Para activar el servidor de Catalogo (PUERTO 50051), debemos entrar en la siguiente ruta 

        Reto1/Back/ProductCatalog/src
        
con el siguiente comando 
        
        npm start
    
- **ProductOrder**

Para inicializar el servidor de Orden (PUERTO 50052), debemos estar en la ruta 
        
        Reto1/Back/ProductOrder/Src
        
con el comando 
    
        py server.py
   

Adicional a esto para hacer las peticiones por medio de Postman o Insomnia podemos utillizar los siguienetes archivos JSON 

- Para hacer un metodo POST al servicio de ProductCatalog, debemos utilizar la siguiente URL

      http://localhost:5000/catalog
 
Con el siguiente archivo 

    {
	  "id_Product": 1,
	  "price": 3.00,
	  "title": "hola1"
    }
        
- Para hacer un metodo POST al servicio de ProductOrder, debemos utilizar la siguiente URL
 
        http://localhost:5000/order
        
Con el siguiente archivo 

    {
	"id_Product": 1,
	"title": "TOUR1",
	"quantity": 3
    }
    
        
## Referencias.
- [1]“Descripción general de gRPC | Documentación de API Gateway,” Google Cloud. https://cloud.google.com/api-gateway/docs/grpc-overview?hl=es-419#:~:text=With%20API%20Gateway%20for%20gRPC.
- [2]ST0263, “st0263-2023-1/Laboratorio N1-RPC at main · ST0263/st0263-2023-1,” GitHub, Feb. 27, 2023. https://github.com/ST0263/st0263-2023-1/tree/main/Laboratorio%20N1-RPC .
- [3]J. Hernández, “Microservicios de Python con gRPC,” Medium, Apr. 21, 2022. https://devjaime.medium.com/microservicios-de-python-con-grpc-3ff25126b6eb .