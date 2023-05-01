let fs = require("fs");
//let input = fs.readFileSync("./test.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [a, b] = input[0].split(" ").map(Number);
let answer = 1;
let flag = false;

while (a <= b) {
    if (a === b) {
        flag = true;
        break;
    }

    //2로 나머지가 0인 경우 2로 나눠줌
    if (b % 2 === 0) {
        b = parseInt(b / 2);
        answer += 1;
    }
    //10으로 나눈 나머지가 1인 경우
    else if (b % 10 === 1) {
        b = parseInt(b / 10);
        answer += 1;
    } else {
        break;
    }
}

console.log(flag ? answer : -1);
