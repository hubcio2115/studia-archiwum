const status = "Completed";

const runFunc = () => 1;

const runFunc2 = () => 0;

switch (status) {
  case "Completed":
    runFunc();
    break;
  case "Running":
    runFunc2();
    break;
}
