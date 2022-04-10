const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => res.send('Hello Holberton School!'));

app.get('/students', async (req, res) => {
  try {
    const obj = await countStudents(process.argv[2]);
    let number = 0;
    for (const ele of Object.values(obj)) number += ele.length;
    const list = [];
    list.push(`This is the list of our students\nNumber of students: ${number}`);
    for (const key of Object.keys(obj)) {
      list.push(`\nNumber of students in ${key}: ${obj[key].length}. List: ${obj[key].join(', ')}`);
    }
    res.send(list.join(''));
  } catch (error) {
    res.send(`\n${error.message}`);
  }
});

app.listen(1245);

module.exports = app;
