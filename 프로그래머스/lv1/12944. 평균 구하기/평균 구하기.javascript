function solution(arr) {
    let sum = 0
    arr.forEach(n => {
        sum += n
    })
    
    return sum / arr.length;
}

// def solution(arr):
//     answer = 0
//     n = len(arr)
//     sum = 0
//     for i in arr : 
//         sum += i
//     answer = sum / n

//     return answer