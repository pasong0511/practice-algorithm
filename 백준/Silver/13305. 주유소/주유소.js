let isBaekjoon = true;
let fs = require("fs");
let input = isBaekjoon
    ? fs.readFileSync("/dev/stdin").toString().split("\n")
    : fs.readFileSync("./test.txt").toString().split("\n");

let n = Number(input[0]);
const loadList = input[1].split(" ").map((el) => Number(el));
const oilList = input[2].split(" ").map((el) => Number(el));

let minCost = 10001;
let sumCost = 0;
for (let i = 0; i < n - 1; i++) {
    //현재 도시를 기준으로 minCost 보다 작으면 그 도시에서 기름 넣고 가자
    if (minCost >= oilList[i]) {
        minCost = oilList[i]; //최소값 갱신
        sumCost += oilList[i] * loadList[i];
    }
    //현재 도시를 기준으로 minCost 보다 큰 경우 minCost 도시에서 기름 넣고 가는걸로 치자
    else {
        sumCost += minCost * loadList[i];
    }
}

console.log(sumCost);