"use strict";
// Zadanie 1.1.
// Dopisz do pomiędzy deklaracją funkcji helloWorld a poleceniem console.log instrukcję wywołania helloWorld() tak, aby na ekranie pojawiło się jako pierwsze 'No, hello universe!'.
// Nie możesz dopisać nic za console.log()

function helloWorld() {
  console.log("Hello world!");
}

// Uzupełnij

// setTimeout(helloWorld, 0);

// console.log("No, hello universe!");

// Zadanie 1.2.
// Napisz funkcję, która wypisuje w konsoli 'Start!' i po dwóch sekundach wypisuje 'Koniec'.

const zad12 = () => {
  console.log("Start");

  setTimeout(() => {
    console.log("Koniec");
  }, 2000);
};

// zad12();

// Zadanie 1.3.
// Napisz funkcję, która wypisuje 'Welcome' co sekundę w nieskończoność.

const infinityWelcome = () => {
  setInterval(() => {
    console.log("Welcome");
  }, 1000);
};

// infinityWelcome();

// Zadanie 1.4.
// Napisz funkcję, która wypisuje 'Welcome' co sekundę, ale tylko przez 5 sekund.
// Podpowiedź: użyj clearInterval

const welcomeFor5Seconds = () => {
  const interval = setInterval(() => {
    console.log("Welcome");
  }, 1000);

  setTimeout(() => {
    clearInterval(interval);
  }, 5000);
};

// welcomeFor5Seconds();

// Zadanie 1.5.
// Napisz funkcję, która przyjmuje trzy argumenty: funkcję i dwie liczby. Funkcja będzie wywołała podaną w argumencie funkcję co x sekund i automatycznie zatrzyma się po upływie y sekund.

const customInterval = (callback, interval, stop) => {
  const temp = setInterval(callback, interval);

  setTimeout(() => {
    clearInterval(temp);
  }, stop);
};

customInterval(
  () => {
    console.log("Halo");
  },
  1000,
  3000
);
