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
