class Solution {
    public boolean isIsomorphic(String s, String t) {
        boolean result=true;
        HashMap<Character,Character> hm=new HashMap<>();
        HashMap<Character,Character> hm2=new HashMap<>();
        for(int i=0;i<s.length();i++){
            char ch1=s.charAt(i);
            char ch2=t.charAt(i);
            if(!hm.containsKey(ch1) && !hm2.containsKey(ch2)){
                hm.put(ch1,ch2);
                hm2.put(ch2,ch1);

            }
            else if(hm.containsKey(ch1)&& hm.get(ch1)!=ch2){
                result=false;
                break;
            }
            else if(hm2.containsKey(ch2)&& hm2.get(ch2)!=ch1){
                result=false;
                break;

            }
        }
        
        
        
        return result;
        
    }
}