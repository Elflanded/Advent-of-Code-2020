const fs = require("fs");

const input = fs.readFileSync("../input.txt", {encoding: "utf-8"}).split("\n");

let validPasswords = 0;
for (let i = 0; i < input.length; i++) {
  let data = input[i].split(/:? /);
  let min = parseInt(data[0].split("-")[0]);
  let max = parseInt(data[0].split("-")[1]);
  let char = data[1];
  let pass = data[2];
  let matches = (pass.match(new RegExp(char, "g")) || []).length;
  if (matches >= min && matches <= max) validPasswords++;
}

console.log(validPasswords);
