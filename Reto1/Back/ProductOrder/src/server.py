from concurrent import futures
import grpc

import catalog_pb2
import catalog_pb2_grpc
import order_pb2
import order_pb2_grpc

HOST = '[::]:50052'

class ProductService(catalog_pb2_grpc.ProductServiceServicer):
   def AddProduct(self, request, context):
      print("Request is received: " + str(request))
      return catalog_pb2.TransactionResponse(status_code=0)
 
class OrderService(order_pb2_grpc.OrderServiceServicer):
   def CreateOrder(self, request, context):
      print("Request is received: " + str(request))
      return order_pb2.OrderResponse(status_code=1)
 

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  catalog_pb2_grpc.add_ProductServiceServicer_to_server(ProductService(), server)
  order_pb2_grpc.add_OrderServiceServicer_to_server(OrderService(), server)
  server.add_insecure_port(HOST)
  print("Service is running... ")
  server.start()
  server.wait_for_termination()

if __name__ == "__main__":
    serve()