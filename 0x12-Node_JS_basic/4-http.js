const http = require('http');

const server = http.createServer((req, res) => {
  res.end('Hello Holberton School!');
}).listen(1245);
