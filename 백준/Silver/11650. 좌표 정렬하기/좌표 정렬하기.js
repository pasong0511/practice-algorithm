let fs = require("fs");
//let input = fs.readFileSync("./test.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let data = [];
for (let i = 1; i <= n; i++) {
    let [x, y] = input[i].split(" ").map(Number);
    data.push([x, y]);
}

const sortData = data.sort((a, b) => {
    if (a[0] != b[0]) {
        return a[0] - b[0];
    } else {
        return a[1] - b[1];
    }
});

let answer = "";
for (let item of sortData) {
    answer += `${item[0]} ${item[1]}\n`;
}

console.log(answer);
