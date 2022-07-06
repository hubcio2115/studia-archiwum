"use strict";

const arr = [
  { id: "abc", name: "Ala" },
  { id: "def", name: "Tomek" },
  { id: "ghi", name: "Jan" },
];

const res = arr.reduce((acc, current) => {
  return [...acc, { [current.id]: { ...current } }];
}, []);

console.log(res);
