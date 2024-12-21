#!/usr/bin/node
// Defines a Rectangle class with width and height attributes

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
    // Otherwise, do not initialize properties, leaving the object empty
  }

  // Method to print the rectangle using 'X'
  print() {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}

module.exports = Rectangle;

