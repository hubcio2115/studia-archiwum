"use strict";

const person1 = {
  name: "Agata",
  age: 21,
};

const person2 = {
  name: "Tomasz",
  age: 25,
};

const person3 = {
  name: "Alicja",
  age: 31,
};

const person4 = {
  name: "Jan",
  age: 20,
};

const persons = [person1, person2, person3, person4];

let sumOfAges = 0;
for (const person of persons) {
  sumOfAges += person.age;
}

const averageAge = sumOfAges / persons.length;

const belowAverage = [];
const aboveAverage = [];

for (const person of persons) {
  person.age > averageAge
    ? aboveAverage.push(person.name)
    : belowAverage.push(person.name);
}

console.log(aboveAverage);
console.log(belowAverage);
