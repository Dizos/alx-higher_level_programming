#!/usr/bin/node
// Defines a Rectangle class with additional methods

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }

  // Method to print the rectangle using 'X'
  print() {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  // Method to swap the width and height
  rotate() {
    if (this.width && this.height) {
      const temp = this.width;
      this.width = this.height;
      this.height = temp;
    }
  }

  // Method to double the width and height
  double() {
    if (this.width && this.height) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

module.exports = Rectangle;

