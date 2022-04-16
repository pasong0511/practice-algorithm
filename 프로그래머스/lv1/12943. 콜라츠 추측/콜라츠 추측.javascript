function solution(num) {
    let answer = 0;
    let count = 0
    while (true) {
        if (num === 1) {
            break
        }
        if (count === 500) {
            break
        }
        if (num % 2 === 0) {
            num = num / 2
            count += 1
            continue
        }
        if (num % 2 !== 0) {
            num = (num * 3) + 1
            count += 1
            continue
        }
    }
    
    if (count === 500) {
        return -1
    }
    
    return count;
}


// def solution(num):
//     answer = 0
//     count = 0
//     while True :
//         if num == 1 :   #종료조건 1인경우
//             break
//         if count == 500 :   #종료조건 작업 500번 경과인 경우
//             break
//         if num % 2 == 0 :   #짝수인 경우
//             num = num // 2
//             count += 1
//             continue
//         if num % 2 != 0 :
//             num = (num * 3) + 1
//             count += 1
//             continue
    
//     if count == 500 :
//         return -1
//     return count