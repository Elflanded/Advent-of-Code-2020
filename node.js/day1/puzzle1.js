const fs = require("fs");
const input = fs.readFileSync("node.js/day1/input.js", {encoding: "utf-8"});

const inputArray = input.split("\n").map(n => parseInt(n));
let numberA, numberB;
(() => {
  for (let i = 0; i < inputArray.length; i++) {
    for (let j = i + 1; j < inputArray.length; j++) {
      if (inputArray[i] + inputArray[j] === 2020) {
        numberA = inputArray[i];
        numberB = inputArray[j];
        return;
      }
    }
  }
})();

console.log(numberA * numberB);

