#!/usr/bin/node

module.exports = class Square extends require('./5-square.js') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      if (c !== undefined) {
        console.log(c.repeat(this.width));
      } else {
        console.log('X'.repeat(this.width));
      }
    }
  }
};
