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
}

module.exports = Rectangle;

