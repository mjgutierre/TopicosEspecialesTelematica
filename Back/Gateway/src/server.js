const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');

const app = express();
app.use(bodyParser.json());
app.use(cors());

const catalogPackageDefinition = protoLoader.loadSync('../protobufs/catalog.proto');
const catalogProtoDescriptor = grpc.loadPackageDefinition(catalogPackageDefinition);
const catalogClient = new catalogProtoDescriptor.Catalog('localhost:8080', grpc.credentials.createInsecure());

const orderPackageDefinition = protoLoader.loadSync('order.proto');
const orderProtoDescriptor = grpc.loadPackageDefinition(orderPackageDefinition);
const orderClient = new orderProtoDescriptor.Order('localhost:8080', grpc.credentials.createInsecure());

const gatewayPackageDefinition = protoLoader.loadSync('../protobufs/Service.proto');
const gatewayProtoDescriptor = grpc.loadPackageDefinition(gatewayPackageDefinition);

app.get('/ProductCatalog', (req, res) => {
  catalogClient.GetCatalogItems({}, (error, response) => {
    if (error) {
      res.status(500).send({ error: error.message });
    } else {
      res.send({ items: response.items });
    }
  });
});

app.get('/ProductOrder', (req, res) => {
  orderClient.GetOrderItems({}, (error, response) => {
    if (error) {
      res.status(500).send({ error: error.message });
    } else {
      res.send({ items: response.items });
    }
  });
});

const server = new grpc.Server();
server.addService(gatewayProtoDescriptor.Gateway.service, {
  GetCatalogItems: (call, callback) => {
    catalogClient.GetCatalogItems({}, (error, response) => {
      if (error) {
        callback(error);
      } else {
        callback(null, response);
      }
    });
  },
  GetOrderItems: (call, callback) => {
    orderClient.GetOrderItems({}, (error, response) => {
      if (error) {
        callback(error);
      } else {
        callback(null, response);
      }
    });
  }
});
server.bind('127.0.0.1:8080', grpc.ServerCredentials.createInsecure());
server.start();
