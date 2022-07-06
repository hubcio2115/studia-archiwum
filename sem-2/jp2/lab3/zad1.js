"use strict";

// Poniższe fragmenty kodu zostały skomentowane w celu utrzymania porządku.
// Odkomentowuj je na bieżąco i zapisuj odpowiedzi w komentarzu.
// Ostatecznie przed wrzuceniem pliku na repozytorium skomentowane powinny być tylko dodane odpowiedzi i fragmenty kodu powodujące ewentualne błędy.

// ========================= Zadanie 1 =========================
// Co zwróci funkcja poniższa funkcja w każdym z poniższych przypadków?
// Wyjaśnij, dlaczego w niektórych przypadkach wyniki różnią się.

// ========================== UWAGA =============================
// Zapis
// (impression) ? console.log('A') : console.log('B');
// Jest skróconą wersją:
// if (impression) {
//     console.log('A');
// } else {
//     console.log('B');
// }
// ==============================================================

function isEquals(val_1, val_2) {
  val_1 == val_2 ? console.log("A") : console.log("B");
  val_1 === val_2 ? console.log("C") : console.log("D");
}

// Wyniki różnią się ponieważ w pierwszym przypadku porównywane są same wartości, a w drugim wartości wraz z typem.
// Jeżeli wartości mogą się pokrywać wtedy w pierwszym przypadku są zamieniane.
// isEquals(2, '2'); A, D
// isEquals(null, undefined); A, D
// isEquals(undefined, NaN); B, D
// isEquals(["a", "b", "c"], ["b", "c", "d"]); B, D
// isEquals(0, ''); A, D
// isEquals('0', ''); B, D
// isEquals(+0, -0); A, C
// isEquals(0, false); A, D
// isEquals(0, 'false'); B, D
// isEquals([1, 2], '1,2'); A, D

!!false;
!!true;
!!undefined;
!!null;

// ========================= Zadanie 2 =========================
// Jaki będzie efekt działania poniższego fragmentu kodu?
// Wyjaśnij wynik

const person = {
  firstName: "Jan",
  lastName: "Kowalski",
};

// console.log(person);
// person = {};
// console.log(person);

// Kod się wykrzaczy, ponieważ nadpisujemy stały obiekt nowym obiektem.

// ========================= Zadanie 3 =========================
// Co zostanie wyświetlone na ekranie?
// Wyjaśnij wynik

// let number = 3;
// console.log(number);
// {
//   let number = 4;
//   console.log(number);
// }
// console.log(number);

// 3, 4, 3
// Wynika to z tego, że na początku liczba jest deklarowana globalnie i jest wyświetlana.
// Czwórka wynika z tego, że zmienna została zadeklarowana lokalnie w klamerkach pod tą samą nazwą i przykryła zmienną globalną.
// Druga trójka to ponowne wyświetlenie zmiennej globalnej. Zmienna lokalna już nie istnieje.

// ========================= Zadanie 4 =========================
// Czym się różnią poniższe dwa fragmenty kodu?
// Jak działa operator '...'?
// Operator ... to tak zwany *spread*. Możemy go użyć na tablicach po to, żeby stworzyć nową tablicę z wartości innej.

// Zadeklarowanie arr
// const arr = [1, 2];
// Wpisanie arr do innej tablicy
// const newArr1 = [arr, 3, 4];
// console.log(newArr1);
// *Spread* wartości z tablicy i zapisanie jej do innej
// const newArr2 = [...arr, 3, 4];
// console.log(newArr2);

// Co zostanie wyświetlone na ekranie?
// Wyjaśnij wynik
// [[1, 2], 3, 4], [1, 2, 3, 4]

// const word = "javascript";
// const arrWord = [...word];
// console.log(arrWord);
// ['j', 'a', 'v', 'a', 's', 'c', 'r', 'i', 'p', 't']

// ========================= Zadanie 5 =========================
// Zapoznaj się z kodem poniżej. Jaki będzie jego wynik i dlaczego?

// var hello = "Hello world!";
// var result = hello / 2;

// result;

// console.log(Number.isNaN(hello)); false, ponieważ NaN jest typu number
// console.log(Number.isNaN(result)); true, ponieważ Nan jest typu number

// ========================= Zadanie 6 =========================
// Zapoznaj się z przykładami poniżej. Jaka jest różnica między var a let/const?

// var car = "BMW";

// function showCar() {
//   car = "Audi";
//   model = "A5";
//   console.log("Great car!");
// }

// showCar();

// console.log(car);
// console.log(model);

// -------

// var name = "Bryan";

// (function differentName() {
//   var name = "Adam";
//   console.log(name);
// })();

// console.log(name);

// -------

// if (true) {
//   var a = 2;
// }
// console.log(a);

// if (true) {
//   const b = 2;
// }
// console.log(b);

// -------

// for (var i = 0; i < 10; i++) {
//   console.log(i);
// }
// console.log(i);

// for (let i = 0; i < 10; i++) {
//   console.log(i);
// }
// console.log(i);

// -------

// var test = "var1";
// var test = "var2";

// let test2 = "let1";
// let test2 = "let2";

// const - tworzy lokalnie stałą
// let - tworzy lokalnie zmienną
// var - tworzy zmienne które dostępne są dla każdego dziecka

// ========================= Zadanie 7 =========================
// Do czego używany jest 'use strict' w pierwszej linijce skryptu?

// Włącza strict mode w pliku. https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode
