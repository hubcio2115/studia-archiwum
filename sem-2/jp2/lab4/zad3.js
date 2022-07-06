"use strict";

const caller = (func) => {
  func();
};

const helper = () => {
  console.log("wiadomość");
};

caller(helper);
