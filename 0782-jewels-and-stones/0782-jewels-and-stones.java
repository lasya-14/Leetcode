class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        HashMap<Character,Integer> hm=new HashMap<>();
        for(int i=0;i<stones.length();i++){
            char ch=stones.charAt(i);
            if(hm.containsKey(ch)){
                int curr=hm.get(ch);
                hm.put(ch,curr+1);

            }
            else{
                hm.put(ch,1);
            }
        }
        int ans=0;
        for(int i=0;i<jewels.length();i++){
            char cc=jewels.charAt(i);
            if(hm.containsKey(cc)){
                ans+=hm.get(cc);

            }
        }
        return ans;
        
    }
}