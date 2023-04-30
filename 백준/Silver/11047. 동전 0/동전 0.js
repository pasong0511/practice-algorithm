let fs = require("fs");
//let input = fs.readFileSync("./test.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [n, k] = input[0].split(" ").map(Number);
const coinList = [];

for (let i = 1; i <= n; i++) {
    coinList.push(Number(input[i]));
}

let count = 0;
//가장 가치가 큰 동전부터 확인
for (let i = n - 1; i >= 0; i--) {
    count += parseInt(k / coinList[i]); //해당 동전 몇개 사용해야 하는지 확인
    k %= coinList[i]; //해당 동전으로 거슬러 준 후 나머지
}

console.log(count);
