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

* Crear una instancia en AWS con imagen ubuntu 22.04 LTS  
* Abrir el cliente SSH de la instancia creada y correr los comandos en terminal:   

      sudo apt update
      sudo apt install docker.io -y
      sudo apt install docker-compose -y

      sudo systemctl enable docker
      sudo systemctl start docker

Aqui envidenciaremos la conexion del moodle en nuestra instancia y los contenedores de docker con la imagen de bitnami/moodle.

![WhatsApp Image 2023-05-04 at 11 48 41](https://user-images.githubusercontent.com/68908889/236272480-f16e5a29-0a30-4c09-bc92-82ef1fc509f4.jpeg)

![WhatsApp Image 2023-05-04 at 11 49 02](https://user-images.githubusercontent.com/68908889/236272558-1366f3ab-666b-4aef-9877-7481559d5405.jpeg)

![WhatsApp Image 2023-05-04 at 11 49 21](https://user-images.githubusercontent.com/68908889/236272580-4ced66f4-c382-4a22-b4c4-139dedc17efd.jpeg)

![WhatsApp Image 2023-05-04 at 11 49 21 (1)](https://user-images.githubusercontent.com/68908889/236272604-79a0b613-7268-459f-b5b0-df5ebe8d0ebe.jpeg)


