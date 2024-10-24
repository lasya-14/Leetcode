class Solution {
    public int scoreOfString(String s) {
        int ans=0;
        for(int i=0;i<s.length()-1;i++){
            char first=s.charAt(i);
            char second=s.charAt(i+1);
            int temp=Math.abs(second-first);
            ans+=temp;
        }
        return ans;
    }
}