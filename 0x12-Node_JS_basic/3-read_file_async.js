module.exports = async function countStudents (path) {
  const fs = require('fs').promises;
  await fs.readFile(path, 'binary')
    .then((data) => {
      const lines = data.split('\n');
      lines.splice(0, 1);
      for (let i = lines.length - 1; i >= 0; i--) {
        if (lines[i].length === 0) lines.splice(i, 1);
      }
      const number = lines.length;
      const obj = {};
      for (const line of lines) {
        const row = line.split(',');
        if (!obj[row[3]]) obj[row[3]] = [];
        obj[row[3]].push(row[0]);
      }
      if (number > 0) {
        console.log(`Number of students: ${number}`);
        for (const key in obj) {
          console.log(`Number of students in ${key}: ${obj[key].length}. List: ${obj[key].join(', ')}`);
        }
      }
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
};
