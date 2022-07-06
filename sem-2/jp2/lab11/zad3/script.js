let counter = 0;
let interval;

const startCounter = () => {
  interval = setInterval(() => {
    console.log(counter);
    counter++;
  }, 1000);
};

const stopCounter = () => {
  clearInterval(interval);
};

const clearCounter = () => {
  counter = 0;
};
