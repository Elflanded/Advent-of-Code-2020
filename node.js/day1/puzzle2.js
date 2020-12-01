const fs = require("fs");
const input = fs.readFileSync("node.js/day1/input.js", {encoding: "utf-8"});

const inputArray = input.split("\n").map(n => parseInt(n));
let numberA, numberB, numberC;
(() => {
  for (let i = 0; i < inputArray.length; i++) {
    for (let j = i + 1; j < inputArray.length; j++) {
      for (let k = j + 1; k < inputArray.length; k++) {
        if (inputArray[i] + inputArray[j] + inputArray[k] === 2020) {
          numberA = inputArray[i];
          numberB = inputArray[j];
          numberC = inputArray[k];
          return;
        }
      }
    }
  }
})();

console.log(numberA * numberB * numberC);