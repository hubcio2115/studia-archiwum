"use strict";

const detectChanges = (original, modified) => {
  const keys = Object.keys(original);

  return keys.reduce((acc, key) => {
    return JSON.stringify(original[key]) === JSON.stringify(modified[key])
      ? acc
      : [...acc, [key, modified[key]]];
  }, []);
};

const object1 = {
  id: 2,
  name: "Przyjaciele",
  startYear: 1994,
  endYear: 2004,
  type: ["Komedia"],
  seasons: 10,
};

const object2 = {
  id: 2,
  name: "Przyjaciele edytowany",
  startYear: 1994,
  endYear: 2010,
  type: ["Komedia"],
  seasons: 10,
};

console.log(detectChanges(object1, object2));

const object3 = {
  value: {
    field: "old value",
  },
  name: "test",
};

const object4 = {
  value: {
    field: "new value",
  },
  name: "test",
};

console.log(detectChanges(object3, object4));
