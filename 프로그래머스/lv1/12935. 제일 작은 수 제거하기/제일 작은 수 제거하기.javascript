function solution(arr) {
    var answer = [];
    if (arr.length === 1) {
        return [-1]
    } else {
        let min = Math.min(...arr)
        let minIndex = arr.indexOf(min)
        arr.splice(minIndex, 1)
    }
    return arr;
}
    
// def solution(arr):
//     min_num = min(arr)
//     arr.remove(min_num)
    
//     if len(arr) == 0:
//         arr.append(-1)
//         return arr
//     return arr