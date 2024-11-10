import java.util.*;

class Solution {
    public int solution(int[] mats, String[][] park) {
        int answer = -1; // 마지막에 출력할 답
        int result = -1; // 돗자리 깔 수 있는 가장 긴 변의 길이
        
        int n = park.length; // 세로
        int m = park[0].length; // 가로
        
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                
                // 빈공간일 경우
                if (park[i][j].equals("-1")) {
                    
                    // k만큼 빈공간 더 있는지 확인
                    int k = 1;
                    boolean isBreak = false;
                    boolean isEnter = false;
                    
                    while (k+i<n && k+j<m && !isBreak) {
                        isEnter = true;
                        for (int y=i; y<=k+i; y++) {
                            
                            // 종료 플래그 시 종료
                            if (isBreak) {
                                break;
                            }
                            
                            // k칸까지 빈칸이 아닐 경우 break
                            for (int x=j; x<=k+j; x++) {
                                if (!park[y][x].equals("-1")) {
                                    k--;
                                    isBreak = true;
                                    break;
                                }
                            }
                        }
                        
                        // 결과 업데이트
                        if (isEnter) {
                            result = Math.max(result, k+1);
                        }
                        
                        if (isBreak) {
                            break;
                        }
                        
                        // 길이 늘려서 다음 확인하기
                        k++;
                    }
                }
            }
        }
        // 가진 돗자리와 비교하여 결과 출력
        Arrays.sort(mats);
        for (int ma : mats) {
            if (ma <= result) {
                answer = ma;
            }
        }
        return answer;
    }
}