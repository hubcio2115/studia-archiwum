"use strict";
import { lp3 } from "./toplist.js";
import _ from "lodash";

// 1
const queen = _.filter(lp3, (element) => element.author === "Queen");
console.log(queen);

// 2
const pinkFloyd = _.filter(lp3, (element) => {
  return element.author === "Pink Floyd" && element.change >= 10;
});
console.log(pinkFloyd);

// 3
const n = 5;
const sortedByChange = _.chain(lp3)
  .orderBy((element) => element.change, "asc")
  .dropRight(n);
console.log(sortedByChange.value());

// 4
const head = _.head(lp3);
const first = {
  author: head?.author,
  song: head?.song,
};
console.log(first);

// 5
const nums = [1, 2, 3, 4, 5];
_.every(nums, (number) => typeof number === "number")
  ? ((numbers) => {
      _.map(numbers, (number) => {
        console.log(lp3[number]);
      });
    })(nums)
  : null;

// 6
((n, min, max) => {
  const helper = _.slice(lp3, min, max);
  Array.from(Array(n)).forEach(() => {
    console.log(helper[_.floor(_.random(1, true) * helper.length)]);
  });
})(5, 4, 10);

// 7
_.forEach(_.slice(lp3, 0, 10), (element, index) => {
  _.delay(() => {
    console.log(element);
  }, 2000 * (index + 1));
});

// 8
const decrease = _.filter(lp3, (element) => element.change < 0);
console.log(decrease);

// 9
const newLp3 = _.reduce(
  lp3,
  (acc, element) => {
    return { ...acc, [element.song]: { ...element } };
  },
  {}
);
console.log(newLp3);

// 10
const groupedByAuthor = _.reduce(
  lp3,
  (acc, element) => {
    acc[element.author]
      ? acc[element.author].push({
          song: element.song,
          place: element.place,
        })
      : (acc[element.author] = [{ song: element.song, place: element.place }]);
    return acc;
  },
  {}
);
console.log(groupedByAuthor);

// 11
const counter = _.countBy(lp3, (element) => element.author);
console.log(counter);

// 12
const biggestChanges = [
  _.minBy(lp3, (element) => element.change),
  _.maxBy(lp3, (element) => element.change),
];
console.log(biggestChanges);
