const path = require('path');
const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');
const packageDefinition = protoLoader.
                            loadSync(path.join(__dirname, '../protos/Service.proto'));
const ServiceProto = grpc.loadPackageDefinition(packageDefinition);

const Products = [
    {
        id: 100,
        Product_id: 1000,
        title: 'Amsterdam, Luxembourg, France',
        notes: 'Fun tour'
    },
    {
        id: 200,
        Product_id: 2000,
        title: 'Italy, France, Switzerland',
        notes: 'History Tour'
    }
];

function findPorduct(call, callback) {
    let Product = Products.find(() => Product.Product_Id == call.request.id);
    if(Product) {
        callback(null, Product);
    }
    else {
        callback({
            message: 'Product not found',
            code: grpc.status.INVALID_ARGUMENT
        });
    }
}

const server = new grpc.Server();
server.addService(ProductsProto.Products.service, { find: findProduct });
server.bindAsync('0.0.0.0:8080', grpc.ServerCredentials.createInsecure(), () => {
    server.start();
});