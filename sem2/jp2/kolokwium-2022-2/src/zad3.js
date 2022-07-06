"use strict";

import axios from "axios";

const id1 = Math.floor(Math.random() * 10);
const id2 = Math.floor(Math.random() * 100);

const funcArr = [
  () => axios.get("https://jsonplaceholder.typicode.com/photos"),
  () =>
    axios.post("https://jsonplaceholder.typicode.com/posts", {
      title: "Test",
      body: "Lorem ipsum",
      userId: 2,
    }),
  () => axios.get(`https://jsonplaceholder.typicode.com/users/${id1}`),
  () => axios.get("https://jsonplaceholder.typicode.com/todos"),
  () =>
    axios.put(`https://jsonplaceholder.typicode.com/posts/${id2}`, {
      id: id2,
      userId: 3,
      title: "New title",
      body: "New body",
    }),
];

const checkTime = (funTab) => {
  console.log("Start");

  let timer = 0;
  const interval = setInterval(() => {
    timer += 1;
    console.log(timer);
  }, 1000);

  const result = [];

  // a)
  funTab[0]().then((_) => {
    funTab[1]().then((_) => {
      funTab[2]().then((_) => {
        funTab[3]().then((_) => {
          funTab[4]().then((_) => {
            console.log("Zakończenie działania: scenariusz a)");
            result.push(timer);

            if (result.length === 2) {
              console.log("Koniec");
              console.log(`Czas działania: [${result.join(", ")}]`);
              clearInterval(interval);
            }
          });
        });
      });
    });
  });

  // b)
  Promise.all([...funTab].map((func) => func())).then((_) => {
    console.log("Zakończenie działania: scenariusz b)");
    result.push(timer);

    if (result.length === 2) {
      console.log("Koniec");
      console.log(`Czas działania: [${result.join(", ")}]`);
      clearInterval(interval);
    }
  });
};

checkTime(funcArr);
