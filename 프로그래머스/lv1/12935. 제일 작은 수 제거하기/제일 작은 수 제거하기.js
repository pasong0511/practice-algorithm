function solution(arr) {
    if (arr.length === 0) return -1
    if (arr.length === 1) return [-1]
    let minIdx = arr.indexOf(Math.min(...arr))
    
    arr.splice(minIdx, 1)

    
    let num = [0, 1, 2, 3, 4]
    console.log(num)
    num.splice(2, 0, 999)
    console.log(num)
    return arr
    
}
    
// def solution(arr):
//     min_num = min(arr)
//     arr.remove(min_num)
    
//     if len(arr) == 0:
//         arr.append(-1)
//         return arr
//     return arr