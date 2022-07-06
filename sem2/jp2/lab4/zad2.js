"use strict";

((string) => {
  const result = string
    .split(" ")
    .reduce((prev, curr) => (prev.length < curr.length ? curr : prev));

  console.log(result);
})("Ala kota ma");
