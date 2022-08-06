function solution(num) {
    let answer = 0
    let count = 0
    
    while (true) {
        if (num === 1) return count
        if (count === 500) return -1
        if (num % 2 === 0) {
            num = num / 2
            count += 1
        } else {
            num = (num * 3) + 1
            count += 1
        } 
    }
}

// function solution(num) {
//     let answer = 0;
//     let count = 0
//     while (true) {
//         if (num === 1) {
//             break
//         }
//         if (count === 500) {
//             break
//         }
//         if (num % 2 === 0) {
//             num = num / 2
//             count += 1
//             continue
//         }
//         if (num % 2 !== 0) {
//             num = (num * 3) + 1
//             count += 1
//             continue
//         }
//     }
    
//     if (count === 500) {
//         return -1
//     }
    
//     return count;
// }