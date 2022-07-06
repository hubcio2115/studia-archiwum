## Zanim zaczniesz

Utwórz prosty projekt node'owy, a następnie skonfiguruj go tak, aby:

- komenda `yarn script1` uruchomiła kod zawierający rozwiązanie zadania 1.
- komenda `yarn script2` uruchomiła kod zawierający rozwiązanie zadania 2.
- komenda `yarn script3` uruchomiła kod zawierający rozwiązanie zadania 3.

Wszystkie pliki zawierające rozwiązania powinny znaleźć się w folderze `src`.

Do projektu możesz dodać narzędzia poznane podczas zajęć pod warunkiem, że zostaną wykorzystane i ich użycie ma sens.

## UWAGA (!)

Zadbaj o to, by oddawany projekt nie zawierał błędów. Rozwiązania, których nie da się uruchomić po wpisaniu odpowiedniej komendy **NIE BĘDĄ SPRAWDZANE (!!!)**. To samo tyczy się zakomentowanych fragmentów kodu, które będą traktowane jako brudnopis.

Rozwiązane zadania należy wysyłać w formacie Grupa*[numer_grupy]*[pierwsza_litera_imienia][nazwisko] na adres e-mail prowadzącego laboratoria ([imie].[nazwisko]@ug.edu.pl).

## Polecenia

**Zadanie 1**

W pliku [books.js](/books.js) znajduje się tablica książek. Posegreguj podane książki względem gatunku. Jeśli książka posiada więcej gatunków niż jeden, powinna znaleźć się pod każdym z tych gatunków. Dodatkowo usuń wszystkie pola oprócz tytułu i autora. Zadanie rozwiąż uzupełniając poniższy kod, tak aby otrzymać poniżej zaprezentowany wynik.
Pamiętaj, aby używać _wyłącznie_ funkcji wbudowanych klasy Array (oprócz funkcji `.forEach()`), `for` i `foreach` zdecydowanie odpada ;)

```
const books = require('./books.js');

const result = books.booksArray.reduce(
    // Uzupełnij
)

console.log (result);
```

```
// Postać oczekiwanego wyniku
{
    'fantasy': [
        { title: 'Lord of the Rings', author: 'J.R.R. Tolkien' },
        { title: 'Harry Potter', author: 'J.K. Rowling' },
        ...
    ],
    'fiction': [
        { title: 'The Borthers Karamazov', author: 'Fyodor Dostoyevsky' },
        ...
    ],
    ...
}
```

**Zadanie 2.**

Napisz funkcję:

`const poKolei = (funTab, cb) => (n) => { ... };`

taką, że:

1. pierwszym argumentem jest tablica funkcji asynchronicznych – załóż, że funkcje te muszą być przygotowane na przyjęcie argumentu `n`, z którego korzysta funkcja poKolei
2. funkcja poKolei powinna zapewnić, że następna funkcja np. `fun2` wykona się zawsze po poprzedniej np. `fun1`, a wyniki wygenerowane przez `fun1` zostaną przekazane do `fun2`.
3. trzecim argumentem jest „callback” `cb`, czyli funkcja, której zadaniem jest przetworzenie wyników zwracanych przez ostatnią funkcję w tablicy

**Zadanie 3.**

Wyobraź sobie, że piszesz program do sprzedaży ciastek w swojej cukierni. Każde ciastko kosztuje 5 zł i każdy klient może kupić tylko jedno ciastko.  
Klienci mogą zapłacić za ciastko monetą lub banknotem o nominale 5, 10 lub 20 zł. Zawsze musisz wydać prawidłową resztę.

**Uwaga!** Jako nowa cukiernia nie masz wkładu własnego oprócz ciastek. Twój początkowy budżet wynosi 0 zł.

Napisz program, który sprawdzi, czy będziesz w stanie wypłacić każdemu klientowi resztę.

```
// Przykład działania:

checkExchange([5, 5, 5, 10, 20]) // true

checkExchange([5, 5, 10, 10, 20]) // false

checkExchange([10, 10]) // false

checkExchange([5, 5, 10]) // true

```
