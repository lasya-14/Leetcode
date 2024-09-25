class Solution {
    public int maxDistance(int[] colors) {
        int n=colors.length;
        int max=0;
        for(int i=n-1;i>=1;i--){
            if(colors[i]!=colors[0]){
                int value=i-0;
                max=Math.max(value,max);
                break;
            }
        }
        for(int i=0;i<n-1;i++){
            if(colors[n-1]!=colors[i]){
                int value=n-1-i;
                max=Math.max(value,max);
                break;
            }
        }
        
            
            
        return max;
    }
}