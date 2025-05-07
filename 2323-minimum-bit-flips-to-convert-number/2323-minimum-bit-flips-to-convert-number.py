class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count=0
        max_bits = max(start.bit_length(), goal.bit_length())
        for i in range(max_bits):
            if ((start>>i)&1)!=((goal>>i)&1):
                count+=1
                start^=(1<<i)
        return count
        
        