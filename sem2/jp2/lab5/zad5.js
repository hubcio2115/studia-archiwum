"use strict";

const wishlist = [
  { name: "Czajnik", netto: 100 },
  { name: "Lodówka", netto: 2730 },
  { name: "Mikrofalówka", netto: 940 },
  { name: "Mikser", netto: 120 },
  { name: "Piekarnik", netto: 3100 },
  { name: "Zmywarka", netto: 2400 },
  { name: "Toster", netto: 260 },
];

// a
const prices = wishlist.reduce((acc, current) => {
  return acc + current.netto * 1.23;
}, 0);

console.log(prices);

// b
const nettoPrices = wishlist.reduce((acc, current) => {
  return [...acc, { [current.name]: current.netto }];
}, []);

console.log(nettoPrices);

// c
const newArray = (arr, util) => {
  return arr.reduce((acc, current) => {
    return [...acc, util(current)];
  }, []);
};

console.log(newArray(wishlist, (x) => `${x.name}: ${x.netto}`));

// d
const newArrayMap = (arr, util) => {
  return arr.map((element) => {
    return util(element);
  });
};

console.log(newArrayMap(wishlist, (x) => `${x.name}: ${x.netto}`));

// e
const thingsThatCanBeBought = (wishlist, util) => {
  return wishlist.reduce((acc, current) => {
    return util(current) ? [...acc, current] : acc;
  }, []);
};

console.log(thingsThatCanBeBought(wishlist, (x) => x.netto < 500));
