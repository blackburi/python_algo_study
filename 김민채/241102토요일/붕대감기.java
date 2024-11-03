class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = health;
        int time = 1;
        int conTime = 1; // 연속 시전시간
        int attackIdx = 0;
        while (attackIdx < attacks.length) {
            if (attacks[attackIdx][0] == time) {
                answer -= attacks[attackIdx][1];
                attackIdx++;
                if (answer <= 0) {
                    answer = -1;
                    break;
                }
                time++;
                conTime = 1;
                continue;
            }
            
            int heal = conTime == bandage[0] ? bandage[2] + bandage[1] : bandage[1];
            answer = answer + heal > health ? health : answer + heal;
            conTime++;
            conTime = conTime > bandage[0] ? 1 : conTime;
            time++;
            
        }
        
        return answer;
    }
}