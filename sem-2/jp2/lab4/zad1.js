"use strict";

const helper = (num1) => {
  let num2 = 10;
  return ((num1) => {
    return num1 + num2;
  })(num1);
};

console.log(helper(10));
