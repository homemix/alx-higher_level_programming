#!/usr/bin/node

const myArgs = process.argv;

if (myArgs[2] === undefined || isNaN(myArgs[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myArgs[2]; i++) {
    console.log('X'.repeat(myArgs[2]));
  }
}
