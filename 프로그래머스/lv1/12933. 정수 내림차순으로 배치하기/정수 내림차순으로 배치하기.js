function solution(n) {
    let answer = '';
    let newStr = String(n).split("")
    newStr.sort().reverse()

    newStr.forEach((n) => {
        answer += n
    })
    
    return parseInt(answer)
}