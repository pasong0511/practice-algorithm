let fs = require("fs");
//let input = fs.readFileSync("./test.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = [...input[0]].map(Number);
const newN = n.sort((a, b) => b - a);

console.log(newN.join(""));
