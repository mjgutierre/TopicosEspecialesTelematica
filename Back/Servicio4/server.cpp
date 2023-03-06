//El server llama uno o varios servicios 
//https://www.google.com/search?q=grpc+en+c%2B%2B&client=opera-gx&biw=1325&bih=619&tbm=vid&sxsrf=AJOqlzV0uTNVHAlXimS9SQZESvMC03ko2w%3A1677864203300&ei=Cy0CZNjxEbKokvQPxb6a6A8&ved=0ahUKEwiYo8aeo8D9AhUylIQIHUWfBv04FBDh1QMIDA&uact=5&oq=grpc+en+c%2B%2B&gs_lcp=Cg1nd3Mtd2l6LXZpZGVvEAMyCAghEKABEMMEOgQIIxAnUI4CWI4CYIYHaABwAHgAgAGpAYgBswOSAQMwLjOYAQCgAQHAAQE&sclient=gws-wiz-video#fpstate=ive&vld=cid:b0f920f7,vid:RuLar8WVWG4
#include<iostream>
#include <grpcpp/grpcpp.h>
#include "Service.grpc.pb.h"

using grpc::Server;
using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::Status;
using Service::ProductService;
using Service::TransactionRequest;
using Service::TransactionResponse;

// Definir la implementación del servicio ProductService
class ProductServiceServiceImpl final : public ProductService::Service {
public:
  Status AddProduct(ServerContext* context, const TransactionRequest* request, TransactionResponse* response) override {
    std::cout << "Request is received: " << request->DebugString() << std::endl;
    response->set_status_code(1);
    return Status::OK;
  }
};

void RunServer() {
  std::string server_address("[::]:8080");
  ProductServiceServiceImpl service;

  // Configurar el servidor gRPC
  grpc::ServerBuilder builder;
  builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
  builder.RegisterService(&service);
  std::unique_ptr server(builder.BuildAndStart());
  std::cout << "Service is running on..." << server_address  << std::endl;
  server->Wait();
}

int main(int argc, char** argv) {
  RunServer();

  return 0;
}
