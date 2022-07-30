from collections import defaultdict
from itertools import combinations

def solution(infos, querys):
    answer = []
    info_dic = defaultdict(list)
    
    for info in infos :
        #1. info를 " "로 자르고, 숫자 따로 저장
        temp = info.split(" ")
        info_list = temp[:-1]
        info_score = int(temp[-1])
        
        #-의 개수는 0~4까지의 개수
        for dash_count in range(5) :
        #2. -의 조합 만들어주기
            dash_pos = list(combinations(range(4), dash_count))
            #print(dash_pos)

            #3. 2에서 만든 -의 위치를 뽑아서 info_list에 해당하는 위치마다 -로 바꿔주기
            for pos in dash_pos :
                #print(pos)
                info_dash = info_list[:]
                for p in pos :
                    info_dash[p] = "-"
                info_key = "".join(info_dash)
                info_dic[info_key].append(info_score)
    
    #4. socre 오름차순 정렬
    for item in info_dic :
        info_dic[item].sort()
    
    
    #5. querys를 돌면서 querys에 매칭되는 info_dic key가 점수가 있는지 확인
    for query in querys :
        #print(query)
        no_and_query = list(map(str, query.split(" and ")))        #and 제거
        no_and_query_head = no_and_query[:-1]
        no_and_query_tail = no_and_query[-1].split(" ")
        qurey_key = "".join(no_and_query_head + [no_and_query_tail[0]])
        qurey_score = int(no_and_query_tail[1])
        
        if qurey_key in list(info_dic) :
            #print("있음", qurey_key, info_dic[qurey_key])         #이중에서 이분검색으로 찾아야한다.
            search_score = info_dic[qurey_key]
            
            if len(search_score) > 0 :
                start, end = 0, len(search_score)
                
                while start != end and start != len(search_score) :
                    mid = (start  + end) // 2
                    
                    #현재 좌표 search_score[mid]가 찾는 점수보다 큰 작은 경우
                    #찾는 데이터는 mid 앞에 가있음 mid 오른쪽을 버림
                    if search_score[mid] >= qurey_score :
                        end = mid
                    #현재 좌표가 search_score[mid]보다 큰 경우 mid 왼쪽을 버림
                    else :
                        start = mid + 1
            answer.append(len(search_score) - start)
        else :
            answer.append(0)
                        
    
    return answer 
