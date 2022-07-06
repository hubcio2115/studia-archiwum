"use strict";

const myFilter = (arr, util) => {
  return arr.reduce((acc, current) => {
    if (util(current) && acc === undefined) return current;
    return acc;
  }, undefined);
};

const arr = ["Ala", "Kot", "Pies"];
console.log(myFilter(arr, (x) => x === "Ala"));
