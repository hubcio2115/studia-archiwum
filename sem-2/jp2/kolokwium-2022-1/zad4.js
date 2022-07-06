"use strict";

class Log {
  constructor() {
    this.history = [];
  }
  write() {
    const temp = [...arguments].reduce((acc, argument) => {
      return typeof argument === "function"
        ? acc + argument.toString().replaceAll("\n", "").replaceAll(";", "")
        : acc + JSON.stringify(argument);
    }, "");

    this.history.push(temp);
    return temp;
  }
  printHistory(range) {
    if (arguments[0] === undefined) {
      return this.history
        .reduce((acc, element) => `${acc}\n${element}`, "")
        .slice(2);
    }
    if (arguments.length > 1) return "błąd";
    if (range.length !== 2) return "błąd";
    if (
      range.every((a) => {
        a > 0;
      })
    )
      return "błąd";
    if (range[0] < range[1]) return "błąd";

    this.history
      .slice(range[0], range[1])
      .reduce((acc, element) => `${acc}\n${element}`, "")
      .slice(2);
  }
  clearHistory() {
    this.history = [];
  }
}

const log = new Log();

log.write("test: ", () => {
  return "komunikat";
});

console.log(log.printHistory());
console.log(log.printHistory([1, 5]));
console.log(log.printHistory([5, 1]));
console.log(log.printHistory([-1, 5]));
console.log(log.printHistory([2]));

log.clearHistory();
console.log(log.printHistory() === "");
