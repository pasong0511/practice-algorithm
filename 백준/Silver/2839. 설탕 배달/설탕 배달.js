let fs = require("fs");
//let input = fs.readFileSync("./test.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let answer = 0;

while (n >= 0) {

    if (n % 5 == 0 || n == 0) {
        answer += parseInt(n / 5);
        n = n % 5;
        break;
    }
    n -= 3;
    answer += 1;
}

if (n === 0) {
    console.log(answer);
} else {
    console.log(-1);
}
