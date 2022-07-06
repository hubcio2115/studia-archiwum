"use strict";

const toArray = (arg1, arg2) => {
  return [].concat(arg1, arg2);
};

console.log(toArray("js", [1, 2, 3]));
