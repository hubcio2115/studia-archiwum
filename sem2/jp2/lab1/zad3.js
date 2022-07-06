const arr = [0, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5];

for (let num of arr) {
  console.log(num);
}

console.log(`Najmniejsza liczba to ${Math.min.apply(Math, arr)}`);
console.log(`Największa liczba to ${Math.max.apply(Math, arr)}`);

console.log(arr.reverse());
