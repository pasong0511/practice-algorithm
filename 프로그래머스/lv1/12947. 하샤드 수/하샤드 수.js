function solution(x) {
    let str = x.toString()                      //문자열 변환
    let num = 0
    
    for (let i = 0; i < str.length; i++) {      //자리수길이만큼 반복
        num += parseInt(str[i])                 //int로 변환해서 합해줌
    }
    return x % num === 0 ? true : false         //x를 num으로 나누어서 나머지 찾기
}

//x의 자리수의 합이 x로 나누어져야함
//18의 자리수는 1 + 8 = 9
//18은 9로 나누어 떨어짐