"use strict";

const numbers = [4, 3, 5, 1, 3, 2, 21, 1, 65, -43, 9];

const uniqs = [];
let helper = true;
for (const number of numbers) {
  for (const uniq of uniqs) {
    if (uniq === number) helper = false;
  }
  if (helper) uniqs[uniqs.length] = number;
  helper = true;
}

console.log(uniqs);
