class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer,Integer> hm=new HashMap<>();
        int n=nums.length;
        for(int i=0;i<nums.length;i++){
            int val=nums[i];
            if(hm.containsKey(val)){
                int curr=hm.get(val);
                hm.put(val,curr+1);
            }else{
                hm.put(val,1);
            }
        }
        for(int i:hm.keySet()){
            if(hm.get(i)>n/2){
                return i;
            }
        }
        return -1;
        
        
    }
}