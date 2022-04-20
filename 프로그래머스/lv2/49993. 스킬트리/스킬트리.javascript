function solution(skill, skill_trees) {
    let count = 0;
    let dic = {}
    
    //스킬 종류와 유지해야하는 순서의 인덱스를 딕셔너리로 저장
    //{키=스킬종류 : 밸류=순서번호}
    for (let i = 0; i<skill.length; i++) {
        dic[skill[i]] = i
    }
    
    console.log(dic)
    //skill_trees의 스킬트리 하나씩 뽑으면서 확인
    skill_trees.forEach((skill_tree) => {
        console.log(skill_tree)
        let check = new Array(skill.length)
        let flag = true

        skill_tree = String(skill_tree).split("")
        skill_tree.forEach((s) => {
            if (s !== -1) {
                check[dic[s]] = true
                
                for(let i = 0; i < dic[s]; i++) {
                    if (check[i] === undefined ) {
                        console.log("잘못된 스킬트리")
                        flag = false
                        break
                    }
                }
            }
        })
        if (flag == true) {
            count += 1
        }
        console.log("----------------------")
    })
    return count;
}