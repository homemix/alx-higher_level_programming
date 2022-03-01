#!/usr/bin/node

let n = 0;
exports.logMe = function (item) {
  console.log(`${n}: ${item}`);
  n++;
};
const logMe = require('./9-logme').logMe;

logMe('Hello');
logMe('Best');
logMe('School');
