# **Reto 5**
**Curso:** Tópicos Especiales en Telemática st0263-2023-1 <br>
**Título:** Laboratorio: Map/Reduce en Python con MRJOB y reto Reto de Programación <br>
**Autores:** Maria Jose Gutierrez Estrada -  mjgutierre@eafit.edu.co - Estudiante de la Universidad EAFIT - [mjgutierre](https://github.com/mjgutierre) <br>

### Profesor: Juan Carlos Montoya, jcmtya 
***

# 1. Descripción de la actividad

Despliegue un cluster EMR en su cuenta de AWS Academy, teniendo en cuenta la guia para esto.

Reto: Consulte como realizar la implementación del cluster via AWS CLI. En el informe debe enviar la evidencia de los diferentes comandos que tuvo que ejecutar para poder instanciar el cluster EMR. Adjunte el paso a paso con los diferentes pantallazos de evidencia.

Ejecutar la versión serial/secuencial de la aplicación de wordcount-local.py. Esto lo puede ejecutar en el main node del clúster EMR. 

# 2. Documentación Técnica 

## Preparación del entorno (Reto1)

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
  <img src="https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/53a8ebd4-e06b-4195-a536-cf4e30c49102" alt="creacion s3" width="" height="" style="display: block; margin: auto;">
</p>

Podemos observar que en nuestra cuenta ya se encuentra el s3 bucket.

<p align="center">
  <img src="https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/ada0f021-e319-4ecb-a81b-20dc3e039cc4" alt="verificacion en aws de creacion s3" width="" height="" style="display: block; margin: auto;">
</p>

## Creación de Cluster en consola AWS CLI

Con los siguientes comandos crearemos un cluster a traves de la consola de AWS CLI
    
    aws emr create-cluster --name emr-MyClusterEMR --release-label emr-6.10.0 --service-role EMR_DefaultRole --ec2-attributes KeyName=emr-key1,InstanceProfile=EMR_EC2_DefaultRole  --applications Name=Hue Name=Spark Name=Hadoop Name=Sqoop Name=Hive  --log-uri s3://mjgutierre-reto5-emr/logs/ --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large InstanceGroupType=TASK,InstanceCount=1,InstanceType=m4.large --no-termination-protected


**Los valores configurados fueron:**

- Nombre: emr-MyClusterEMR
- Amazon EMR release: emr-6.10.0
- Aplicaciones
  - Hue 4.4.0
  - Spark 2.4.3
  - Hadoop 2.8.5
  - Sqoop 1.4.7
  - Hive 2.3.5
  - Ozzie 5.1.0
    
- Instance groups.
  - Primary. m4.large.
  - Core. m4.large
  - Task. m4.large

- Amazon EC2 key emr-key1.pem.
- IAM roles:
  - Service Role: Seleccione EMR_DefaultRole.
  - Instance profile: Seleccione EMR_EC2_DefaultRole

Y este es el resultado arrojado

- Consola 

<p align="center">
  <img src="https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/ab61c925-9e38-43cd-8bc1-90c499c12ed4" alt="creacion emr a traves de aws cli" width="" height="" style="display: block; margin: auto;">
</p>

- EMR AWS 

<p align="center">
  <img src="https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/539ed8e1-ad62-454e-a998-c51fed7dc33a" alt="verificacion emr" width="" height="" style="display: block; margin: auto;">
</p>

![image](https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/eb3e06e7-32e2-417b-ae2c-74f57de4ce4f)

- EC2

![image](https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/8ba13706-06e2-43de-8284-3120c0e68c53)

## Ejecución de la versión serial de una aplicación (wordcount-local.py) desde el main node cluster (Reto2)

Para continuar con nuestro reto, ingresamos desde consola al man node de nuestro cluster creado. 

    ssh -i "emr-key1.pem" ec2-user@ec2-3-89-116-115.compute-1.amazonaws.com
    
Tener en cuenta:
  - Nuestro grupo de seguridad debe permitir como regla de entrada el puerto 22 (SSH)
  - Se debe cambiar el usuario por ec2-user como se puede ver en el comando 

Se tendra el siguiente resultado

<p align="center">
  <img src="https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/6bed6547-8d50-49dd-8e06-573760396f39" alt="ingreso a emr por ssh" width="" height="" style="display: block; margin: auto;">
</p>

Luego ejecutaremos dentro de nuestra consola los siguientes comandos para actualizar nuestro paquete yum e instalar git:

    sudo yum update -y
    sudo yum install git -y
    
Luego clonaremos el repositorio 
    
    git clone https://github.com/ST0263/st0263-2023-1.git
    
Una vez dentro se ejecutaron los siguientes comandos

     cd st0263-2023-1/"Laboratorio N6-MapReduce"/wordcount
     python wordcount-local.py ../../datasets/gutenberg-small/*.txt > salida-serial.txt
     more salida-serial.txt
     
 Este sera nuestro resultado

<p align="center">
  <img src="https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/f0e7b4b0-b255-4c88-845b-f3bb372391e8" alt="ingreso a emr por ssh" width="" height="" style="display: block; margin: auto;">
</p>

Como parte del sistema, se instalará mrjob así:

    sudo yum install python-pip -y
    sudo pip3 install mrjob
    sudo pip install boto3
    
  Probamos mrjob con python local:
     
     cd wordcount
     python wordcount-mr.py ../../datasets/gutenberg-small/*.txt

  Y este es nuestro resultado 
  
![image](https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/fdd67602-9d14-4bfb-961c-fdb967ac3553)
![image](https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/f2ba79a8-da91-45d9-bfbe-04a29f14c030)


Copiamos el dataset en nuestro emr

    hdfs dfs -mkdir /user/admin
	  hdfs dfs -copyFromLocal /home/hadoop/st0263-2023-1/datasets/ /user/admin/

Y luego ejecuramos con 

    python wordcount-mr.py hdfs:///user/admin/datasets/gutenberg-small/*.txt -r hadoop --output-dir hdfs:///user/admin/result3
   
Este comando ejecuta un programa Python llamado wordcount-mr.py en un entorno Hadoop utilizando Hadoop Streaming. El programa cuenta las palabras en varios archivos de texto ubicados en el directorio hdfs:///datasets/gutenberg-small/ y guarda los resultados en el directorio hdfs:///user/admin/result3.

Tendremos un resultado como este

![image](https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/97984e4b-fc5a-432c-b84f-19f0104c48eb)


Se clona el repositorio donde estan los codigos 

      git clone https://github.com/mjgutierre/TopicosEspecialesTelematica.git
      cd TopicosEspecialesTelematica/Reto5/MapReduce

Luego copiamos los datos a un directorio 

     hdfs dfs -put dataempleados.txt hdfs:///user/admin/dataempleados.txt
     
Y ejecutamos 

      python a_avrg_salary_se_mr.py hdfs:///user/admin/dataempleados.txt -r hadoop --output-dir hdfs:///user/admin/punto1a

Para obtener el siguiente resultado


Se creo un archivo llamado mrjob.conf con las siguientes configuraciones

    runners:
      emr:
          aws_access_key_id:ASIATQCL7MV5ZPJCK6EN 
          aws_secret_access_key: zP7e2hn0zEuIHcewCVzdapqNpjQeQlNp86ERoLSA
          aws_session_token: FwoGZXIvYXdzEJn//////////wEaDHOYkX7B0Lua0VX9OCLIAb6delJoTwisMafvmSHRcUWHPfYkxFGJQgaXL9wjRgCa0VErQ67t1Sg4p5wj6bNi10l+vlAPFo6zhhRSABLCZraXJnK7t6VtKn/HjenmyOee3mrW5irlXAIX5E9Vm7C1Xri2py4iVHbdnsFkXnjPsAK8mlxl08GjBCZJGN/Ap35D4Qn/ZRzB490/srjT8AQ/M4C+brbw2BJacZn1WxvvFKGNVGu5CVOFU12mqkysmxcwGaYyB8JlU1VRBpF3O5n9tvk5X5tyyKTnKLX34qMGMi1tr4X1c2+oJR6LDSCDzMAEQo2l6rJeyzQSo1XgUQzdUdILjbshd8ya8S8yfMo=
          region: us-east-1
          ec2_key_pair: emr-key1
          ec2_key_pair_file: ~/.ssh/emr-key1.pem
          ssh_tunnel: true
          emr_job_flow_id: j-1PET2VX7YRRR2

  
## Reto de Programación en Map/Reduce (Reto3)

1. Se tiene un conjunto de datos, que representan el salario anual de los empleados formales en Colombia por sector económico, según la DIAN. 

  Programa en Map/Reduce, con hadoop en Python, que permita calcular:

  **a. El salario promedio por Sector Económico (SE)**
	
  - Local
	
	    python a_avrg_salary_se_mr.py  dataempleados.txt	
	
<p align="center">
  <img src="https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/c6fc80cd-7c56-4fea-93b1-0ba1e5364925" alt="RESULTADOS DIAN LOCAL" width="" height="" style="display: block; margin: auto;">
</p>
	
   - EMR

	     cd DIAN
	     hdfs dfs -put dataempleados.txt hdfs:///user/admin/dataempleados.txt
	     python a_avrg_salary_se_mr.py hdfs:///user/admin/dataempleados.txt -r hadoop --output-dir hdfs:///user/admin/punto1a
	     hdfs dfs -cat /user/admin/punto1a/*

![image](https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/cfc2561c-a56f-4aba-8d9a-dacec465ded9)

![image](https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/0fb88f5a-3b69-4c0f-b6b8-0831018ff33a)

en s3 

	      python a_avrg_salary_se_mr.py hdfs:///user/admin/dataempleados.txt -r hadoop --output-dir s3://mjgutierre-reto5-emr/test1/p1a
	      
![image](https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/a052aed6-62e3-41d1-b518-6fee4e964764)


  **b. El salario promedio por Empleado**
	
  - Local
	
	     python b_avrg_salary_emp_mr.py  dataempleados.txt
	
<p align="center">
  <img src="https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/1219053f-fddb-47ee-a3d2-75c4b1de4097" alt="RESULTADOS DIAN LOCAL" width="" height="" style="display: block; margin: auto;">
</p>

   - EMR

	     python b_avrg_salary_emp_mr.py hdfs:///user/admin/dataempleados.txt -r hadoop --output-dir hdfs:///user/admin/punto1b
	     hdfs dfs -cat /user/admin/punto1b/*

![image](https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/70d48b8b-2d29-4707-9401-7a79cff60623)

en s3 

		python b_avrg_salary_emp_mr.py hdfs:///user/admin/dataempleados.txt -r hadoop --output-dir s3://mjgutierre-reto5-emr/test1/p1b

![image](https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/9c263680-0b8d-4dcd-8624-5a4fbbc46d52)

		
  **c. Número de SE por Empleado que ha tenido a lo largo de la estadística**
	
  - Local
	
	      python c_se_emp_mr.py  dataempleados.txt
	
<p align="center">
  <img src="https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/d9af69cb-ed77-48f3-ae33-9a18b06d4944" alt="RESULTADOS DIAN LOCAL" width="" height="" style="display: block; margin: auto;">
</p>

   - EMR

	      python c_se_emp_mr.py hdfs:///user/admin/dataempleados.txt -r hadoop --output-dir s3://mjgutierre-reto5-emr/test1/p1c	  	     
	     
![image](https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/558e3932-095d-4c6f-9b8a-0864f1304d0c)
	
	
![image](https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/6b431dd3-aa76-4666-a270-8645d828efb3)

	
2. Se tiene un conjunto de acciones de la bolsa, en la cual se reporta a diario el valor promedio por acción, la estructura de los datos es (archivo: dataempresas.csv):

	    cd Acciones
	    hdfs dfs -put dataempresas.txt hdfs:///user/admin/dataempresas.txt
  
  Programa en Map/Reduce, con hadoop en Python, que permita calcular:

**a. Por acción, dia-menor-valor, día-mayor-valor**
	
  - Local	
	
	       python a_minmax_mr.py  dataempresas.txt
	
<p align="center">
  <img src="https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/b711097a-19c5-47ef-84b3-b83a812c5174" alt="RESULTADOS EMPRESAS LOCAL" width="" height="" style="display: block; margin: auto;">
</p>
	
  - EMR		

	       python a_minmax_mr.py hdfs:///user/admin/dataempresas.txt -r hadoop --output-dir s3://mjgutierre-reto5-emr/test1/p2a	
	       
	      

	
**b. Listado de acciones que siempre han subido o se mantienen estables.**
	
  - Local	
	
	       python b_estable_mr.py  dataempresas.txt
		
<p align="center">
  <img src="https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/d74b11f4-cda0-4c77-bfb8-0e9d83dd54c8" alt="RESULTADOS EMPRESAS LOCAL" width="" height="" style="display: block; margin: auto;">
</p>
	
  - EMR	

	        python b_estable_mr.py hdfs:///user/admin/dataempresas.txt -r hadoop --output-dir s3://mjgutierre-reto5-emr/test1/p2b

**c. DIA NEGRO: Día en el que la mayor cantidad de acciones tienen el menor valor de acción (DESPLOME), suponiendo una inflación independiente del tiempo.**
	
  - Local	
	
	       python c_dianegro_mr.py dataempresas.txt
		
<p align="center">
  <img src="https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/f9cd3be2-df28-4eed-8900-716960663de8" alt="RESULTADOS EMPRESAS LOCAL" width="" height="" style="display: block; margin: auto;">
</p>
	
  - EMR	

		python c_dianegro_mr.py hdfs:///user/admin/dataempresas.txt -r hadoop --output-dir s3://mjgutierre-reto5-emr/test1/p2c

![image](https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/821f8774-c5f3-4c0e-94ec-a48bcddbb23b)

	
3. Sistema de evaluación de películas: Se tiene un conjunto de datos en el cual se evalúan las películas con un rating.

		cd Peliculas
	        hdfs dfs -put datapeliculas.txt hdfs:///user/admin/datapeliculas.txt
		
  Realizar un programa en Map/Reduce, con hadoop en Python, que permita calcular:
	
	
 **a. Número de películas vista por un usuario, valor promedio de calificación**
	
  - Local	
	
	       python a.py datapeliculas.tx
		
<p align="center">
  <img src="https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/3b00a6c6-9efd-4b01-a696-3e3583a3cf8a" alt="RESULTADOS PELICULAS LOCAL" width="" height="" style="display: block; margin: auto;">
</p>
	
  - EMR		
  
		python a.py hdfs:///user/admin/datapeliculas.txt -r hadoop --output-dir s3://mjgutierre-reto5-emr/test1/p3a
		
 **b. Día en que más películas se han visto**
	
  - Local	
	
	      python b_masPelisFecha_mr.py datapeliculas.txt
		
<p align="center">
  <img src="https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/a7120c91-8b70-4b4f-a534-b4bb6df3ffe1" alt="RESULTADOS PELICULAS LOCAL" width="" height="" style="display: block; margin: auto;">
</p>
	
  - EMR	
	
	       python b_masPelisFecha_mr.py hdfs:///user/admin/datapeliculas.txt -r hadoop --output-dir s3://mjgutierre-reto5-emr/test1/p3b
	
 **c. Día en que menos películas se han visto**
	
  - Local	
	
	       python c_menosPelisFecha_mr.py datapeliculas.txt
		
<p align="center">
  <img src="https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/0f77ffa4-7b47-4948-a70d-d95b76af9c03" alt="RESULTADOS PELICULAS LOCAL" width="" height="" style="display: block; margin: auto;">
</p>
	
  - EMR

		python c_menosPelisFecha_mr.py hdfs:///user/admin/datapeliculas.txt -r hadoop --output-dir s3://mjgutierre-reto5-emr/test1/p3c

 **d. Número de usuarios que ven una misma película y el rating promedio**
	
  - Local	
	
	       python d.py datapeliculas.txt
		
<p align="center">
  <img src="https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/05dac064-b4fd-4ec4-974e-cbbe5f19c754" alt="RESULTADOS PELICULAS LOCAL" width="" height="" style="display: block; margin: auto;">
</p>
	
  - EMR
  
		python d.py hdfs:///user/admin/datapeliculas.txt -r hadoop --output-dir s3://mjgutierre-reto5-emr/test1/p3d

**e. Día en que mejor evaluación en promedio han dado los usuarios**
	
  - Local	
	
	       python e.py datapeliculas.txt
		
<p align="center">
  <img src="https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/1276a323-ec0a-4232-8b60-94798853e04f" alt="RESULTADOS PELICULAS LOCAL" width="" height="" style="display: block; margin: auto;">
</p>
	
  - EMR

		python e.py hdfs:///user/admin/datapeliculas.txt -r hadoop --output-dir s3://mjgutierre-reto5-emr/test1/p3e

**f. Día en que mejor evaluación en promedio han dado los usuarios**
	
  - Local	
	
	       python f.py datapeliculas.txt
		
<p align="center">
  <img src="https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/91405b76-49e7-45dc-9e85-7d74e8da290e" alt="RESULTADOS PELICULAS LOCAL" width="" height="" style="display: block; margin: auto;">
</p>
	
  - EMR

		python f.py hdfs:///user/admin/datapeliculas.txt -r hadoop --output-dir s3://mjgutierre-reto5-emr/test1/p3f

**g. La mejor y peor película evaluada por genero**
	
  - Local	
	
	       python g.py datapeliculas.txt
		
<p align="center">
  <img src="https://github.com/mjgutierre/TopicosEspecialesTelematica/assets/68908889/8a5ab7c3-3321-467b-bb28-2bbcc3b93d6b" alt="RESULTADOS PELICULAS LOCAL" width="" height="" style="display: block; margin: auto;">
</p>
	
  - EMR

		python g.py hdfs:///user/admin/datapeliculas.txt -r hadoop --output-dir s3://mjgutierre-reto5-emr/test1/p3g
  
  Con el siguiente comando descargamos las pruebas 
  
  		aws s3 sync s3://mjgutierre-reto5-emr/test1/ C:\Users\USER\Downloads\Pruebasaws
		
# Referencias
- [Uso de AWS CLI](https://docs.aws.amazon.com/es_es/cli/latest/userguide/cli-chap-using.html)
- [Amazon S3](https://docs.aws.amazon.com/es_es/cli/latest/userguide/cli-services-s3.html)
- [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps-create-cluster.html)
- [mrjob on EMR](https://mrjob.readthedocs.io/en/latest/guides/runners.html#configuration)
