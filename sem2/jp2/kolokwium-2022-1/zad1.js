"use strict";

import { series } from "./series.js";

const miniSeries = series
  .reduce((acc, serial) => {
    const { name, startYear: year, type } = serial;

    return serial.endYear === serial.startYear
      ? [...acc, { name, type, year }]
      : acc;
  }, [])
  .sort((a, b) => a.name.localeCompare(b.name));

console.log(miniSeries);

const sortedSeries = [...series].sort((a, b) => {
  if (a.endYear === null) return -1;
  if (b.endYear === null) return 1;

  if (a.startYear > b.startYear) return 1;
  if (a.startYear < b.startYear) return -1;

  if (a.startYear === b.startYear) {
    if (a.endYear > b.endYear) return 1;
    if (a.endYear < b.endYear) return -1;
  }
});

const mySeries = sortedSeries.reduce(
  (acc, serial) => {
    const { id, name, startYear, endYear, type, seasons } = serial;

    const tempType = type.reduce((acc, typ, index) => {
      typ.length - 1 === index ? acc + typ : acc + typ + ", ";
    }, "");

    let temp;
    endYear
      ? (temp = {
          id,
          name,
          startYear,
          endYear,
          type: tempType,
          seasons,
        })
      : (temp = {
          id,
          name,
          startYear,
          type: tempType,
          seasons,
        });

    if (serial.startYear < 2010) acc[0].push(temp);
    else if (serial.startYear > 2010 && serial.startYear < 2020)
      acc[1].push(temp);
    else if (serial.startYear > 2020) acc[2].push(temp);

    return acc;
  },
  [[], [], []]
);

console.log(mySeries);
