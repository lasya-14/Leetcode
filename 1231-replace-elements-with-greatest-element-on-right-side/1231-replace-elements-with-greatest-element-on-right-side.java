class Solution {
    public int[] replaceElements(int[] arr) {
        int len=arr.length;
        int max=0;
        for(int i=0;i<len;i++){
            int rightmax=-1;
            for(int j=i+1;j<len;j++){
                rightmax=Math.max(rightmax,arr[j]);
            }
            arr[i]=rightmax;

        }
        return arr;
        
    }
}