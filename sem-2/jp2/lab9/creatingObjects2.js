"use strict";

// 1. Uprość funkcję BookCreator z poprzednich zajęć tak, aby zawierała tylko nadawanie wartości polom. (użyj operatora this)
// Dodaj wywołanie słowa kluczowego new, przy wywołaniu BookCreator().

function BookCreator(title, author) {
  this.title = title;
  this.author = author;
  this.readers = 0;
}

const book = new BookCreator("How to Not Die Alon", "Logan Ury");

// BookCreator jest konstruktorem, a je zawsze (ZAWSZE) deklarujemy zaczynając nazwę od wielkiej litery

// 1.1. Użyj zmiennej prototype, aby dodać funkcje print() i addReader() do tworzonych obiektów.

BookCreator.prototype.print = function () {
  console.log(`${this.author} - ${this.title}`);
};

BookCreator.prototype.addReader = function () {
  this.readers++;
};

const newBook = new BookCreator("Getting Thing Done", "David Allen");

newBook.print();
newBook.addReader();

// 2. Tworzymy alternatywną wersję powyższego kodu. Użyj słów kluczowych class i constructor, aby osiągnąć powyższy efekt.

class BookCreatorClass {
  constructor(title, author) {
    this.title = title;
    this.author = author;
    this.readers = 0;
  }
  print() {
    console.log(`${this.author} - ${this.title}`);
  }
  addReader() {
    this.readers++;
  }
}

// 3. Znasz już wiele sposób na stworzenie obiektu. Dlaczego więc nie użyć arrow function?
// Uzupełnij poniższy kod o inicjalizację pola name i age. Dodaj wewnątrz funkcję addAge, która inkrementuje wiek.

const Person = (name) => ({
  name: name,
  age: 0,
  addAge() {
    this.age++;
  },
});

// Przetestuj działanie tak stworzonego obiektu, korzystając z wiedzy, którą już masz. Jakie są różnice pomiędzy stworzeniem obiektu za pomocą poprzednich metod?
// (przetestuj prototype, new itd.)

const person = Person("Paweł");

console.log(person.age);

person.addAge();

console.log(person.age);

Person.prototype.changeName = function (newName) {
  this.name = newName;
};

person.changeName("Hubert");
console.log(person.name);
