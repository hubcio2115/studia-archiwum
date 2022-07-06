"use strict";

// 1.1
// Co wyświetlą na ekranie poniższe wywołania?

const book = {
  title: "Potop",
  author: "Henryk Sienkiewicz",
};

// console.log(book.__proto__ === Object.prototype); // true
// console.log(book.__proto__.__proto__ === null); // true

// 1.2.
// Zastanów się, co należy wpisać w miejsce ..., tak aby każde wywołanie po odkomentowaniu zwróciło true.

const animals = ["dog", "cat", "rabbit", "hamster"];

// console.log(animals.__proto__ === Array.prototype);
// console.log(animals.__proto__.__proto__ === Object.prototype);
// console.log(
//   animals.__proto__.__proto__.__proto__ === Object.prototype.__proto__
// );

// 1.3.
// Co zostanie wyświetlone na ekranie w poniższym przykładzie?

function Animal(animal) {
  this.animal = animal;
}

var dog = new Animal("dog");
var cat = new Animal("cat");
dog.whatIs = function () {
  console.log("It's a " + this.whatIs());
};

// console.log(dog.__proto__ === Animal.prototype); // true
// console.log(dog.__proto__ === cat.__proto__); // true

// 1.4.
// Stwórz obiekt za pomocą funkcji CreateMovie (zawierający klucze bez wartości: director, title, year) wykorzystując słówko `this`.
// Jeśli przy tworzeniu obiektu rok nie zostanie podany powinien przyjmować wartość "unknown".

function CreateMovie(director, title, year) {
  this.director = director;
  this.title = title;
  !year ? this.year : (this.year = "unknown");
}

// Następnie nie zmieniając implementacji funkcji CreateMovie, dodaj do niego metody:
// * isOlder(year) - zwracającą true/false w zależności od tego, czy podany film jest młodszy/starszy nić rok 2000.
// * print - wyświetlającą: "director: title (year)"

CreateMovie.prototype.isOlder = function (year) {
  return this.year > year;
};

CreateMovie.prototype.print = function () {
  console.log(`${this.director}: ${this.title} (${this.year})`);
};

// 1.5.
// Uzupełnij poniższy konstruktor o inicjalizację name, type i funkcję printInstrument. Funkcja printInstrument powinna być współdzielona między wszystkie utworzone obiekty.

function CreateInstrument(name, type) {
  const instrument = Object.create({
    name: name,
    type: type,
    printInstrument() {
      console.log(this.name);
    },
  });

  return instrument;
}

const violin = CreateInstrument("violin", "");
const guitar = CreateInstrument("guitar", "");

// violin.printInstrument();
// guitar.printInstrument();

// 1.6.
// Uzupełnij poniższy konstruktor, który tworzy obiekt dziedziczący po Instrument. Wykorzystaj do jego stworzenia konstruktor z zadania poprzedniego.
// Zdefiniuj funkcję setStrings(number), która ustala liczbę strun w instrumencie (ta funkcja też powinna być współdzielona). NewStringInstrument powinien mieć też dostęp do funkcji, która znajduje się w Instrument.
// Podpowiedź: aby zmienić wartość zmiennej __proto__ należy użyć - Object.setPrototypeOf(object, prototype) - należy użyć tej funkcji dwa razy w tym rozwiązaniu.

function CreateStringedInstrument(name, type, stringsCount) {
  const newStringedInstrument = {
    stringsCount,
    setStrings(stringsCount) {
      this.stringsCount = stringsCount;
    },
  };
  Object.setPrototypeOf(newStringedInstrument, CreateInstrument(name, type));

  return newStringedInstrument;
}

// const stringedInstrument = CreateStringedInstrument("gitara", "strunowy", "3");
// stringedInstrument.printInstrument();
// stringedInstrument.setStrings(3);

// 1.7.
// Przeanalizuj poniższy kod i odpowiedz na umieszczone w nim pytania.

function Instrument(name, type) {
  this.name = name;
  this.type = type;
}

Instrument.prototype.printInstrument = function () {
  console.log("Instrument: " + this.name + ", typ: " + this.type);
};

function StringedInstrument(stringsCount, name, type) {
  Instrument.call(this, name, type);
  this.stringsCount = stringsCount;
}

StringedInstrument.prototype = Object.create(Instrument.prototype);

// a) Stwórz instancję StringedInstrument.

const stringedInstrument = new StringedInstrument("6", "gitara", "elektryczna");

// b) W jaki sposób odwołać się do metody printInstrument?

// stringedInstrument.printInstrument();

// c) Zastąp wywołanie call() funkcją apply()

// 1.8.
// Utwórz obiekt Animal z polem 'name' i funkcją printName, po którym będą dziedziczyły Mammal (z polem age i funkcją getAge) i Fish (z polem weight i funkcją increaseWeight()) .
// Następnie stwórz kolejne obiekty - Dog (z polem breed i nadpisaniem funkcji getAge(), która tutaj będzie najpierw wywoływała funkcję getAge() z klasy dziedziczonej, a następnie mnożyła wynik razy 4 i wyświetlała go) i Salmon (z funkcją catch()), które będą dziedziczyły odpowiednio po Mammal i Fish.
// W razie problemów wzoruj się na rozwiązaniu z poprzedniego zadania.

class MyAnimal {
  constructor(name) {
    this.name = name;
  }
  printName() {
    console.log(this.name);
  }
}

const zwierze = new MyAnimal("zwierze");
zwierze.printName();

class Mammal extends MyAnimal {
  constructor(name, age) {
    super(name);
    this.age = age;
  }
  getAge() {
    return this.age;
  }
}

const ssak = new Mammal("kangur", 10);
ssak.printName();
console.log(ssak.getAge());

class Fish extends MyAnimal {
  constructor(name, weight) {
    super(name);
    this.weight = weight;
  }
  increaseWeight(weight) {
    this.weight += weight;
  }
}

const ryba = new Fish("szczupak", 11);
console.log(ryba.weight);
ryba.increaseWeight(1);
console.log(ryba.weight);

class Dog extends Mammal {
  constructor(name, age, breed) {
    super(name, age);
    this.breed = breed;
  }
  getAge() {
    return Mammal.prototype.getAge() * 4;
  }
}

const pies = new Dog("Gucci", 3, "mastiff włoski");
