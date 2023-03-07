import grpc from '@grpc/grpc-js';
import protoLoader from '@grpc/proto-loader';

var PROTO_PATH="../protobufs/catalog.proto"

const packageDefinition = protoLoader.loadSync(PROTO_PATH);
const catalog = grpc.loadPackageDefinition(packageDefinition);

const server = new grpc.Server();

server.addService(catalog.ProductService.service, {
  AddProduct: async (call) => {
    const { id_Product, title, price } = call.request;
    console.log(`Adding product ${title} with id ${id_Product} and price ${price}`);
    return{ status_code: 200, title, price };
  }
});

const port = 8080;
  server.bindAsync(`0.0.0.0:${port}`, grpc.ServerCredentials.createInsecure(), () => {
  console.log(`Server running on port ${port}`);
  server.start();
});