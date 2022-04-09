const http = require('http');

module.exports = http.createServer((req, res) => {
  res.end('Hello Holberton School!');
}).listen(1245);
