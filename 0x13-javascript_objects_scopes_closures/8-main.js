#!/usr/bin/node
const esrever = require('./8-esrever').esrever;

console.log(esrever([1, 2, 3, 4, 5])); // [ 5, 4, 3, 2, 1 ]
console.log(esrever(["School", 89, { id: 12 }, "String"])); // [ 'String', { id: 12 }, 89, 'School' ]

