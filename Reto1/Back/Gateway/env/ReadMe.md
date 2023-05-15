## Gateway

### Clonar el repositorio y dirigirse a la carpeta

    git clone https://github.com/mjgutierre/TopicosEspecialesTelematica.git
    
### Instalar las dependencias para el microservicio
    cd TopicosEspecialesTelematica/Reto1/Back/Gateway/env 
    sudo apt update
    sudo apt install python3-pip
    pip install -r requirements.txt
      
### Cambiar Puertos e IP

    cd TopicosEspecialesTelematica/Reto1/Back/Gateway/env/src
    sudo nano server1.py
    
  Y cambiar la siguiente linea 
 
    catalogCanalComuni = grpc.insecure_channel('localhost:50051')
    orderCanalComuni = grpc.insecure_channel('localhost:50052')

### Iniciar el microservicio

    cd TopicosEspecialesTelematica/Reto1/Back/Gateway/env/src
    pyton3 server1.py
