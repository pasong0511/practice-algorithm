function solution(n) {
    var answer = [];
    let newN = String(n).split("")
    
    newN.forEach(i => {
        answer.push(Number(i))
    })
    answer.reverse()
    return answer;
}


// def solution(n):
//     arr = []
//     answer = [] 
    
//     for i in str(n) :
//         arr.append(i)
    
//     while arr :
//         answer.append(int(arr.pop()))
//     return answer