"use strict";

// Zadanie 2.1.
// Stwórz obiekt klasy Promise -> niech zakończy się powodzeniem (resolve) po 5 sekundach i zwróci string 'Udało się!'.
// Jako callback niech wypisze zwrócony string w konsoli.

// Zadanie 2.2.
// Zmodyfikuj powyższy kod tak, aby zamiast z sukcesem - promise zakończył się porażką i zwracał string 'Porażka'.
// Skorzystaj z then() aby obsłużyć błąd.

// Zadanie 2.3.
// Zamiast then(), zmodyfikuj powyższy kod używając catch()

// Zadanie 2.4.
// Napisz funkcję multiplyAsync(x,y), która zwraca obiekt klasy Promise, kończący się porażką, gdy któryś za argumentów jest niepoprawny (nie jest liczbą).
// W przeciwnym przypadku zwraca iloczyn dwóch liczb. Napisz callback, który wypisuje wynik w konsoli.

// 2.1
const promise1 = new Promise((resolve, reject) => {
  resolve("Udało się!");
}).then((string) => {
  console.log(string);
});

// 2.2
const promise2 = new Promise((resolve, reject) => {
  resolve("Porażka");
}).then((string) => {
  console.log(string);
});

// 2.3
const promise3 = new Promise((resolve, reject) => {
  reject("Porażka");
}).catch((string) => {
  console.log(string);
});

// 2.4
const multiplyAsync = (x, y) => {
  return new Promise((response, reject) => {
    if (typeof x !== "number" || typeof y !== "number")
      reject("Podano nie poprawne dane");

    response(x * y);
  });
};

multiplyAsync(5, 5)
  .then((res) => {
    console.log(res);
  })
  .catch((rej) => {
    console.log(rej);
  });

multiplyAsync("5", 5)
  .then((res) => {
    console.log(res);
  })
  .catch((rej) => {
    console.log(rej);
  });
