function solution(phone_number) {
    var answer = '';
    let n = phone_number.length    
    let asterisk = "*".repeat(n-4)

    
    return asterisk + phone_number.slice(-4);
}

// def solution(phone_number):
//     n = len(phone_number)
//     asterisk = "*"*(n-4)
//     return asterisk+phone_number[-4:]