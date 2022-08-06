function solution(n) {
    let num = String(n).split("").reverse().map((str) => parseInt(str))
    return num
}


// def solution(n):
//     arr = []
//     answer = [] 
    
//     for i in str(n) :
//         arr.append(i)
    
//     while arr :
//         answer.append(int(arr.pop()))
//     return answer