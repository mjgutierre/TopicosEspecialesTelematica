from flask import Flask, request, jsonify
#Librerias y protobufs 
import grpc
import catalog_pb2
import catalog_pb2_grpc
import order_pb2
import order_pb2_grpc

app = Flask(__name__)

# Conexión al servidor de catálogo y catalogo con la descripcion de sus puertos 
catalogCanalComuni = grpc.insecure_channel('localhost:50051')
orderCanalComuni = grpc.insecure_channel('localhost:50052')
orderCliente = order_pb2_grpc.OrderServiceStub(orderCanalComuni)
catalogCliente = catalog_pb2_grpc.ProductServiceStub(catalogCanalComuni)

#Creacion de las rutas para la aplicacion con sus metodos y llamadas desde el cliente al servidor
#RUTA DE CATALOGO
@app.route('/catalog', methods=['POST'])
def add_product():
    # datos recibidos desde el cliente
    data = request.get_json()
    id_Product = data.get('id_Product')
    price = data.get('price')
    title = data.get('title')

    # En nuestro caso añadimos el producto al catalogo 
    response = catalogCliente.AddProduct(catalog_pb2.Product(
        id_Product=id_Product,
        price=price,
        title=title
    ))
    #respuesta del json, retornara el id_product
    return jsonify({'id_Product': response.status_code})

#RUTA DE ORDEN
@app.route('/order', methods=['POST'])
def create_order():
    data = request.get_json()
    title = data.get('title')
    id_Product = data.get('id_Product')
    quantity = data.get('quantity')

    response = orderCliente.CreateOrder(order_pb2.ProductOrder(
        title=title,
        id_Product=id_Product,
        quantity=quantity
    ))

    return jsonify({'order_id': response.status_code})

#MAIN
if __name__ == '__main__':
    app.run(debug=True)