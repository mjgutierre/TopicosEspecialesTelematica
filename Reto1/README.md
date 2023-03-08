# MICROSERVICIOS COMUNICADOS CON GRPC

## Información de la asignatura.

## Datos del estudiante (s).
Maria José Gutiérrez Estrada. ***mjgutierre@eafit.edu.co***

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
> Detalle cómo se encuentra la estructura del proyecto en su repositorio.

## Arquitectura de la solución planteada. 
> En este punto por favor describa de igual forma, que patrones logró implementar.
Esta es la arquitectura del proyecto. Para esta aplicacion se realizo un comercio electronico con API Gateway que gestiona las peticiones HTTP entrantres y las reenvía a los microservicios. 

- El primer servicio como se ve en el diagram es el de Catalogo, en donde los usuarios podran ver el producto, en este caso es un Tour, que contiene los campos de titulo y precio. 
- El segundo servicio es el de ordenes, en donde el usuario podra añadir el producto y la orden se gestionara. 

Para termminos del proyecto se utilizó gRPC, un framework que puede conectar de forma eficiente servicios en y entre centros de datos con soporte conectable para el equilibrio de carga, el rastreo, la comprobación del estado y la autenticación.

Tambien utilizamos en terminos de patrones una pasarela API para centralizar el acceso a los servicios de backend y exponer una API pública para los clientes. Esto ayuda a reducir la complejidad y a proporcionar una mayor seguridad.

## Resultados logrados: 
Las pruebas que se hicieron fueron las siguientes: 
> Por favor describa claramente en puntos de lo solicitado logró alcanzar los objetivos propuestos. De igual forma, indique cuales objetivos no alcanzo a desarrollar.

## Descripción técnica de la solución implementada: 
> Por favor indique todos los aspectos técnicos de la solución (librerías, como se debe compilar, etc, con las versiones de cada elemento que utilice). Igualmente, todos los aspectos de parametrización que se requiere, direcciones IPs, puertos, conexión a bases de datos, etc.


## Guía de uso:
> Por favor ilustre de manera clara, precisa y breve como se utiliza su solución.


## Referencias.
- [1]“Descripción general de gRPC | Documentación de API Gateway,” Google Cloud. https://cloud.google.com/api-gateway/docs/grpc-overview?hl=es-419#:~:text=With%20API%20Gateway%20for%20gRPC.
- [2]ST0263, “st0263-2023-1/Laboratorio N1-RPC at main · ST0263/st0263-2023-1,” GitHub, Feb. 27, 2023. https://github.com/ST0263/st0263-2023-1/tree/main/Laboratorio%20N1-RPC .
- [3]J. Hernández, “Microservicios de Python con gRPC,” Medium, Apr. 21, 2022. https://devjaime.medium.com/microservicios-de-python-con-grpc-3ff25126b6eb .
