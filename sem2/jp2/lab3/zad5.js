"use strict";

const unequal = (arg1, arg2, arg3) => {
  return arg1 === arg2 || arg2 === arg3 || arg1 === arg3 ? false : true;
};

console.log(unequal(1, 2, 3));
