import java.io.*;
import java.util.*;

public class Main {
    static int answer = 0;
    static int n;
    static int m;
    static boolean[][] visited;
    static int[][] arr;

    // 좌표 설정을 위한 클래스
    public static class Position {
        int y;
        int x;

        public Position(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    // DFS 함수
    public static void dfs(Position[] friends, int time, int amount) {
        // 기저조건: 3초가 되면 최댓값 갱신 후 종료
        if (time >= 3) {
            answer = Math.max(amount, answer);
            return;
        }

        // 모든 친구들이 움직일 수 있는 모든 경우의 수 구함
        Position[][] canMove = new Position[friends.length][4];
        int[] dy = {-1, 1, 0, 0};
        int[] dx = {0, 0, -1, 1};
        
        // 각 친구들이 현재 좌표에서 이동할 수 있는 위치 모아두기
        for (int i = 0; i < friends.length; i++) {
            Position friend = friends[i];
            for (int d = 0; d < 4; d++) {
                int ny = friend.y + dy[d];
                int nx = friend.x + dx[d];

                // 이동 불가능하면 skip
                if (ny < 0 || nx < 0 || ny >= n || nx >= n || visited[ny][nx]) {
                    continue;
                }
                canMove[i][d] = new Position(ny, nx);
            }
        }

        // 가능한 모든 이동 조합을 생성
        List<Position[]> allCases = new ArrayList<>();
        generateAllCases(friends, canMove, 0, new Position[friends.length], allCases);

        // 각 조합에 대해 DFS 호출
        for (Position[] newPositions : allCases) {
            int newAmount = amount;
            
            // 새로운 위치 방문 표시 및 값 누적
            for (Position pos : newPositions) {
                if (pos != null) {
                    visited[pos.y][pos.x] = true;
                    newAmount += arr[pos.y][pos.x];
                }
            }

            // 재귀 호출
            dfs(newPositions, time + 1, newAmount);
            
            // 방문 상태 복구
            for (Position pos : newPositions) {
                if (pos != null) {
                    visited[pos.y][pos.x] = false;
                }
            }
        }
    }

    // 친구들이 "함께" 이동할 수 있는 모든 경우의수
    public static void generateAllCases(Position[] friends, Position[][] canMove, int idx, Position[] currentCase, List<Position[]> allCases) {
        // 모든 친구의 위치 설정 완료시 종료
        if (idx == friends.length) {
            allCases.add(currentCase.clone());
            return;
        }

        for (int d = 0; d < 4; d++) {
            if (canMove[idx][d] != null) {
                boolean cannotMove = false;
                // 다른친구의 경로와 겹치는 경우 안 됨
                for (int p=idx-1; p>=0; p--) {
                    if (currentCase[p].y == canMove[idx][d].y && currentCase[p].x == canMove[idx][d].x) {
                        cannotMove = true;
                        break;
                    }
                }
                if (cannotMove == true) {
                    continue;
                }
                currentCase[idx] = canMove[idx][d];
                // 다음 친구 설정하러 가기
                generateAllCases(friends, canMove, idx + 1, currentCase, allCases);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        // 맵 입력받기
        arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        Position[] friends = new Position[m]; // 친구 좌표
        visited = new boolean[n][n]; // 방문 표시

        int initialAmount = 0; // 시작 좌표 값의 합

        // 친구들의 위치 입력 받기
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            
            // 0부터 시작할 수 있도록 -1 해줌
            int y = Integer.parseInt(st.nextToken()) - 1; 
            int x = Integer.parseInt(st.nextToken()) - 1;

            // 생성자에 넣어서 생성한 뒤 친구 좌표 배열에 넣어주고 방문표시
            friends[i] = new Position(y, x);
            visited[y][x] = true;
            initialAmount += arr[y][x];
        }
        
        dfs(friends, 0, initialAmount);
        System.out.println(answer);
    }
}
