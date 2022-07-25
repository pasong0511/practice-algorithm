function solution(n)
{
    var answer = 0;
    var strN = String(n).split("")
    for (let s of strN) {
        answer += Number(s)
    }

    return answer;
}