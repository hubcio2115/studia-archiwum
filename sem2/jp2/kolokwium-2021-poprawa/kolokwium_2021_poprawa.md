## Zanim zaczniesz

Utwórz prosty projekt node'owy, a następnie skonfiguruj go tak, aby:
* komenda `yarn zad1` uruchomiła kod zawierający rozwiązanie zadania 1.
* komenda `yarn zad2` uruchomiła kod zawierający rozwiązanie zadania 2.
* komenda `yarn zad3` uruchomiła kod zawierający rozwiązanie zadania 3. 

Do projektu możesz dodać narzędzia poznane podczas zajęć pod warunkiem, że zostaną wykorzystane i ich użycie ma sens.


## UWAGA (!)

Zadbaj o to, by oddawany projekt nie zawierał błędów. Rozwiązania zawierające je lub nieuruchamiające się po wpisaniu odpowiedniej komendy **NIE BĘDĄ SPRAWDZANE (!!!)**. To samo tyczy się **zakomentowanych** fragmentów kodu, które będą traktowane jako brudnopis. 

Zadbaj o to, aby wysyłane archiwum zawierające rozwiązanie kolokwium **nie zawierało** folderu **node_modules**.

Rozwiązane zadania należy wysyłać w formacie Grupa_[numer_grupy]_[pierwsza_litera_imienia][nazwisko] (np. `Grupa_1_JKowalski` dla Jana Kowalskiego) na adres e-mail prowadzącego laboratoria ([imie].[nazwisko]@ug.edu.pl).


## Polecenia 

**Zadanie 1** 

W pliku [potter.js](/potter.js) znajduje się tablica postaci z Harry'ego Pottera. Pogrupuj je według domu do jakiego przynależą (weź pod uwagę tylko te oznaczone jako żyjące). Jeśli postać nie ma podanego domu powinna znajdować się pod kluczem "noHouse". Dodatkowo usuń wszystkie pola oprócz imienia i typu. Typ powinien być jedną z wartości: `student`, `staff` lub `none` (jeśli postać nie jest ani nauczycielem ani studentem). Zadanie rozwiąż uzupełniając poniższy kod, tak aby otrzymać poniżej zaprezentowany wynik.

**UWAGA (!)** Pamiętaj, aby używać *wyłącznie* funkcji wbudowanych klasy Array (oprócz funkcji `.forEach()`). Nie można również korzystać z pętli: `for`, `foreach` i `while`. 

```js
const resultArray = hogwardArray.reduce((prev, curr) => {
    // Uzupełnij tutaj

}, []);
```

```js
// Oczekiwany output

[
  Gryffindor: [
    { name: 'Harry Potter', type: 'student' },      
    // ...
  ],
  Slytherin: [
    { name: 'Draco Malfoy', type: 'student' },
    { name: 'Horace Slughorn', type: 'staff' },
    { name: 'Dolores Umbridge', type: 'staff' },
    { name: 'Lucius Malfoy', type: 'none' },
    { name: 'Gregory Goyle', type: 'student' }
  ],
  // ...
  noHouse: [
    { name: 'Kingsley Shacklebolt', type: 'none' },
    // ...
  ]
]

```

**Zadanie 2** 

Napisz funkcję:

```js
const razem = (fun1, fun2, fun3, cb) => n => { 
  // Uzupełnij tutaj
};
```                
                        
taką, że:
1. pierwszymi trzema parametrami są funkcje asynchroniczne, gdzie jednym z parametrów jest n, będące liczbą. 
2. funkcja `razem` powinna zapewnić, że wszystkie funkcje będą wykonywać się „równolegle”, a wyniki przez nie wygenerowane zostaną przekazane – jako tablica `[wynik1, wynik2, wynik3]` do funkcji `cb`. 
3. czwartym argumentem jest „callback” `cb`, czyli funkcja, której zadaniem jest przetworzenie wyników zwróconych przez funkcje.
4. Deklaracja funkcji razem ma pozostać w podanym kształcie

**UWAGA (!)** Aby końcowe rozwiązanie było kompletne, powinno zawierać wszystkie parametry potrzebne do wywołania funkcji (deklaracje funkcji asynchrocznych i callback'u) oraz jej przykładowe wywołanie. 

**Zadanie 3**

Stwórz klasę o nazwie `CoffeeShop` zawierający następujące zmienne: 
1. `name` - string (nazwa sklepu)
2. `menu` - tablica obiektów, każdy z elementów zawiera: 
    1. `item` (nazwa elementu), 
    2. `type` (`food` lub `drink`), 
    3. `price`
3. `orders` - na początku pusta tablica

i siedem metod: 
1. `addOrder` - dodaje `name` elementu na koniec tablicy `orders`, jeśli nie istnieje w menu i zwraca komunikat `"Order added!"`. W przeciwnym razie zwróć `"This item is currently unavailable!"`
2. `fulfillOrder` - jeśli `orders` nie jest pustą tablicą zwróć `"The {item} is ready!"`. Jeśli tablica jest pusta zwróć `"All orders have been fulfilled!"`.
3. `listOrders` - zwraca listę przyjetych zamówień, w przeciwnym wypadku - pustą tablicę
4. `dueAmount`- zwraca całkowitą należność za realizowane zamówienia.
5. `cheapestItem` - zwraca nazwę najtańszej pozycji w menu.
6. `drinksOnly`: zwraca tylko nazwy pozycji typu `drink` z menu.
7. `foodOnly`: zwraca tylko nazwy pozycji typu `food` z menu.

**UWAGA 1 (!)** Zamówienia realizowane są w kolejności FIFO (first-in, first-out)

**UWAGA (!)** Pamiętaj, aby używać *wyłącznie* funkcji wbudowanych klasy Array (oprócz funkcji `.forEach()`). Nie można również korzystać z pętli: `for`, `foreach` i `while`. 


```js
// Przykład działania:

// Tworzymy sklep o nazwie "Shop1", który zawiera w menu 3 pozycje: 
// [
//   { item: "cinnamon roll", type: "food", price: 4.99},
//   { item: "hot chocolate", type: "drink", price: 2.99}
//   { item: "lemon tea", type: "drink", price: 2.50}
// ]
// tablica zamówień jest pusta

obj.addOrder("espresso"); // "This item is currently unavailable!" (Sklep nie sprzedaje espresso)

obj.addOrder("hot chocolate"); // "Order added!"
obj.addOrder("cinnamon roll"); // "Order added!"

obj.listOrder(); // ["hot chocolate", "cinnamon roll"]

obj.dueAmount(); // 5.49 (suma cen za hot chocolate i cinnamon roll)

obj.fulfillOrder(); // "The hot chocolate is ready!"
obj.fulfillOrder(); // "The cinnamon roll is ready!"
obj.fulfillOrder(); // "All orders have been fulfilled!" (Wszystkie zamówienia zostały zrealizowane)

obj.listOrder(); // []

obj.dueAmount(); // 0.0

obj.cheapestItem(); // "lemon tea"
obj.drinksOnly(); // ["hot chocolate", "lemon tea"]
obj.foodOnly(); // ["cinnamon roll"]
```