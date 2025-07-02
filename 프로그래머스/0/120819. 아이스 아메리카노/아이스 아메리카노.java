class Solution {
    public int[] solution(int money) {
        int cups = money /5500;
        int change = money %5500;
        int[] answer = {cups, change};
        return answer;
    }
}