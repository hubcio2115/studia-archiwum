"use strict";

const result = (funTab1, funTab2, process) => {
  const [funArr1, funArr2] =
    funTab1.length >= funTab2 ? [funTab1, funTab2] : [funTab2, funTab1];

  const result = [];
  funArr1.forEach((func, index) => {
    const func2 = funArr2[index] !== undefined ? funArr2[index] : () => 0;

    Promise.all([func(), func2()]).then((res) => {
      const [res1, res2] = res;

      result.push(process(res1, res2));

      if (result.length === funArr1.length) {
        console.log(result);
      }
    });
  });
};

const tab1 = [
  () =>
    new Promise((resolve) => {
      resolve(1);
    }),
  () =>
    new Promise((resolve) => {
      resolve(2);
    }),
];

const tab2 = [
  () =>
    new Promise((resolve) => {
      resolve(3);
    }),
  () =>
    new Promise((resolve) => {
      resolve(4);
    }),
  () =>
    new Promise((resolve) => {
      resolve(5);
    }),
];

const process = (wyn1, wyn2) => wyn1 + wyn2;

result(tab1, tab2, process);
