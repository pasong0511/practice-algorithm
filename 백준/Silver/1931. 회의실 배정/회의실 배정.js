let isBaekjoon = 1; //0로컬, 1백준
let fs = require("fs");
let input = isBaekjoon
    ? fs.readFileSync("/dev/stdin").toString().split("\n")
    : fs.readFileSync("./test.txt").toString().split("\n");

let n = Number(input[0]);
let roomList = [];
for (let i = 1; i <= n; i++) {
    roomList.push(input[i].split(" ").map(Number));
}

const sortRoomList = roomList.sort((a, b) => {
    if (a[1] != b[1]) {
        return a[1] - b[1];
    }

    return a[0] - b[0];
});

let count = 0;
let catchRoomTime = 0;

for (let i = 0; i < n; i++) {
    if (sortRoomList[i][0] >= catchRoomTime) {
        catchRoomTime = sortRoomList[i][1];
        count++;
    }
}

console.log(count);

//두번째껄로 오름차순 정렬
//바로 끝나는거 바로 뒤에있는거 수행
