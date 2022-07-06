const counter = (max, timeout) => {
  const numbers = Array.from({ length: max }, (_, index) => index + 1);

  return () => {
    numbers.map((number, index) => {
      setTimeout(() => {
        console.log(number);
      }, timeout * index);
    });
  };
};

const counterInstance = counter(10, 500);
counterInstance();
