class Solution {
    public int solution(String[][] board, int h, int w) {
        int answer = 0;
        int n = board.length;
        
        // 상하좌우
        int[] dy = {-1, 1, 0, 0};
        int[] dx = {0, 0, -1, 1};
        
        for (int d=0; d<4; d++) {
            int ny = dy[d] + h;
            int nx = dx[d] + w;
            
            if (0 <= ny && ny < n && 0 <= nx && nx < n) {
                if (board[ny][nx].equals(board[h][w])) {
                    answer++;
                }
            }
        }
        
        return answer;
    }
}