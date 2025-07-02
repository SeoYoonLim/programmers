class Solution {
    public String solution(String[] seoul) {
        int index = 0; // "Kim"이 있는 위치(index)를 저장할 변수

        for (int i = 0; i < seoul.length; i++) { // 배열 전체를 순회
            if (seoul[i].equals("Kim")) { // i번째 원소가 "Kim"과 같으면
                index = i; // index 변수에 해당 위치를 저장하고
                break; // 더 이상 반복할 필요 없으므로 중단
            }
        }

        return "김서방은 " + index + "에 있다"; // 최종 결과 문자열 반환
    }
}
