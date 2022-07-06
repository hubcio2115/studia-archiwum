"use strict";

const cat = {
  name: "Filemon",
  age: 6,
};

cat.description = `Kot ma na imię ${cat.name} i ma ${cat.age} lat.`;
cat.breed = "kot";
cat.colour = "czarny";

cat.description += ` Ma ${cat.colour} kolor i jest rasy ${cat.breed}.`;

console.log(cat.description);
