"use strict";

const mySum = (arr) => {
  const helper = (arr, acc = 0) => {
    return arr.length !== 0 ? helper(arr.slice(1), acc + arr[0]) : acc;
  };

  return helper(arr);
};

console.log(mySum([1, 2, 3, 4, 5]));
