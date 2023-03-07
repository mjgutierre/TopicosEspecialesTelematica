from flask import Flask, request, jsonify
import grpc
import catalog_pb2
import catalog_pb2_grpc
import order_pb2
import order_pb2_grpc

app = Flask(__name__)

# Conexión al servidor de catálogo
catalog_channel = grpc.insecure_channel('localhost:50051')
catalog_stub = catalog_pb2_grpc.ProductServiceStub(catalog_channel)

# Conexión al servidor de órdenes
order_channel = grpc.insecure_channel('localhost:50052')
order_stub = order_pb2_grpc.OrderServiceStub(order_channel)

@app.route('/catalog', methods=['POST'])
def add_product():
    # Parseamos los datos recibidos desde el cliente
    data = request.get_json()
    id_Product = data.get('id_Product')
    price = data.get('price')
    title = data.get('title')

    # Creamos el producto utilizando el stub de gRPC
    response = catalog_stub.AddProduct(catalog_pb2.Product(
        id_Product=id_Product,
        price=price,
        title=title
    ))

    return jsonify({'id_Product': 'HOLA'})#response.product_id})

@app.route('/order', methods=['POST'])
def create_order():
    # Parseamos los datos recibidos desde el cliente
    data = request.get_json()
    customer_name = data.get('customer_name')
    id_Product = data.get('id_Product')
    quantity = data.get('quantity')

    # Creamos la orden utilizando el stub de gRPC
    response = order_stub.CreateOrder(order_pb2.ProductOrder(
        customer_name=customer_name,
        id_Product=id_Product,
        quantity=quantity
    ))

    return jsonify({'order_id': 'HOLA2'})#response.order_id})

if __name__ == '__main__':
    app.run(debug=True)
