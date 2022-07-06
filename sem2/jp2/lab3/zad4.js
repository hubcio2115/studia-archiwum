"use strict";

const counter = (arr) => {
  const counters = {};
  for (const element of arr) {
    counters[element] ? (counters[element] += 1) : (counters[element] = 1);
  }

  return counters;
};

console.log(counter(["js", "react", "js", "angular", "angular", "js"]));
