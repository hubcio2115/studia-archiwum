"use strict";
import { hogwardArray } from "./potter.js";

const resultArray = hogwardArray.reduce((acc, curr) => {
  if (acc[curr.house] === undefined) acc[curr.house] = [];

  const { name, hogwartsStaff, hogwartsStudent } = curr;

  let type = "none";
  if (hogwartsStaff) type = "staff";
  else if (hogwartsStudent) type = "student";

  acc[curr.house].push({ name, type });

  return acc;
}, {});

console.log(resultArray);
