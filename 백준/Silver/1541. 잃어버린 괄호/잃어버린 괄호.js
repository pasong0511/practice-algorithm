let fs = require("fs");
//let input = fs.readFileSync("./test.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

//1. 마이너스로 잘라준다
const group = input[0].split("-");

let answer = 0;
for (let i = 0; i < group.length; i++) {
    //2. 잘라진 그룹의 내부는 + 이므로 값을 키워준다.
    let current = group[i]
        .split("+")
        .map(Number)
        .reduce((a, b) => a + b, 0);

    //첫번째 그룹은 항상 덧셈
    if (i == 0) {
        answer += current;
    }
    //두번째 그룹 부터는 무조건 마이너스
    else {
        answer -= current;
    }
}

console.log(answer);
