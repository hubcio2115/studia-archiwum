"use strict";

const getCounter = (min, max) => {
  let count = min - 1;

  return () => (count + 1 > max ? undefined : ++count);
};

const counter = getCounter(5, 7);

console.log(counter());
console.log(counter());
console.log(counter());
console.log(counter());
