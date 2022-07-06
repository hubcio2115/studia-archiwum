"use strict";

const NWD = (a, b) => {
  const helper = (a, b) => {
    return a - b === 0
      ? a
      : helper(Math.max(a, b) - Math.min(a, b), Math.min(a, b));
  };

  return helper(a, b);
};

console.log(NWD(48, 18));
