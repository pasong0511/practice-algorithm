function solution(arr) {
    let sum = 0
    
    arr.forEach(n => {
        sum += n    
    })
    
    
    
    return sum / arr.length;
}