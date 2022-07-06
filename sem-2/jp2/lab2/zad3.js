"use strict";

const testArray = [
  1,
  2,
  null,
  [4, undefined, 11, 10],
  6,
  [7, null, 0],
  null,
  9,
];

const newArray = [];
for (const element of testArray) {
  if (typeof element !== "object" || element === null) {
    newArray[newArray.length] = element;
    continue;
  }

  for (let i = 0; i < element.length; i++) {
    newArray[newArray.length] = element[i];
  }
}

console.log(newArray);
