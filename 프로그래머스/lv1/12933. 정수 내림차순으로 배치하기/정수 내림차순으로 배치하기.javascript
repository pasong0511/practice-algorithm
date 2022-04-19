function solution(n) {
    let answer = '';
    let newStr = String(n).split("")
    newStr.sort().reverse()
    
    newStr.forEach(item => {
        answer += item
    })
    
    
    return Number(answer);

}
    // def solution(n):
    // answer = ''
    // arr = []
    // for i in str(n) :
    //     arr.append(i)
    // arr.sort(reverse = True)
    // for i in arr :
    //     answer+= i
    // return int(answer)