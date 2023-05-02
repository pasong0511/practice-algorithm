let fs = require("fs");
//let input = fs.readFileSync("./test.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let s = Number(input[0]);
let sum = 0;
let count = 0;

while (true) {
    if (s < sum) {
        break;
    } else {
        count += 1;
        sum += count;
    }
}

console.log(count - 1);
