const checkExchange = (money) => {
  let helper = 0;
  for (const current of money) {
    helper -= 5 * (current / 5 - 1);
    if (helper < 0) return false;
    helper += 5 * (current / 5);
  }

  return true;
};

console.log(checkExchange([5, 5, 5, 10, 20]));
console.log(checkExchange([5, 5, 10, 10, 20]));
console.log(checkExchange([10, 10]));
console.log(checkExchange([5, 5, 10]));
