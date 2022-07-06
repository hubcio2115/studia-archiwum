"use strict";

const arr = [1, 2, 3, 4, 5];

const sum = arr.reduce((acc, current) => {
  return acc + current;
}, 0);

console.log(sum);
