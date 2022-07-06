"use strict";
const together = async (promisesTab, callback) => {
  const results = promisesTab.map(async (func) => {
    return await func();
  });
  return callback(results);
};

(async () => {
  console.log(
    await together([async () => 10, async () => 11], async (results) => {
      return await results.reduce(async (acc, current) => {
        return (await acc) + (await current);
      }, Promise.resolve(0));
    })
  );
})();

const razem = (promisesTab, callback) => {
  const results = [];
  for (let i = 0; i < promisesTab.length; i++) {
    console.log(i);
    promisesTab[i].then((response) => {
      console.log(response);
      results.push(response);
      if (results.length === promisesTab.length) {
        callback(results);
      }
    });
  }
};
