#!/usr/bin/node
// Defines a Square class that inherits from Square in 5-square.js

const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint(c) {
    // Use 'X' if c is undefined
    const char = c || 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;

