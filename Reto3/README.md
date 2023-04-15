# RETO 3: Aplicación Monolítica con Balanceo y Datos Distribuidos (BD y archivos)

## Arquitectura del reto 

A nivel de recursos, se desplegará cinco (5) VM en AWS, para implementar la siguiente
arquitectura:

  1. Aplicación CMS Drupal dockerizada monolítica en varios nodos que mejore la
  disponibilidad de esta aplicación.
  2. Implementar un balanceador de cargas basado en apache que reciba el tráfico web https
  de Internet con múltiples instancias de procesamiento.
  3. Tener 2 instancias de procesamiento Drupal detrás del balanceador de cargas.
  4. Tener 1 instancia de bases de datos mariaDB
  5. Tener 1 instancia de archivos distribuidos en NFS.

 ![image](https://user-images.githubusercontent.com/68908889/232166200-d585fa91-665b-4756-a80c-d0bb6818a142.png)
 
 - BD IP PRIV 172.31.81.31
 Docker:MariaDB:
 3306
 VM
 
 - IP-priv: 172.31.82.166
Linux:NFSServer:
22
VM

- IP-priv: 172.31.81.39
Docker:Drupal1:80
VM

- IP-priv: 172.31.86.30
Docker:Drupal2:80
VM

## Especificaciones Técnicas

Para nuestra version estos son los aspectos importantes a considerar 

### Base de datos MariaDB 

## Instalación de Docker 

Actualice el índice de paquetes apt de Ubuntu:

    sudo apt-get update

Instale algunos paquetes necesarios para permitir que apt use paquetes sobre HTTPS:

    sudo apt-get install apt-transport-https ca-certificates curl software-properties-common

Agregue la clave GPG oficial de Docker:

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

Agregue el repositorio de Docker a las fuentes de paquetes de apt:

    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

Actualice el índice de paquetes apt de Ubuntu nuevamente:

    sudo apt-get update

Instale la última versión de Docker Community Edition (CE):

    sudo apt-get install docker-ce

Verifique que Docker se ha instalado correctamente ejecutando el siguiente comando:

    sudo docker run hello-world

Se creo una instancia EC2 en AWS asociada al puerto 3306 con las especificaciones requeridas en Ubuntu 20.04 y se crea un contenedor a partir de la imagen de mariadb anteriormente descargada

    docker run --name reto3user -e MYSQL_ROOT_PASSWORD=1234 -p 3306:3306 -d mariadb
    
Verificacion del contenedor con el comando 
  
    docker ps 
    
![image](https://user-images.githubusercontent.com/68908889/232248155-58934458-21dd-4216-8620-ba19e5573300.png)
    
Inicializar base de datos

     sudo docker start reto3user
    
ejecutar base de datos 
      
       docker exec -it reto3user mysql -p


Creacion de una nueva base de datos y un usuario.

       CREATE DATABASE drupal;
       GRANT ALL PRIVILEGES ON drupal.* TO 'user'@'user' IDENTIFIED BY '<contraseña>';
       exit

### Drupal (2 Instancias)

Se crearon 2 instancias EC2 de AWS asociadas al puerto 80 y se instaló docker y la imagen de Docker de Drupal.Luego se crearon los contenedores en cada una de las instancias
          
          sudo docker run -p 80:80 --name drupal1 -d drupal
          sudo docker run -p 80:80 --name drupal2 -d drupal
          
Ahora conectaremos la instancia de la base de datos y la de archivos NFS con las instancias de Drupal

           sudo docker run -p 80:80 --name drupal1 --network=host -e DRUPAL_DATABASE_HOST=172.31.81.31 -e DRUPAL_DATABASE_USER=reto3user -e DRUPAL_DATABASE_PASSWORD=1234 -e DRUPAL_DATABASE_NAME=drupal -e DRUPAL_FILES_PATH=/mnt/nfs -e DRUPAL_FILES_NFS_SERVER=172.31.82.166 -e DRUPAL_FILES_NFS_PATH=/exports -d drupal


           sudo docker run -p 80:80 --name drupal2 --network=host -e DRUPAL_DATABASE_HOST=172.31.81.31 -e DRUPAL_DATABASE_USER=reto3user -e DRUPAL_DATABASE_PASSWORD=1234 -e DRUPAL_DATABASE_NAME=drupal -e DRUPAL_FILES_PATH=/mnt/nfs -e DRUPAL_FILES_NFS_SERVER=172.31.82.166 -e DRUPAL_FILES_NFS_PATH=/exports -d drupal

### NFS

Se creo una instancia EC2 en AWS asociada al puerto 22 (SSH) con las especificaciones requeridas en Ubuntu 20.04 y se crea un contenedor y un paquete nfs-kernel-server

     sudo apt update
     
     sudo apt install nfs-kernel-server

Después de la instalación, se configura el archivo /etc/exports para especificar qué directorios compartir a través de NFS. 

     /nfs_server *(rw,sync,no_subtree_check)

Reinicia el servicio NFS con el siguiente comando:
     
     sudo systemctl restart nfs-kernel-server

### Balanceador de cargas Apache

Se creo una instancia EC2 en AWS asociada al puerto 443 para el balanceador de cargas usando Apache, se instaló docker la imagen de Docker de Apache
Luego crearemos el directorio que almacenará la configuración

     sudo mkdir -p /usr/local/apache2/conf
  
Después se accede al archivo creado en ese directorio

     sudo nano /usr/local/apache2/conf/httpd.conf
  
 y se le da la siguiente configuración
 
        <VirtualHost *:80>
          ServerName balanceador.example.com

          <Proxy balancer://mycluster>
              # Ajusta las siguientes líneas con las IP privadas del drupal 1 y drupal2
              BalancerMember http://172.31.81.39:80
              BalancerMember http://172.31.86.30:80

              # Ajusta la siguiente línea al algoritmo de balanceo deseado
              ProxySet lbmethod=byrequests
          </Proxy>

          ProxyPass / balancer://mycluster/
          ProxyPassReverse / balancer://mycluster/
      </VirtualHost>
  
  
  
