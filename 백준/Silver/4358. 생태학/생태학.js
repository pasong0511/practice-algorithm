const fs = require("fs");

BOJkey = 0;

let input = fs
    .readFileSync(BOJkey ? "input.txt" : "./dev/stdin")
    .toString()
    .trim()
    .split("\n");

let dic = new Map();

for (let i = 0; i < input.length; i++) {
    if (dic.get(input[i])) {
        //상기시킨점
        dic.set(input[i], dic.get(input[i]) + 1);
    } else {
        dic.set(input[i], 1);
    }
}
// 상기시킨점
// let total = dic.size;
let total = input.length;
// console.log(total);
let result = [];
let per;
let strr = "";
// 상기시킨점 Map 순회
for (let tree of dic) {
    per = ((tree[1] / total) * 100).toFixed(4);
    strr = tree[0] + ` ${per}`;
    result.push(strr);
}

result.sort();
console.log(result.join("\n"));