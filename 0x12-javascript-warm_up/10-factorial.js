#!/usr/bin/node

function factorial (n) {
  // Handle base cases: NaN, 0, and 1
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  // Recursive case
  return n * factorial(n - 1);
}

const num = parseInt(process.argv[2]);
console.log(factorial(num));
