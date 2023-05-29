# **Reto 5**
**Curso:** Tópicos Especiales en Telemática st0263-2023-1 <br>
**Título:** Laboratorio: Map/Reduce en Python con MRJOB y reto Reto de Programación <br>
**Autores:** Maria Jose Gutierrez Estrada -  mjgutierre@eafit.edu.co - Estudiante de la Universidad EAFIT - [mjgutierre](https://github.com/mjgutierre) <br>

### Profesor: Juan Carlos Montoya, jcmtya 
***

# 1. Breve descripción de la actividad


# 2. Documentación Técnica 

### Preparación del entorno

[Descarga AWS CLI desde la pagina oficial de AWS](https://docs.aws.amazon.com/es_es/cli/latest/userguide/getting-started-install.html)

<p align="center">
  <img src="https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/ea29da9b-3f0a-44bf-8740-f421ba45bbd1" alt="Instalacion AWSCLI" width="" height="" style="display: block; margin: auto;">
</p>

Luego se verifica en nuestra consola que se haya instalado correctamente el awscli, con el comando

    aws --version
    
Después con las credenciales de IAM de nuestra sesion en AWS ejecutaremos los siguientes datos con el comando

    aws configure

<p align="center">
  <img src="https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/f47c4372-49ae-4c59-af16-21e8f678caf7" alt="Verificacion y configuracion AWSCLI" width="" height="" style="display: block; margin: auto;">
</p>

### Creación de Bucket S3 en consola AWS CLI

Luego de configurar las credenciales, ejecutaremos el siguiente comando para crear el bucket s3://mjgutierre-reto5-emr

      aws s3 mb s3://mjgutierre-reto5-emr
      
Para verificar la creacion se ejecutará el comando

      aws s3 ls



###




# Referencias
- [Uso de AWS CLI](https://docs.aws.amazon.com/es_es/cli/latest/userguide/cli-chap-using.html)
- [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps-create-cluster.html)
