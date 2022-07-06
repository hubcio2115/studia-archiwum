// ========================================
// ZADANIE 1
// ========================================

//  Zdefiniuj pola 'title' i 'author' i funkcję print(), która wypisze: author - title

const book0 = {
  title: "tytuł",
  author: "autor",
  print() {
    console.log(`${this.author} - ${this.title}`);
  },
};

book0.print();

const book1 = {};

book1.title = "tytuł";
book1.author = "autor";
book1.print = () => {
  console.log(`${book1.author} - ${book1.title}`);
};

book1.print();

const book2 = Object.create({});

book2.title = "tytuł";
book2.author = "autor";
book2.print = () => {
  console.log(`${book2.author} - ${book2.title}`);
};

book2.print();

function BookCreator(title, author) {
  const b = {
    title: "",
    author: "",
    readers: 0,
    print() {
      console.log(`${this.author} - ${this.title}`);
    },
    addReaders() {
      this.readers++;
    },
  };

  return b;
}

const book3 = BookCreator("Cień wiatru", "Carlos Ruiz Zafon");
const book4 = BookCreator("Ojciec Chrzestny", "Mario Puzo");

book3.print();
book4.print();

// ========================================
// ZADANIE 2
// ========================================

// Przetestuj poniższy kod i odpowiedz na pytania

function testThis() {
  console.log(this);
}

testThis();

function testThis2() {
  "use strict";
  console.log(this);
}

testThis2();

// 2.1. Czym jest this?
// To zmienna kontekstowa, przyjmuje wartość obiektu, w którym jest używana.

// 2.2. Do czego odwołuje się this w obu przypadkach.
// undefined

const person = {
  name: "Oscar Wilde",
  print() {
    console.log(`'a: ${this.name}'`);

    function a() {
      console.log(this);
    }

    a();
  },
};
person.print();

// 2.3. Jakie wartości przyjmuje this w powyższych przypadkach i dlaczego?
//  "Oscar Wilde" i undefined

// 2.4. Zmodyfikuj powyższy kod w ten sposób, aby funkcja a wyświetlała w konsoli 'a: Oscar Wilde'. Nie używaj arrow function.

const printName = function () {
  console.log(this.name);
};

const person1 = {
  name: "Aaron Towels",
};

const person2 = {
  name: "Tom Clancy",
};

// 2.5. Za pomocą funkcji printName wypisz 'name' obu autorów. Nie zmieniaj implementacji funkcji printName!

person1.printName = printName;
person2.printName = printName;

person1.printName();
person2.printName();

const person3 = {
  name: "Arthur Conan Doyle",
  print() {
    const a = () => {
      console.log(this);
    };
    a();
  },
};

person3.print();

// 2.6. Co wydrukuje w konsoli powyższy kod? Jaki scope ma arrow function?
// Obiekt. Scope całego obiektu.

// ========================================
// ZADANIE 3
// ========================================

// Powróćmy do zadania 1.
// Dlaczego nasza funkcja BookCreator nie jest najlepszym rozwiązaniem do tworzenia obiektów?
// Ponieważ tworzy pusty obiekt potem go edytuje i zwraca.

// Zmodyfikuj funkcję BookCreator tak, aby inicjalizowała pola author i title.
// Funkcję print zadeklaruj jako wspólną dla wszystkich obiektów tworzonych przez BookCreator.
// Dopisz do tworzonych obiektów pole readers, które będzie zawierało liczbę czytelników.
// Zadeklaruj funkcję addReader, która inkrementuje pole readers. addReader powinna być funkcją wspólną, tak jak print.

// ========================================
// * ZADANIE 4
// ========================================

// Na stworzonym obiekcie wywołaj funkcję hasOwnProperty('isBestseller').
// Napisz dlaczego nasz obiekt ma do niej dostęp. (jeśli wyskakuje błąd - powróć do poprzedniego zadania)

const object = {};
object.hasOwnProperty("isBestseller");

// Ponieważ w Prototypie obiektu jest taka metoda.

// ========================================
// * ZADANIE 5
// ========================================

// Odwołaj się do zmiennej __proto__ w stworzonym obiekcie, co zawiera ta zmienna i do czego służy?
// Zmienna __proto__ zawiera nazwę Prototypu danego obiektu.
const book = BookCreator("Włamać się do mózgu", "Radek Kotarski");
console.log(book.__proto__);
