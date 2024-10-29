import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][] arr = new int[n][m];
        
        // 행별로 공격할 수 있는 파괴범의 수
        int[] canAttack = new int[n]; 
        
        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<m; j++) {
                int x = Integer.parseInt(st.nextToken());
                arr[i][j] = x;
                if (x > 0) {
                    canAttack[i] += 1;
                }
            }
        }

        for (int i=0; i<2; i++) {
            st = new StringTokenizer(br.readLine());
            int left = Integer.parseInt(st.nextToken()) - 1;
            int right = Integer.parseInt(st.nextToken()) - 1;

            while (left<=right) {
                // 공격할 파괴범이 없다면 스킵
                if (canAttack[left] == 0) {
                    left++;
                    continue;
                }
                for (int j=0; j<m; j++) {
                    if (arr[left][j] == 1) {
                        canAttack[left]--;
                        break;
                    }
                }
                left++;
            }
        }
        int answer = 0;
        for (int i=0; i<n; i++) {
            answer += canAttack[i];
        }
        System.out.println(answer);
    }
}
