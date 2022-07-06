"use strict";

const printElements = (arr) => {
  arr.map((element, index) => {
    console.log(`"rząd ${index}"`);

    element.map((thing) => {
      console.log(`"${thing}"`);
    });
  });
};

const arr = [
  [1, 2, 1, 24],
  [8, 11, 9, 4],
  [7, 0, 7, 27],
  [7, 4, 28, 14],
  [3, 10, 26, 7],
];

printElements(arr);
