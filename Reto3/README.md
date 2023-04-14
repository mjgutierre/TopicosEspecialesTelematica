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

## Especificaciones Técnicas

Para nuestra version estos son los aspectos importantes a considerar 

- Para cada una de las instancias se configuraron los archivos docker-compose.yml que se podran encontrar en este repositorio
