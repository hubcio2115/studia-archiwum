"use strict";

const func1 = () =>
  new Promise((resolve) => {
    resolve(0);
  });

const func2 = (init) =>
  new Promise((resolve) => {
    resolve(init + 1);
  });

const func3 = (init) =>
  new Promise((resolve) => {
    resolve(init + 2);
  });

const callback = (result) => {
  console.log(result);
};

const poKolei = (fun1, fun2, fun3, cb) => {
  fun1().then((res1) => {
    fun2(res1).then((res2) => {
      fun3(res2).then((res) => {
        cb(res);
      });
    });
  });
};

poKolei(func1, func2, func3, callback);
