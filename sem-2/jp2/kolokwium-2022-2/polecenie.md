# Kolokwium 2 - 2021/2022

## Zanim zaczniesz

Utwórz prosty projekt node'owy, a następnie skonfiguruj go tak, aby:

- komenda `yarn zad1` uruchomiła skrypt zawierający rozwiązanie zadania 1.
- komenda `yarn zad2` uruchomiła skrypt zawierający rozwiązanie zadania 2.
- komenda `yarn zad3` uruchomiła skrypt zawierający rozwiązanie zadania 3.

Do projektu możesz dodać narzędzia poznane podczas zajęć pod warunkiem, że zostaną wykorzystane i ich użycie ma sens.

## UWAGA (!!!)

Zadbaj o to, by oddawany projekt nie zawierał błędów.

Rozwiązania zawierające je lub nieuruchamiające się po wpisaniu odpowiedniej komendy
**NIE BĘDĄ SPRAWDZANE (!!!)**.

To samo tyczy się **zakomentowanych** fragmentów kodu, które będą traktowane jako brudnopis.

Zadbaj o to, aby wysyłane archiwum zawierające rozwiązanie kolokwium **nie zawierało** folderu **node_modules**.

**W swoich rozwiązaniach NIE używaj mechanizmu async/await.**

## Polecenia

**Zadanie 1.**

```js
const process = (wyn1, wyn2) => {
  // Uzupełnij
};

const result = (funTab1, funTab2, func) => {
  // Uzupełnij
};

result(tab1, tab2, process);
```

Napisz funkcje `result` spełniającą poniższe warunki:

- dwoma pierwszymi argumentami funkcji są tablice funkcji asynchronicznych, których rezultatem są wartości liczbowe
- trzecim argumentem jest funkcja `func` przetwarzające wyniki kolejnych funkcji z tablic `funTab1` i `funTab2`
- jeżeli tablice nie są równe, to przyjmujemy, że brakująca wartość wynosi 0
- funkcja `result` powinna zapewnić, że wszystkie funkcje z obu tablic będą wykonywać się "równolegle" i wyświetli je w formacie:

```js
[
  wynik_funkcji_func(wynik_funkcji_1_z_funTab1, wynik_funkcji_1_z_funTab2),
  wynik_funkcji_func(wynik_funkcji_2_z_funTab1, wynik_funkcji_2_z_funTab2),
  wynik_funkcji_func(wynik_funkcji_3_z_funTab1, wynik_funkcji_3_z_funTab2),
  wynik_funkcji_func(wynik_funkcji_4_z_funTab1, wynik_funkcji_4_z_funTab2),
  // ...
];
```

**Zadanie 2.**

Napisz funkcję:

```js
const poKolei = (fun1, fun2, fun3, cb) => {
  // Uzupełnij
};
```

taką, że:

- jej trzema pierwszymi argumentami są funkcje zwracające promise – możesz założyć, że funkcje te muszą być przygotowane na przyjęcie określonej listy argumentów, z których korzystać będzie `poKolei`
- funkcja `poKolei` powinna zapewnić, że `fun3` wykona się po `fun2`, które to wykona się zawsze po `fun1`. Wyniki wygenerowane przez `fun1` zostaną przekazane do `fun2`, a wynik `fun2` zostanie przekazany do `fun3`
- czwartym argumentem jest „callback” `cb`, czyli funkcja, której zadaniem jest przetworzenie wyników zwracanych przez `fun3`
- jeżeli któryś z promise'ów zakończy się porażką, funkcja ma dalej kontynuować swoje zadanie

**Zadanie 3.**

Napisz funkcje

```js
const checkTime = (funTab) => {
  // Uzupełnij
};
```

spełniającą poniższe warunki:

- funkcja przyjmuje tablice funkcji asynchronicznych tj. `funTab` zawierającą stałą liczbę 5-ciu zapytań (w dowolnej kolejności):
  1. GET `https://jsonplaceholder.typicode.com/photos`
  2. POST `https://jsonplaceholder.typicode.com/posts` z obiektem:
     ```
     {
       title: 'Test',
       body: 'Lorem ipsum',
       userId: 2
     }
     ```
  3. GET `https://jsonplaceholder.typicode.com/users/{id}` po dowolnym `id` (zakres 1-10)
  4. GET `https://jsonplaceholder.typicode.com/todos`
  5. PUT `https://jsonplaceholder.typicode.com/posts/{id}` po dowolnym `id` (zakres 1-100) z obiektem:
     ```
     {
       id: id,
       userId: 3,
       title: 'New title',
       body: 'New body'
     }
     ```
- funkcja powinna wykonywać dwa scenariusze (oba powinny wykonywać się jednocześnie, muszą być osobnymi procesami)
  1. (a) funkcje przekazane jako parametr będą wykonywane jedna po drugiej (tzn. w momencie zakończenia wykonywania funkcji pierwszej, rozpoczyna się wykonanie funkcji drugiej)
  2. (b) wszystkie funkcje wykonywane są równocześnie
- co sekundę (lub inną jednostkę czasu) powinna zostać wypisana informacja, ile czasu upłynęło od rozpoczęcia działania programu
- kiedy jeden ze scenariuszy zakończy swoje działanie w konsoli powinien zostać wypisany odpowiedni komunikat z informacją, po ilu np. sekundach scenariusz zakończył swoje działanie
- na koniec funkcja `checkTime` powinna wyświetlić tablice dwóch liczb zawierającą czasy zakończenia działania każdego ze scenariuszy

```js
// Przykładowe działanie programu

checkTime(funTab);
// Start
// 1
// Zakończono działanie: scenariusz b)
// 2
// 3
// 4
// Zakończono działanie: scenariusz a)
// Koniec
// Czas działania: [1, 4]
```
