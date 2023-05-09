## ProductOrder

### Clonar el repositorio y dirigirse a la carpeta

    git clone https://github.com/mjgutierre/TopicosEspecialesTelematica.git
    
### Instalar dependencias 

    cd Reto1/Back/Gateway/env 
    sudo apt update
    sudo apt install python3-pip
    pip install -r requirements.txt
    
### Cambiar la IP y Puerto del microservicio 

    cd Reto1/Back/ProductOrder/src
    sudo nano .server.py

Y cambiar la siguiente linea

    HOST = '[::]:50052'

### Iniciar el microservicio
    cd Reto1/Back/ProductOrder/Src
    py server.py
    
