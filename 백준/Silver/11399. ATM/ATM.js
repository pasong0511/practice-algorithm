let fs = require("fs");
//let input = fs.readFileSync("./test.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]);
const monyList = [...input[1].split(" ").map(Number)];
const sprtMonyList = monyList.sort((a, b) => a - b);
let sum = 0;
let answer = 0;
sprtMonyList.forEach((el) => {
    sum += el;
    answer += sum;
});

console.log(answer);
