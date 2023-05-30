# **Reto 5**
**Curso:** Tópicos Especiales en Telemática st0263-2023-1 <br>
**Título:** Laboratorio: Map/Reduce en Python con MRJOB y reto Reto de Programación <br>
**Autores:** Maria Jose Gutierrez Estrada -  mjgutierre@eafit.edu.co - Estudiante de la Universidad EAFIT - [mjgutierre](https://github.com/mjgutierre) <br>

### Profesor: Juan Carlos Montoya, jcmtya 
***

# 1. Breve descripción de la actividad


# 2. Documentación Técnica 

## Preparación del entorno

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

## Creación de Bucket S3 en consola AWS CLI

Luego de configurar las credenciales, ejecutaremos el siguiente comando para crear el bucket s3://mjgutierre-reto5-emr

      aws s3 mb s3://mjgutierre-reto5-emr
      
Para verificar la creacion se ejecutará el comando

      aws s3 ls

Aqui se puede observar que en un primer momento ejecutamos el comando para ver que s3 bucket estaban en nuestra cuenta y luego procedemos a crear uno nuevo y verificar si fue exitoso este proceso.

<p align="center">
  <img src="https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/bac9522c-ad76-49ac-9e02-262050f47345" alt="creacion s3" width="" height="" style="display: block; margin: auto;">
</p>

Podemos observar que en nuestra cuenta ya se encuentra el s3 bucket.

<p align="center">
  <img src="https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/ada0f021-e319-4ecb-a81b-20dc3e039cc4" alt="verificacion en aws de creacion s3" width="" height="" style="display: block; margin: auto;">
</p>

### Creación de Cluster en consola AWS CLI


aws emr create-cluster \ --name emr-MyClusterEMR \ --release-label emr-5.26.0 \ --service-role EMR_DefaultRole \ --ec2-attributes KeyName=emr-key1,InstanceProfile=EMR_EC2_DefaultRole \ --applications Name=Hue Name=Ozzie Name=Spark Name=Hadoop Name=Sqoop Name=Hive \ --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large InstanceGroupType=TASK,InstanceCount=1,InstanceType=m4.large \ --no-auto-terminate









Name: emr-MyClusterEMR
 Amazon EMR release: emr-5.26.0
o Applications EMR:
§ Hue 4.4.0
§ Spark 2.4.3
§ Hadoop 2.8.5
§ Sqoop 1.4.7
§ Hive 2.3.5
§ Ozzie 5.1.0

o Instance groups.
§ Primary. Seleccione m4.large.
§ Core. Seleccione m4.large
Task. Seleccione m4.large

Amazon EC2 key pair emr-key.pem.
§ Service Role: Seleccione EMR_DefaultRole.
§ Instance profile: Seleccione EMR_EC2_DefaultRole

# Referencias
- [Uso de AWS CLI](https://docs.aws.amazon.com/es_es/cli/latest/userguide/cli-chap-using.html)
- [Amazon S3](https://docs.aws.amazon.com/es_es/cli/latest/userguide/cli-services-s3.html)
- [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps-create-cluster.html)
