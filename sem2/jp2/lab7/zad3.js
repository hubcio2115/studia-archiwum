"use strict";
import { lp3 } from "./zad2/toplist.js";

// 6
((n, min, max) => {
  const helper = lp3.slice(min, max);
  Array.from(Array(n)).forEach(() => {
    console.log(helper[Math.floor(Math.random() * helper.length)]);
  });
})(5, 4, 10);

// 7
lp3.slice(0, 10).forEach((element, index) => {
  setTimeout(() => {
    console.log(element);
  }, 2000 * (index + 1));
});

// 10
const groupedByAuthor = lp3.reduce((acc, element) => {
  acc[element.author]
    ? acc[element.author].push({
        song: element.song,
        place: element.place,
      })
    : (acc[element.author] = [{ song: element.song, place: element.place }]);
  return acc;
}, {});
console.log(groupedByAuthor);
