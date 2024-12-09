class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        op=''
        if num>=1000:
            p=num//1000
            op+='M'*p
            num%=1000
        if num>=900:
            p=num//900
            op+='CM'*p
            num%=900
        if num>=500:
            p=num//500
            op+='D'*p
            num%=500
        if num>=400:
            p=num//400
            op+='CD'*p
            num%=400
        if num>=100:
            p=num//100
            op+='C'*p
            num%=100
        if num>=90:
            p=num//90
            op+='XC'*p
            num%=90
        if num>=50:
            p=num//50
            op+='L'*p
            num%=50
        if num>=40:
            p=num//40
            op+='XL'*p
            num%=40
        if num>=10:
            p=num//10
            op+='X'*p
            num%=10
        if num>=9:
            p=num//9
            op+='IX'*p
            num%=9
        if num>=5:
            p=num//5
            op+='V'*p
            num%=5
        if num>=4:
            p=num//4
            op+='IV'*p
            num%=4
        if num>=1:
            p=num//1
            op+='I'*p
            num%=1
        return op



        