let isBaekjoon = 1; //0로컬, 1백준
let fs = require("fs");
let input = isBaekjoon
    ? fs.readFileSync("/dev/stdin").toString().split("\n")
    : fs.readFileSync("./test.txt").toString().split("\n");

let n = Number(input[0]);
let itemHights = input[1].split(" ").map(Number);
const currentHightArrow = Array(n).fill(0);
let arrowCount = 0;

for (hight of itemHights) {
    //현재 높이에 화살이 있는 경우 : 있던 화살로 쏨
    if (currentHightArrow[hight] > 0) {
        currentHightArrow[hight] -= 1; //기존 자리에 있던거는 없애줌
        currentHightArrow[hight - 1] += 1;
    }
    //현재 높이에 화살이 없는 경우 : 새로운 화살 장전
    else {
        arrowCount += 1;
        currentHightArrow[hight - 1] += 1;
    }
}

console.log(arrowCount);
