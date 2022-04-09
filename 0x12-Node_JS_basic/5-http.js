const http = require('http');
const countStudents = require('./3-read_file_async');

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  if (req.url === '/') {
    res.write('Hello Holberton School!');
  }
  else if (req.url === '/students') {
    res.write('This is the list of our students');
    countStudents("database.csv")
  }
  res.end();
}).listen(1245);
