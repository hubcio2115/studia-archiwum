// Autor: Paweł Olszko
"use strict";

const array = [4, 2, "a", "b", 3, "aa", "ww", 2, "ab", -2];

for (let i = 0; i < array.length; i++) {
  if (typeof array[i] !== "number") {
    for (let j = i + 1; j < n; j++) {
      if (typeof array[j] === "number") {
        let temp = array[i];
        array[i] = array[j];
        array[j] = temp;
        break;
      }
    }
  }
}

console.log(array);
