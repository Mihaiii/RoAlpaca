const fs = require('fs');
const mySet1 = new Set();

let rawdata = fs.readFileSync('data/dataset_flat.json');
let arrayData = JSON.parse(rawdata);

arrayData.forEach((z) => Object.keys(z).forEach((y) => mySet1.add(y)));

console.log(mySet1);