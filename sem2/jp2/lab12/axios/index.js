"use strict";

import axios from "axios";

/* 
Zadanie 1.1

Stwórz projekt i dołącz do niego bibliotekę axios.

Następnie wykonaj zapytanie metodą GET za pomocą dodanej biblioteki pod następujący url: https://jsonplaceholder.typicode.com/posts
Jako pierwszy callback - sprawdź, czy response jest poprawny (status równy 200). Jeśli tak, to zwróć response, w przeciwnym wypadku wypisz błąd w konsoli.
Jako następny callback - użyj destrukcji obiektów, aby wypisać w konsoli zmienną 'data' i 'headers'.
*/

/* 
Zadanie 1.2 
Stwórz funkcję, która przyjmuje jako parametr obiekt takiej postaci:
{
    idUser: (pole typu int)
    title: (pole typu string)
    completed: (pole typu boolean)
}

Następnie wysyła taki obiekt za pomocą funkcji post z biblioteki axios pod url: https://jsonplaceholder.typicode.com/todos
Jeśli dodanie zakończy się sukcesem - wyświetli w konsoli komunikat 'Dodano' i wyświetli id dodanego obiektu. W przeciwnym wypadku wypisze błąd.
*/

// 1.1
axios
  .get("https://jsonplaceholder.typicode.com/posts")
  .then((res) => {
    if (res.ok) return res;
    else throw "Błąd";
  })
  .then((res) => {
    const { body: data, headers } = res;

    console.log(data);
    console.log(headers);
  })
  .catch((err) => {
    console.log(err);
  });

// 1.2
const todo = {
  idUser: 1,
  title: "Tytuł",
  completed: false,
};

axios
  .post("https://jsonplaceholder.typicode.com/todos", todo)
  .then((res) => {
    if (res.status === 201) {
      console.log("Dodano");
      return res;
    } else throw "Błąd";
  })
  .then(() => {
    console.log(res.data.idUser);
  })
  .catch((err) => {
    console.log(err);
  });
