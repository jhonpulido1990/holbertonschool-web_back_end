const express = require('express');
const fs = require('fs');
const util = require('util');

const readFile = util.promisify(fs.readFile);

function countStudents(file) {
  return readFile(file, 'utf8').then((data) => {
    const classroom = {};
    let seats = 0;
    let message = `Number of students: ${seats}\n`;
    const sep = data.split('\n');
    const students = sep.slice(1).map((seat) => seat.split(',')).filter((seat) => seat.length > 0 && seat[0] !== '');

    for (const student of students) {
      seats += 1;
      if (!(student[3] in classroom)) {
        classroom[student[3]] = [];
      }
      classroom[student[3]].push(student[0]);
    }

    message = `Number of students: ${seats}\n`;
    for (const name of Object.keys(classroom)) {
      message += `Number of students in ${name}: ${classroom[name].length}. List: ${classroom[name].join(', ')}\n`;
    }
    return message.slice(0, -1);
  }).catch(() => 'Cannot load the database');
}

const app = express();
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.send(`This is the list of our students\n${await countStudents(process.argv[2])}`);
});

app.listen(1245);
module.exports = app;
