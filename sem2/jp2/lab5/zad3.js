"use strict";

const arr = [1, 2, 3, 4, 5];

const result = arr.reduce((_, current, index) => {
  console.log(`${index}: ${current}`);
}, 0);
