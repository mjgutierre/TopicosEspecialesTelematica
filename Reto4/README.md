# Info de la materia: st0263-2023-1 <Tópicos Especiales En Telemática>

# Estudiante(s):
## Paulina Ocampo Duque, mpocampod@eafit.edu.co
## Maria Jose Gutierrez Estrada, mjgutierre@eafti.edu.co
### Profesor: Juan Carlos Montoya, jcmtya 

# 1. Breve descripción de la actividad

Despliegue de una aplicación open source LAMP de comunidad que represente un sistema de información del tipo Sistema de Gestión de Aprendizaje (LMS, por sus siglas en inglés). En este caso se seleccionará Moodle.

## Requerimientos:

1. Alta Disponibilidad:
  - Balanceadores de carga
  - Crecimiento horizontal en autoscaling
  - Disponibilidad en la capa de servicios
  - Disponibilidad en la capa de persistencia de datos para el manejo de archivos.
  - Disponibilidad en la capa de bases de datos para el manejo de la información almacenada en el motor definido para esto.

Nota: Para efectos del reto se utilizaran servicios administrados de AWS para Balanceadores de carga, autoscaling, base de datos y NFS.

# 2. Pasos a seguir

En esta sección se mostrará paso por paso el desarrollo del reto. 

## Moodle

* Crear una instancia en AWS con imagen ubuntu 22.04 LTS  
* Abrir el cliente SSH de la instancia creada y correr los comandos en terminal:   

      sudo apt update
      sudo apt install docker.io -y
      sudo apt install docker-compose -y

      sudo systemctl enable docker
      sudo systemctl start docker

Aqui envidenciaremos la conexion del moodle en nuestra instancia y los contenedores de docker con la imagen de bitnami/moodle.También para mas información, nos podemos dirigir al archivo [docker-compose.yml](https://github.com/mjgutierre/TopicosEspecialesTelematica/blob/master/Reto4/Docker-compose.yml) en donde encontraremos la configuración completa del contenedor.

![WhatsApp Image 2023-05-04 at 11 48 41](https://user-images.githubusercontent.com/68908889/236272480-f16e5a29-0a30-4c09-bc92-82ef1fc509f4.jpeg)

![WhatsApp Image 2023-05-04 at 11 49 02](https://user-images.githubusercontent.com/68908889/236272558-1366f3ab-666b-4aef-9877-7481559d5405.jpeg)

![WhatsApp Image 2023-05-04 at 11 49 21](https://user-images.githubusercontent.com/68908889/236272580-4ced66f4-c382-4a22-b4c4-139dedc17efd.jpeg)

![WhatsApp Image 2023-05-04 at 11 49 21 (1)](https://user-images.githubusercontent.com/68908889/236272604-79a0b613-7268-459f-b5b0-df5ebe8d0ebe.jpeg)

Ahora se corre el siguiente comando para correr el archivo docker-compose y así aplicar los cambios :
      
      sudo docker-compose up
      

## BD RDS

Para la creación de la base de datos, utilizamos un recurso de aws llamado RDS en donde se configuro de la siguiente manera.

![image](https://user-images.githubusercontent.com/68908889/236353134-e1c698f2-dd65-4ce7-bd28-06c3d018882a.png)

![image](https://user-images.githubusercontent.com/68908889/236353163-500c7de7-371e-4f55-8e7c-02d5bb59e57c.png)

![image](https://user-images.githubusercontent.com/68908889/236353227-8efb5044-16da-4808-8134-5c0d7adf4b28.png)

![image](https://user-images.githubusercontent.com/68908889/236353306-2954b44d-06b9-459b-97b7-138eb9dc48d4.png)


## NFS
Para configurar el nfs con los servicios de aws, se creo el sistema y se asociaron a la red los grupos de seguridad de la instancia 

![image](https://user-images.githubusercontent.com/68908889/236340086-9449cdfd-d440-4022-af21-49510c140411.png)

![image](https://user-images.githubusercontent.com/68908889/236340120-ca6f57b2-40be-4110-ac16-d4af72d49917.png)

De esta manera, en el grupo de seguridad de nuestra instancia se agrego la siguiente regla de entrada.

![image](https://user-images.githubusercontent.com/68908889/236340382-28ac5c49-4108-4eb3-b10d-4720c09c4741.png)

Luego, se ejecutan los siguientes comandos para instalar el nfs-common en el cliente en la instancia Moodle y crear una carpeta llamada /mnt/moodle para posteriormente aplicar el mount y poder enlazar esa carpeta con el nfs-server y se hace el montaje a traves de DNS.

       sudo apt-get -y update
       sudo apt-get -y install nfs-common
       sudo mkdir -p /mnt/moodle
       sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-073e2adaddbb83c53.efs.us-east-1.amazonaws.com: / /mnt/efs
    
![image](https://user-images.githubusercontent.com/68908889/236340628-06c8eea8-4d01-4c6e-9b15-26eed72e5bf9.png)

El ultimo comando permitirá verificar que el mount esté listo ya que aparecerá el DNS de la instancia del nfs-server.

![WhatsApp Image 2023-05-04 at 17 00 17](https://user-images.githubusercontent.com/68908889/236340397-d8b2094b-4e44-4242-bbff-3d81a68486bc.jpeg)

## Balanceador de Cargas


# Referencias 

- [Moodle en AWS](https://aws.amazon.com/es/blogs/aws-spanish/acelerar-aprendizaje-remoto-en-minutos-usando-moodle-en-aws/)
- [Moodle](https://www.udemy.com/course/creacion-de-aula-virtual-moodle-41-en-amazon-web-service/)
- [NFS en AWS](https://www.youtube.com/watch?v=-u72cCq2aqM)
