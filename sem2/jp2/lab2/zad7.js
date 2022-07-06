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

console.log(`Wszyscy mają w sumie ${sumOfAges} lat`);
console.log(`Średnia wieku wynosi ${sumOfAges / persons.length}`);
