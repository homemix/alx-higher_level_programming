#!/usr/bin/node

const myArgs = process.argv;

if (myArgs[2] === undefined || isNaN(myArgs[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(myArgs[2]));
}
