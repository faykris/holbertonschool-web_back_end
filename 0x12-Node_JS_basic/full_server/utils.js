const fs = require('fs');

export default function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(Error(err));
        return;
      }
      const lines = data.split('\n');
      lines.splice(0, 1);
      for (let i = lines.length - 1; i >= 0; i -= 1) {
        if (lines[i].length === 0) lines.splice(i, 1);
      }
      const obj = {};
      for (const line of lines) {
        const row = line.split(',');
        if (!obj[row[3]]) obj[row[3]] = [];
        obj[row[3]].push(row[0]);
      }
      resolve(obj);
    });
  });
}
