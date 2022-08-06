function solution(arr1, arr2) {
    let answer = []
    
    for (let i = 0 ; i < arr1.length ; i++) {
        let temp = []
        for (let j = 0 ; j < arr1[i].length ; j++) {
            let sum = arr1[i][j] + arr2[i][j]
            temp.push(sum)
        }
        answer.push(temp)
    }
    
    return answer;
}