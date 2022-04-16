function solution(arr1, arr2) {
    var answer = []
    for(let i = 0; i < arr1.length ; i++){
        let sum = []
        for (let j = 0; j < arr1[i].length ; j++)  {
            sum.push(arr1[i][j] + arr2[i][j])
        }
        answer.push(sum)
    }
    return answer;
}


// def solution(arr1, arr2):
//     for i in range(len(arr1)) :
//         for j in range(len(arr1[0])):
//             arr1[i][j] += arr2[i][j] 
//     return arr1