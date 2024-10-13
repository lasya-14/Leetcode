class Solution {
    public int numIdenticalPairs(int[] nums) {
        int n=nums.length;
        HashMap<Integer,Integer> hm=new HashMap<>();
        int count=0;
        for(int i=0;i<n;i++){
            int val=nums[i];
            if(hm.containsKey(val)){
                count=count+hm.get(val);
                int curr=hm.get(val);
                hm.put(val,curr+1);
            }
            else{
                hm.put(val,1);
            }
            
        }
        return count;
        
    }
}