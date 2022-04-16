function solution(x, n) {
    var answer = [];
    
    for(let i=1; i <= n; i++) {
        answer.push(x*i)
    }
    
    return answer;
}


// def solution(x, n):
//     answer = []

//     for i in range(1, n+1):
//         answer.append(x*i)
//     print(answer)
//     return answer