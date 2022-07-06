"use strict";
const func1 = (init, cb) => {
  cb(init + 10);
};

const func2 = (init, cb) => {
  cb(init + 20);
};

const cb = (init) => init + 30;

const oneAfterAnother = (func1, func2, cb) => {
  func1(0, (result) => {
    func2(result, (result1) => {
      console.log(cb(result1));
    });
  });
};

oneAfterAnother(func1, func2, cb);
