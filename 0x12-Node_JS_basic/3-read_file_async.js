// File System Module
const fs = require('fs');

const countStudents = async (path) => {
  try {
    // Read file
    const data = await fs.promises.readFile(path, 'utf8');
    const columns = data.split('\n').slice(1, data.length);
    let counter = 0;
    const fields = {};
    const message = [];
    let msg = '';
    for (const i of columns) {
      if (i) {
        counter += 1;
      }
      const row = i.split(',');
      if (!fields[row[3]] && row[3]) {
        fields[row[3]] = [];
      }
      if (row[0]) {
        fields[row[3]].push(row[0]);
      }
    }
    console.log(`Number of students: ${counter}`);
    message.push(`Number of students: ${counter}`);
    for (const [key, value] of Object.entries(fields)) {
      if (key) {
        msg = `Number of students in ${key}: ${value.length}. List: ${value.join(', ')}`;
        console.log(msg);
        message.push(msg);
      }
    }
    return message.join('\n');
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};

module.exports = countStudents;
