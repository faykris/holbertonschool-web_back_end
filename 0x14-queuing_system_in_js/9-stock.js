import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4,
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10,
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2,
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5,
  },
];

function getItemById(id) {
  for (const product of listProducts) {
    if (id === product.id) return product;
  }
  return undefined
}

/********** REDIS **********/
const client = redis.createClient();
const GET_ASYNC = promisify(client.get).bind(client);

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const item = await GET_ASYNC(`item.${itemId}`);
  return item;
}

/********* EXPRESS *********/
const app = express();

app.listen(1245);

app.get('/list_products', function (req, res) {
  let list_products = [];
  for (const product of listProducts) {
    let product_obj = {}
    product_obj.itemId = product.id;
    product_obj.itemName = product.name;
    product_obj.price = product.price;
    product_obj.initialAvailableQuantity = product.stock;
    list_products.push(product_obj);
  }
  res.json(list_products);
});

app.get('/list_products/:itemId', async function (req, res) {
  const itemId = Number(req.params.itemId);
  const product = getItemById(itemId);
  let product_obj = {}
  if (product !== undefined) {
    product_obj.itemId = product.id;
    product_obj.itemName = product.name;
    product_obj.price = product.price;
    product_obj.initialAvailableQuantity = product.stock;

    const currentStock = await getCurrentReservedStockById(itemId);
    const stock = currentStock !== null ? currentStock : product_obj.initialAvailableQuantity;

    product_obj.currentQuantity = stock;

    res.json(product_obj);
  }
  else {
    res.json({ "status": "Product not found" });
  }
});

app.get('/reserve_product/:itemId', async function (req, res) {
  const itemId = Number(req.params.itemId);
  const product = getItemById(itemId);

  if (product !== undefined) {
    let currentStock = await getCurrentReservedStockById(itemId);
    if (currentStock === null) currentStock = product.stock;

    if (currentStock > 0) {
      reserveStockById(itemId, Number(currentStock) - 1);
      res.json({ status: 'Reservation confirmed', itemId });
    }
    else {
      res.json({ status: 'Not enough stock available', itemId });
      return;
    }
  }
  else {
    res.json({ "status": "Product not found" });
  }
});