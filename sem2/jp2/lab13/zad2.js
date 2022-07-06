"use strict";
const funcArr1 = [async () => 1 + 1, async () => 2 + 2];
const funcArr2 = [async () => 2 + 2, async () => 3 + 3];

const group = (funcArr1, funcArr2, cb) => {
  const funcArr = funcArr1.length >= funcArr2.length ? funcArr1 : funcArr2;
  funcArr.forEach((func, index) => {
    const temp =
      funcArr2[index] === undefined ? async () => 0 : funcArr2[index];
    Promise.all([func(), temp()]).then((res) => {
      const [x, y] = res;
      console.log(cb(x, y));
    });
  });
};

group(funcArr1, funcArr2, (x, y) => x + y);
group(funcArr1, funcArr1.slice(0, 1), (x, y) => x + y);
