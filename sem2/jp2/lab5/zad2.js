"use strict";

const arr = [-1, 2, -3, 4, -5];

const result = arr.reduce((acc, current) => {
  return current < 0 ? acc : [...acc, current * current];
}, []);

console.log(result);
