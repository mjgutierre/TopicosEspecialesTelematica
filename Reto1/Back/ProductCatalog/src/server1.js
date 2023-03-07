import dotenv from 'dotenv';
import grpc from '@grpc/grpc-js';
import protoLoader from '@grpc/proto-loader';

dotenv.config()

var PROTO_PATH = process.env.PROTO_PATH;

const packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
    });

//var catalogproto = grpc.loadPackageDefinition(packageDefinition).catalogPackage;
var catalogproto = grpc.loadPackageDefinition(packageDefinition).catalog;

console.info("Consumer service is started...");

    const products = [
        {
          id_Product: '1',
          title: 'Product 1',
          price: 10.0
        },
        {
          id_Product: '2',
          title: 'Product 2',
          price: 20.0
        },
        {
          id_Product: '3',
          title: 'Product 3',
          price: 30.0
        }
      ];
  
      function AddProduct(call, callback) {
        const Product = call.request;
        products.push(Product);
        callback(null, {status_code: 200, title: 'Success', price: Product.price });
      }      
      
      function main() {
        const server = new grpc.Server();
        server.addService(catalogproto.ProductService.service, {
            AddProduct: AddProduct,
          });          
        server.bind("127.0.0.1:8080", grpc.ServerCredentials.createInsecure());
        server.start();
        console.log('Catalog service running on port 8080');
      }
      
      main();
   
