# 오프닝 스킵하는 함수
def skip_opening(cm, cs, os_m, os_s, oe_m, oe_s):
    if cm > os_m or (cm == os_m and cs >= os_s):
        if cm < oe_m or (cm == oe_m and cs <= oe_s):
            return oe_m, oe_s
    return cm, cs
            
def solution(video_len, pos, op_start, op_end, commands):
    video_m, video_s = map(int, video_len.split(":"))
    os_m, os_s = map(int, op_start.split(":")) # 오프닝 시작
    oe_m, oe_s = map(int, op_end.split(":")) # 오프닝 끝
    
    current_m, current_s = map(int, pos.split(":"))
    for command in commands:
        # 오프닝 시간에 겹칠경우 스킵
        sm, ss = skip_opening(current_m, current_s, os_m, os_s, oe_m, oe_s)
        current_m, current_s = sm, ss
        
        # 이전으로 가는 명령어
        if command == "prev":
            current_s -= 10
            # 0초 이하일 경우
            if current_s < 0:
                current_m -= 1
                # 00:00 이하일경우 00:00로 이동
                if current_m < 0:
                    current_m, current_s = 0, 0
                else: 
                    current_s += 60
        
        # 앞으로 가는 명령어
        if command == "next":
            current_s += 10
        
        # 60초 이상인 경우
        if current_s > 59:
            current_m += 1
            current_s -= 60
            
        # 비디오 시간을 초과하는 경우 비디오 끝나는 시간으로 이동
        if current_m > video_m or (current_m == video_m and current_s >= video_s):
            current_m = video_m
            current_s = video_s
        
        # 명령어 전부 실행 후 오프닝 겹치는지 확인
        sm, ss = skip_opening(current_m, current_s, os_m, os_s, oe_m, oe_s)
        current_m, current_s = sm, ss
    
    answer = ''
    
    # 문자열 합치기
    if current_m < 10:
        answer += "0" + str(current_m) + ":"
    else:
        answer += str(current_m) + ":"
    if current_s < 10:
        answer += "0" + str(current_s)
    else:
        answer += str(current_s)
    
    return answer