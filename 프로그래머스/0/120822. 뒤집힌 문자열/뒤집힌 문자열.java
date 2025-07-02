class Solution {
    public String solution(String my_string) {
// StringBuilder 문자열을 다루기 위한 클래스, .reverse() 메서드를 통해 문자열을 뒤집고, .toString()으로 다시 문자열 형태로 반환
        return new StringBuilder(my_string).reverse().toString();
    }
}