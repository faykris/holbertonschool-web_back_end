const http = require('http');
const countStudents = require('./3-read_file_async');

http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  if (req.url === '/') {
    res.write('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students');
    try {
      const obj = await countStudents(process.argv[2]);
      let number = 0;
      for (const ele of Object.values(obj)) number += ele.length;
      res.write(`\nNumber of students: ${number}`);
      for (const key of Object.keys(obj)) {
        res.write(`\nNumber of students in ${key}: ${obj[key].length}. List: ${obj[key].join(', ')}`);
      }
    } catch (error) {
      res.end(error.message);
    }
  }
  res.end();
}).listen(1245);
