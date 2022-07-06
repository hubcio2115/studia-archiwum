import { shoppingList } from "./shoppingList.js";

// 1
const shoppingListWithIndexes = shoppingList.reduce((acc, current) => {
  return [...acc, { [current.produkt]: { ...current } }];
}, []);

// console.log(shoppingListWithIndexes);

// 2
const howMuchOnDairy = shoppingList.reduce((acc, current) => {
  return current.typ === "nabiał" ? acc + current.cena * current.ilosc : acc;
}, 0);

// console.log(howMuchOnDairy);

// 3
const thingsInKg = shoppingList
  .reduce((acc, current) => {
    return current.jednostka === "kg" ? [...acc, current.produkt] : acc;
  }, [])
  .sort();

// console.log(thingsInKg);

// 4
const findProductsByType = (shoppingList, type) => {
  return shoppingList
    .reduce((acc, product) => {
      return product.typ === type && product.cena * product.ilosc < 10
        ? [...acc, product]
        : acc;
    }, [])
    .sort((prev, curr) =>
      prev.cena * prev.ilosc > curr.cena * curr.ilosc ? 1 : -1
    );
};

// console.log(findProductsByType(shoppingList, "nabiał"));

// 5
const thingsInSztuki = shoppingList.reduce((acc, current) => {
  return current.jednostka === "sztuk" ? [...acc, current.produkt] : acc;
}, []);

// console.log(thingsInSztuki);

// 6
const list = shoppingList.reduce((acc, current) => {
  if (acc[current.typ] === undefined) acc[current.typ] = [];

  const { produkt, ilosc, jednostka } = current;
  acc[current.typ].push({ produkt, ilosc, jednostka });

  return acc;
}, {});

const keys = Object.keys(list).sort();

const result = keys.reduce((acc, type) => {
  const temp = `${type.charAt(0).toUpperCase() + type.slice(1)}`;

  const rest = [...list[type]]
    .sort((a, b) => a.produkt.localeCompare(b.produkt))
    .reduce((acc, current, index) => {
      return (
        acc +
        `${index + 1}. ${current.produkt} - ${current.jednostka}: ${
          current.ilosc
        }\n`
      );
    }, "");

  return acc + `${temp}:\n${rest}`;
}, "");

console.log(result);

// 7
const mostExpensivePrice = shoppingList.reduce((acc, product) => {
  const price = product.cena * product.ilosc;
  return acc < price ? price : acc;
}, 0);

const cheapestProducts = shoppingList.reduce((acc, current) => {
  return current.cena * current.ilosc < mostExpensivePrice
    ? [...acc, { [current.produkt]: current.cena * current.ilosc }]
    : acc;
}, []);

// console.log(cheapestProducts);
