### Kolokwium nr 2

### UWAGA: Proszę nie korzystać z gotowych funkcji.

### Zadanie 1.
Napisz skrypt zawierający jednoargumentową funkcję rekurencyjną, która obliczy ile liter 'a' jest w danym napisie, np. dla "Alamakota" zwróci liczbę 3. 
#### Wejście: 
Zmienna napis przechowująca łańcuch znaków, która została podana jako argument funkcji.
#### Wyjście: 
Na ekranie pojawia się liczba równa ilości znaków 'a' w napisie.
#### Warunki poprawności zadania: 
Na ekranie powinien pojawić się odpowiedni wynik. Należy zdefiniować i wywołać funkcję rekurencyjną. Upewnij się, czy program działa dla różnych napisów.

### Zadanie 2. 
Napisz skrypt sortujący listę liczb całkowitych zmieniając poniższy algorytm bąbelkowy, tak aby sortował liczby nierosnąco oraz zewnętrzna pętla przechodziła
od pierwszego elementu do ostatniego (czyli w odwrotnej kolejności do alg. poniżej): 

```
Sortowanie bąbelkowe O(n2)
Wejście: lista t, która zawiera n elementów
Wyjście: posortowana lista t
1. j ← n - 1
2. Dopóki j ≥ 1
 2.1. i ← 1
 2.2. Dopóki i ≤ j
  2.2.1. Jeżeli t[i] > t[i + 1]
   2.2.1.1. zamień(t[i], t[i + 1])
  2.2.2. i ← i + 1
 2.3. j ← j - 1
```
#### Wejście: 
Zmienna lista zawierająca liczby całkowite, która zostaje podana jako argument funkcji sortującej.
#### Wyjście: 
Na ekranie pojawia się posortowana nierosnąco lista.
#### Warunki poprawności zadania: 
Na ekranie powinna pojawić się odpowiednia lista. Należy zdefiniować i wywołać funkcję sortującą zmienionym algorytmem bąbelkowym. Upewnij się, czy program działa dla różnych list.

### Zadanie 3. 
Napisz skrypt, który będzie pobierał z pliku szesnastkowo.txt kolejne liczby zapisane w systemie szesnastkowym ( każda w innej linii ), zamieni każdą na system dziesiętny oraz ósemkowy,
a następnie wpisze do odpowiedniego pliku dziesietnie.txt lub osemkowo.txt.

#### Wejście:
Plik szesnastkowo.txt z liczbami w systemie szesnastkowym.
#### Wyjście:
Pliki dziesietnie.txt i osemkowo.txt zawierające odpowiednie wartości.
#### Warunki poprawności zadania:
Upewnij się, że program wpisuje odpowiednie wartości do odpowiednich plików. Upewnij się, że program działa prawidłowo dla różnych danych.


### Zadanie 4.
Napisz skrypt, który będzie zawierał małą bazę danych przechowującą dane osób wraz z wykazem kont bankowych: (id, imię, nazwisko, konto1 (id, nazwa banku, suma środków), konto2...)
np. dane ososby z 3 kontami mogą wyglądać następująco: ( 2, Jan, Kowaski, (1, PKO, 2200), (2, NBP, 21000), (3, NBP, 210) ). Następnie skrypt wypisze ile środków zgromadziły wszystkie
osoby z bazy w konkretnym banku podanym przez użytkownika, czyli dla powyższego przykładu dla banku NBP suma wyniesie 21210. 

#### Wejście:
 Zmienna lista przechowująca dane słownikowe (baza danych), które będą przechowywać informacje o osobach i kontach oraz nazwa banku pobrana od użytkownika.
#### Wyjście:
 Na ekranie pojawia się odpowiednia informacja odnośnie ilości pieniędzy zgroamdzonych na kontach danego banku.
#### Warunki poprawności zadania:
Upewnij się, że skrypt działa prawidłowo, w szczególności czy przechowuje odpowiednie dane i czy liczy pieniądze ze wszystkich kont danego banku.
