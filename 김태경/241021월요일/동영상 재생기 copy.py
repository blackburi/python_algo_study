def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    # 문자열 시간을 입력하면 초 단위로 바꿔주는 함수
    def change(string) :
        m, s = string.split(':')
        m, s = int(m), int(s)
        return 60*m+s
    
    # 비디오 길이
    video_len = change(video_len)
    # 현재 위치
    pos = change(pos)
    # 오프닝 시작
    op_start = change(op_start)
    # 오프닝 끝
    op_end = change(op_end)
    
    # 오프닝 사이에 있는 경우
    if op_start <= pos <= op_end :
        pos = op_end
    
    idx = 0
    while idx < len(commands) :
        command = commands[idx]
        
        # 명령어
        if command == "next" :
            pos += 10
        elif command == 'prev' :
            pos -= 10
            
        # 동영상 길이를 벗어난 경우
        if pos < 0 :
            pos = 0
        elif pos > video_len :
            pos = video_len
            
        # 오프닝 사이에 있는 경우
        if op_start <= pos <= op_end :
            pos = op_end
            
        idx += 1
            
    minute = pos//60
    second = pos%60
    
    if 0 <= minute <= 9 :
        minute = '0'+str(minute)
    else :
        minute = str(minute)
        
    if 0 <= second <= 9 :
        second = '0'+str(second)
    else :
        second = str(second)
        
    answer += minute + ':' + second
    
    return answer