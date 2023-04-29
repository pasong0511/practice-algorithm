let fs = require("fs");
//let input = fs.readFileSync("./test.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let arr = [];

for (let i = 1; i <= n; i++) {
    //onsole.log(input[i]);
    const age = Number(input[i].split(" ")[0]);
    const name = input[i].split(" ")[1];

    arr.push([age, name]);
}

const sortArr = arr.sort((a, b) => a[0] - b[0]);

let answer = "";
sortArr.forEach((item) => {
    answer += item[0] + " " + item[1] + "\n";
});

console.log(answer);
