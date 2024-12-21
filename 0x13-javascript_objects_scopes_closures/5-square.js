#!/usr/bin/node
// Defines a Square class that inherits from Rectangle

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor(size) {
    // Call the constructor of Rectangle with both width and height equal to size
    super(size, size);
  }
}

module.exports = Square;

