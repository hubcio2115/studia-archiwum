# Kolokwium 2021/2022

## Zanim zaczniesz

Utwórz prosty projekt node'owy, a następnie skonfiguruj go tak, aby:

- komenda `yarn zad1` uruchomiła skrypt zawierający rozwiązanie zadania 1.
- komenda `yarn zad2` uruchomiła skrypt zawierający rozwiązanie zadania 2.
- komenda `yarn zad3` uruchomiła skrypt zawierający rozwiązanie zadania 3.
- komenda `yarn zad4` uruchomiła skrypt zawierający rozwiązanie zadania 4.

Do projektu możesz dodać narzędzia poznane podczas zajęć pod warunkiem, że zostaną wykorzystane i ich użycie ma sens.

## UWAGA (!!!)

Zadbaj o to, by oddawany projekt nie zawierał błędów.

Rozwiązania zawierające je lub nieuruchamiające się po wpisaniu odpowiedniej komendy **NIE BĘDĄ SPRAWDZANE (!!!)**. To samo tyczy się **zakomentowanych** fragmentów kodu, które będą traktowane jako brudnopis.

Zadbaj o to, aby wysyłane archiwum zawierające rozwiązanie kolokwium **nie zawierało** folderu **node_modules**.

## Rozwiązanie

Rozwiązane zadania o nazwie:

`[numer_grupy]\_[pierwsza_litera_imienia][nazwisko]`

np. `1_JKowalski` dla Jana Kowalskiego (oczywiście bez znaku "`")

należy wysłać na odpowiedni adres e-mail prowadzącego laboratoria.

## Polecenia

**Zadanie 1.**

w pliku [series.js](/series.js) znajduje się lista seriali. Wykorzystując jedynie programowanie funkcyjne i jedynie funkcje wbudowane takie jak: `reduce`, `sort`, `filter` i `push` stwórz dwa obiekty `miniseries` i `series`, gdzie:

1. `miniseries` będzie tablicą zawierającą tylko miniseriale (jednosezonowe), posortowane alfabetycznie. Każdy z miniseriali powinien zawierać wyłącznie `name`, `year` i `type`. (Miniseriale rok rozpoczęcia i zakończenia mają taki sam)

2. `series` będzie trzyelementową tablicą tablic zawierającą seriale (bez miniseriali), gdzie:

   - pierwsza tablica będzie zawierała seriale rozpoczęte przed rokiem 2010
   - druga tablica będzie zawierała seriale rozpocząte między 2010 (włącznie) a 2020 rokiem
   - trzecia tablica będzie zawierała tablice rozpoczęte po 2020 (włącznie)

   Dodatkowo:

   - Seriale powinny być posortowane latami, od najstarszego tzn. wg roku rozpoczęcia, a następnie wg. roku zakończenia (jeśli serial nie ma roku zakończenia, to powinien wyświetlić się przed serialami, które rok zakończenia mają).
   - Gatunek powinien być zapisany jako string, nie jako tablica stringów:
     `["Dramat", "Wojenny"]` -> `"Dramat, Wojenny",`
     Między kolejnymi gatunkami, po przecinku znajduje się spacja!
   - Jeżeli serial nie ma roku zakończenia, to nie wyświetlamy go (tj. roku zakończenia) w obiekcie.

```js
// Output miniseries
[
  { name: "Czarnobyl", type: ["Dramat"], year: 2019 },
  { name: "Gambit królowej", type: ["Dramat"], year: 2020 },
  { name: "Kompania braci", type: ["Dramat", "Wojenny"], year: 2001 },
  { name: "Pacyfik", type: ["Dramat", "Wojenny"], year: 2010 },
];

// Output series
[
  [
    // ...
  ],
  [
    // ...
    {
      id: 14,
      name: "Rick i Morty",
      startYear: 2013,
      type: "Komedia, Przygodowy, Sci-Fi, Animacja dla dorosłych",
      seasons: 9,
    },
    {
      id: 11,
      name: "House of Cards",
      startYear: 2013,
      endYear: 2018,
      type: "Dramat, Polityczny",
      seasons: 6,
    },
    // ...
  ],
  [
    // ...
  ],
];
```

**Zadanie 2.**

Stwórz funkcje `detectChanges`, która przyjmuje dwa parametry:

- `original` - obiekt
- `modified` - obiekt o takiej samej strukturze, jak `original`, ze zmienionymi niektórymi wartościami

Uzupełnij funkcję tak, aby zwracała tablicę, zawierającą parę klucz-wartość, gdzie wartość uległa zmianie. Funkcja powinna działać dla różnych obiektów, z różnymi parami klucz-wartość.

```js
function detectChanges(original, modified) {}

// Przykład 1

// Input
const object1 = {
  id: 2,
  name: 'Przyjaciele',
  startYear: 1994,
  endYear: 2004,
  type: ["Komedia"],
  seasons: 10
};

const object2 = {
  id: 2,
  name: 'Przyjaciele edytowany',
  startYear: 1994,
  endYear: 2010,
  type: ["Komedia"],
  seasons: 10
};

// Output
detectChanges(object1, object2);
// -> [ [ 'name', 'Przyjaciele edytowany' ], [ 'endYear', 2010 ] ]

// Przykład 2

// Input
const object1 = {
  value: {
    field: "old value"
  },
  name: 'test'
}
const object2 = {
  value: {
    field: "new value"
  },
  name: 'test'
  }
};

// Output
detectChanges(object1, object2);
// -> [ [ 'value', { field: 'new value' } ] ]
```

**Zadanie 3.**

Stwórz funkcję `getCounter`, która jako parametr przyjmuje dwie wartości - `min` i `max`. Funkcja powinna zwrócić funkcję, która przy każdym wywołaniu zwraca liczbę o 1 większą niż poprzednio zwrócona począwszy od podanej wartości minimalnej, a kończąc na maksymalnej.

Uwaga! Rozwiązanie tego zadania nie może używać zmiennych globalnych!

Przykład działania:

Wywołujemy funkcje `getCounter` z wartościami `(5, 7)`.

Wywołujemy zwracaną przez `getCounter` funkcje, która daje output kolejno:
Pierwsze wywołanie -> output: 5
Drugie wywołanie -> output: 6
Trzecie wywołanie -> output: 7
Czwarte wywołanie -> output: undefined

**Zadanie 4.**

Stwórz klasę `Log`, która będzie przechowywać historię komunikatów w aplikacji. Klasa ta powinna zawierać:

1. Funkcję `write`, która przyjmuje dowolną liczbę argumentów i zwraca je jako string np.:

```js
// Input:
instancjaLog.write("test: ", () => {
  return "komunikat";
});

// Output:
// "test: () => { return 'komunikat' }"
```

2. Funkcję `printHistory`, która przyjmuje opcjonalny parametr `range`. Funkcja zwraca wszystkie komunikaty wypisane z pomocą funkcji `write`. Powinny być one zwrócone jako jeden string, gdzie poszczególne komunikaty są rozdzielone znakiem nowej linii (\n). Parametr `range` powinien być dwuelementową tablicą, gdzie:

- nie może być ujemnych liczb
- pierwszy element powinien być mniejszy od drugiego elementu
- drugi element nie powinien być większy od ilości komunikatów w historii.

Jeśli nie został przekazany do funkcji parametr range, to zwracane są wszystkie komunikaty w historii.

```js
// Input:
instancjaLog.printHistory();
instancjaLog.printHistory([1, 5]);
instancjaLog.printHistory([5, 1]);
instancjaLog.printHistory([2]);

// Output:
// cała historia
// tylko komunikaty od 1 do 5 włącznie
// błąd
// błąd
```

3. Funkcję `clearHistory`, która usuwa wszystkie wydrukowane komunikaty (sprawia, że printHistory zwraca pusty string).

```js
// Input:
instancjaLog.clearHistory();
instancjaLog.printHistory();

// Output:
// pusty string
```
