let fs = require("fs");
//let input = fs.readFileSync("./test.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let arr = input[1].split(" ").map(Number);

//1. 중복된 값을 없애기 위해서 set 수행
const uniqueArr = [...new Set(arr)];

//2. 오름차순 정렬 수행
const sortArr = uniqueArr.sort((a, b) => a - b);
//3. 0부터 순서 매기기(순서가 자기보다 작은거 개수를 갖고있음)
let myMap = new Map();
for (let i = 0; i < uniqueArr.length; i++) {
    myMap.set(uniqueArr[i], i);
}

//4. Map 객체에 있는거 객체 순서 꺼내오기
let answer = "";
for (let item of arr) {
    //console.log(item, myMap.get(item));
    answer += myMap.get(item) + " ";
}

console.log(answer);
