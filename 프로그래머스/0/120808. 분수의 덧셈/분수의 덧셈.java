class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int numer = numer1 * denom2 + numer2 * denom1; // 분자
        int denom = denom1 * denom2;  // 분모
        
        int gcd = getGCD(numer, denom);  // 최대공약수
        return new int[]{numer / gcd, denom / gcd};
    }
    
    // 유클리드 호제법으로 최대공약수 구하기
    private int getGCD(int a, int b) {
        while (b!= 0) {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }
}