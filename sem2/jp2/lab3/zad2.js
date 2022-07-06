"use strict";

const isPositiveEven = (number) => {
  return number % 2 === 0 && number > 0;
};

console.log(isPositiveEven(-10));
