const fs = require("fs");

const input = fs.readFileSync("./input.txt", {encoding: "utf-8"}).split("\n");

let validPasswords = 0;
for (let i = 0; i < input.length; i++) {
  let data = input[i].split(/:? /);
  let first = parseInt(data[0].split("-")[0]) - 1;
  let second = parseInt(data[0].split("-")[1]) - 1;
  let char = data[1];
  let pass = data[2];
  if (pass.charAt(first) === char && pass.charAt(second) === char) continue;
  if (pass.charAt(first) !== char && pass.charAt(second) !== char) continue; 
  validPasswords++;
}

console.log(validPasswords);
