class Solution {
    public int maximumDifference(int[] nums) {
        int max=-1;
        for(int i=0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){
                if(nums[i]<nums[j]){
                int temp=nums[j]-nums[i];
                if(temp>max){
                    max=temp;
                }
            }
            }

            }
            return max;
        }
    
        
    }
