const arr = [1, 5, 6, 5, 5, 1, 5];

const counters = {};
for (const num of arr) {
  if (counters[num]) {
    counters[num] += 1;
  } else {
    counters[num] = 1;
  }
}

Object.entries(counters).map((counter) => {
  console.log(
    `${counter[0]} pojawia się ${counter[1]} ${
      counter[1] === 1 ? "raz" : "razy"
    }.`
  );
});
